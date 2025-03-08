from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from rest_framework.views import APIView
from requests import Request, post
from rest_framework import status
from rest_framework.response import Response
from .util import *
from api.models import Room
from .models import Vote
import requests
import os
# AuthURL: Generates the Spotify authorization URL
class AuthURL(APIView):
    def get(self, request, format=None):
        scopes = 'user-read-playback-state user-modify-playback-state user-read-currently-playing'

        url = Request("GET", "https://accounts.spotify.com/authorize", params={
            "scope": scopes,
            "response_type": "code",
            "redirect_uri": os.getenv("REDIRECT_URI"),
            "client_id": os.getenv("CLIENT_ID"),
        }).prepare().url


        return Response({'url': url}, status=status.HTTP_200_OK)


# spotify_callback: Handles the Spotify callback for the authorization code


def spotify_callback(request, format=None):
    code = request.GET.get('code')
    error = request.GET.get('error')

    if error:
        return HttpResponseRedirect(reverse('frontend:home'))

    # Check if user already has tokens
    session_id = request.session.session_key
    if session_id and is_spotify_authenticated(session_id):
        return HttpResponseRedirect(reverse('frontend:home'))  # Already authenticated

    # Request token exchange
    response = post('https://accounts.spotify.com/api/token', data={
        'grant_type': 'authorization_code',
        'code': code,
        'redirect_uri': os.getenv('REDIRECT_URI'),
        'client_id': os.getenv('CLIENT_ID'),
        'client_secret': os.getenv('CLIENT_SECRET')
    }).json()

    if 'error' in response:
        return HttpResponseRedirect(reverse('frontend:home'))

    access_token = response.get('access_token')
    token_type = response.get('token_type')
    refresh_token = response.get('refresh_token')
    expires_in = response.get('expires_in')

    # Ensure session exists
    if not request.session.exists(request.session.session_key):
        request.session.create()

    update_or_create_user_tokens(request.session.session_key, access_token, token_type, expires_in, refresh_token)

    return HttpResponseRedirect(reverse('frontend:home'))




# IsAuthenticated: Checks if the user is authenticated with Spotify
class IsAuthenticated(APIView):
    def get(self, request, format=None):
        is_authenticated = is_spotify_authenticated(self.request.session.session_key)
        return Response({'status': is_authenticated}, status=status.HTTP_200_OK)


# CurrentSong: Fetches the current song playing in the room
class CurrentSong(APIView):
    def get(self, request, format=None):
        room_code = self.request.session.get('room_code')
        room = Room.objects.filter(code=room_code).first()

        if not room:
            return Response({}, status=status.HTTP_404_NOT_FOUND)

        host = room.host
        endpoint = "player/currently-playing"
        response = execute_spotify_api_request(host, endpoint)

        if 'error' in response or 'item' not in response:
            return Response({}, status=status.HTTP_204_NO_CONTENT)

        item = response.get('item')
        duration = item.get('duration_ms')
        progress = response.get('progress_ms')
        album_cover = item.get('album').get('images')[0].get('url')
        is_playing = response.get('is_playing')
        song_id = item.get('id')
        volume = item.get('volume')

        artist_string = ", ".join([artist.get('name') for artist in item.get('artists')])

        votes = len(Vote.objects.filter(room=room, song_id=song_id))

        song = {
            'title': item.get('name'),
            'artist': artist_string,
            'duration': duration,
            'time': progress,
            'image_url': album_cover,
            'is_playing': is_playing,
            'votes': votes,
            'votes_required': room.votes_to_skip,
            'id': song_id,
            'volume': getattr(room, 'volume', 50)  # Default to 50 if not set
        }

        self.update_room_song(room, song_id)

        return Response(song, status=status.HTTP_200_OK)

    def update_room_song(self, room, song_id):
        current_song = room.current_song

        if current_song != song_id:
            room.current_song = song_id
            room.save(update_fields=['current_song'])
            Vote.objects.filter(room=room).delete()


# ModifyVolume: Adjusts the volume of the current song
class ModifyVolume(APIView):
    def put(self, request, format=None):
        try:
            volume = request.data.get("volume")
            if volume is None or not isinstance(volume, int) or not (0 <= volume <= 100):
                return Response({"error": "Invalid volume value"}, status=status.HTTP_400_BAD_REQUEST)

            room_code = request.session.get("room_code")
            if not room_code:
                return Response({"error": "No room code found"}, status=status.HTTP_400_BAD_REQUEST)

            room = Room.objects.filter(code=room_code).first()
            if not room:
                return Response({"error": "Room not found"}, status=status.HTTP_404_NOT_FOUND)

            tokens = get_user_tokens(room.host)
            if not tokens:
                return Response({"error": "Host authentication failed"}, status=status.HTTP_401_UNAUTHORIZED)

            headers = {"Authorization": f"Bearer {tokens.access_token}"}
            endpoint = f"https://api.spotify.com/v1/me/player/volume?volume_percent={volume}"

            response = requests.put(endpoint, headers=headers)

            if response.status_code == 429:
                retry_after = response.headers.get("Retry-After", 5)
                return Response({"error": f"Rate limited. Retry after {retry_after} seconds"}, status=status.HTTP_429_TOO_MANY_REQUESTS)

            if response.status_code not in [200, 204]:
                return Response({"error": f"Spotify API error: {response.text}"}, status=response.status_code)

            return Response({"message": "Volume updated"}, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({"error": f"Internal server error: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# PauseSong: Pauses the current song in the room
class PauseSong(APIView):
    def put(self, request, format=None):
        room_code = self.request.session.get('room_code')
        room = Room.objects.filter(code=room_code).first()
        if room and (self.request.session.session_key == room.host or room.guest_can_pause):
            pause_song(room.host)
            return Response({}, status=status.HTTP_204_NO_CONTENT)

        return Response({}, status=status.HTTP_403_FORBIDDEN)


# PlaySong: Plays the current song in the room
class PlaySong(APIView):
    def put(self, request, format=None):
        room_code = self.request.session.get('room_code')
        room = Room.objects.filter(code=room_code).first()
        if room and (self.request.session.session_key == room.host or room.guest_can_pause):
            play_song(room.host)
            return Response({}, status=status.HTTP_204_NO_CONTENT)

        return Response({}, status=status.HTTP_403_FORBIDDEN)


# SkipSong: Skips the current song in the room
class SkipSong(APIView):
    def post(self, request, format=None):
        room_code = self.request.session.get('room_code')
        room = Room.objects.filter(code=room_code).first()
        if not room:
            return Response({"error": "Room not found"}, status=status.HTTP_404_NOT_FOUND)

        votes = Vote.objects.filter(room=room, song_id=room.current_song)
        votes_needed = room.votes_to_skip

        if self.request.session.session_key == room.host or len(votes) + 1 >= votes_needed:
            votes.delete()
            skip_song(room.host)
            room.current_song = None
            room.save(update_fields=['current_song'])
        else:
            vote, created = Vote.objects.get_or_create(
            user=self.request.session.session_key,  # ✅ If storing votes by session
            room=room,
            song_id=room.current_song
        )


            if not created:
                return Response({'message': 'You have already voted'}, status=status.HTTP_400_BAD_REQUEST)

        return Response({}, status=status.HTTP_204_NO_CONTENT)


# PrevSong: Goes back to the previous song in the room
class PrevSong(APIView):
    def post(self, request, format=None):
        room_code = self.request.session.get('room_code')
        room = Room.objects.filter(code=room_code).first()
        if not room:
            return Response({"error": "Room not found"}, status=status.HTTP_404_NOT_FOUND)

        votes = Vote.objects.filter(room=room, song_id=room.current_song)
        votes_needed = room.votes_to_skip

        if self.request.session.session_key == room.host or len(votes) + 1 >= votes_needed:
            votes.delete()  # Reset votes before going to previous song
            prev_song(room.host)
            room.current_song = None  # Ensure update_room_song is triggered
            room.save(update_fields=['current_song'])
        else:
            vote, created = Vote.objects.get_or_create(
                user=self.request.session.session_key,
                room=room,
                song_id=room.current_song
            )
            if not created:
                return Response({'message': 'You have already voted'}, status=status.HTTP_400_BAD_REQUEST)

        return Response({}, status=status.HTTP_204_NO_CONTENT)


class RepeatCurrentSong(APIView):
    def put(self, request, format=None):
        room_code = self.request.session.get('room_code')
        room = Room.objects.filter(code=room_code).first()

        if not room:
            return Response({"error": "Room not found"}, status=status.HTTP_404_NOT_FOUND)

        # Get the host (who controls playback)
        host = room.host
        tokens = get_user_tokens(host)

        if not tokens:
            return Response({"error": "Host authentication failed"}, status=status.HTTP_401_UNAUTHORIZED)

        # ✅ Get current repeat mode
        playback_info = execute_spotify_api_request(host, "player")
        current_repeat_mode = playback_info.get("repeat_state", "off")  # Default to 'off'

        repeat_modes = ["off", "context", "track"]  # Off -> Playlist -> Repeat One

        try:
            current_index = repeat_modes.index(current_repeat_mode)
            next_repeat_mode = repeat_modes[(current_index + 1) % len(repeat_modes)]
        except ValueError:
            next_repeat_mode = "off"  # Default if API doesn't return a valid mode

        # ✅ Update repeat mode on Spotify
        endpoint = f"https://api.spotify.com/v1/me/player/repeat?state={next_repeat_mode}"
        headers = {"Authorization": f"Bearer {tokens.access_token}"}
        response = requests.put(endpoint, headers=headers)

        if response.status_code not in [200, 204]:
            return Response({"error": f"Spotify API error: {response.text}"}, status=response.status_code)

        return Response({"message": f"Repeat mode set to {next_repeat_mode}"}, status=status.HTTP_200_OK)
