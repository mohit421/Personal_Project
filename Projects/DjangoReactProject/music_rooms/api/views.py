from django.shortcuts import render
from rest_framework import generics, status
from .serializers import RoomSerializer, CreateRoomSerializer, UpdateRoomSerializer
from .models import Room
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse

# Endpoint is pretty much after the slash like /home /about



'''
- we have our room serializers  we get rid of main function
- What we are gonna do is write, that known as an API view that will actually will actually let us view a list of all of the different rooms.
- The first thing that we are gonna do is return this or remove this HttpResponse
'''

# def main(request):
#     return HttpResponse("<h1>Hello World</h1>")

'''
- generics.CreateAPIView :- What this is?
- It's a view that already set up to return to us all of the different rooms.So that's what this will do if we simply tell 
- it the queryset, which essentially is, what do we want to return, from here , we wanna return all of the Room objects
then we give a serializer class that is okay, These are rooms nOw, how do I convert this into some format That I can actually return.
Well we use the room serializers which again inherit from serializers.ModelSerializer
that's how how to handle Room model (Room class stuff) 
-  Now, we have view so we have to link url to it.

'''


# Create your views here.
class RoomView(generics.ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

'''
This should be our get room class now hook that up with an end point 
then go and add code to urls
'''

class GetRoom(APIView):
    serializer_class = RoomSerializer
    lookup_url_kwarg = 'code'

    def get(self, request, format=None):
        code = request.GET.get(self.lookup_url_kwarg)
        if code != None:
            room = Room.objects.filter(code=code)
            if len(room) > 0:
                data = RoomSerializer(room[0]).data
                data['is_host'] = self.request.session.session_key == room[0].host
                return Response(data, status=status.HTTP_200_OK)
            return Response({'Room Not Found': 'Invalid Room Code.'}, status=status.HTTP_404_NOT_FOUND)

        return Response({'Bad Request': 'Code paramater not found in request'}, status=status.HTTP_400_BAD_REQUEST)


class JoinRoom(APIView):
    lookup_url_kwarg = 'code'

    def post(self, request, format=None):
        if not self.request.session.exists(self.request.session.session_key):
            self.request.session.create()

        code = request.data.get(self.lookup_url_kwarg)
        if code != None:
            room_result = Room.objects.filter(code=code)
            if len(room_result) > 0:
                room = room_result[0]
                self.request.session['room_code'] = code
                return Response({'message': 'Room Joined!'}, status=status.HTTP_200_OK)

            return Response({'Bad Request': 'Invalid Room Code'}, status=status.HTTP_400_BAD_REQUEST)

        return Response({'Bad Request': 'Invalid post data, did not find a code key'}, status=status.HTTP_400_BAD_REQUEST)


'''
- What APIView will allow us to do is to  override some default 
 methods ... we can define get method and post method and put 
 method we can sent that type of request to this APIView and 
 it will automatically dispatch it to the correct method.

'''
class CreateRoomView(APIView):
    serializer_class = CreateRoomSerializer
    # Ensure the session exists
    def post(self, request, format=None):
        print("Received POST request:", request.data)
        if not self.request.session.exists(self.request.session.session_key):
            self.request.session.create()
        # Validate incoming data with the serializer
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            guest_can_pause = serializer.data.get('guest_can_pause')
            votes_to_skip = serializer.data.get('votes_to_skip')
            host = self.request.session.session_key
            # There is a possibility that a person trying to create a new room already has 
            # has an active room. IN that case, I don't want to make a new room for them. What I will do
            # instead is update their room settings so that guest_can_pause and votes_to_skips
            # or equal to whatever request they just sent us. SO this we will give them the same room code and 
            # and we'll return them to kind of original room that they were in
            # and update the settings that they just sent us.
            # Say a user has a multiple sessions or session expire and they restart
            # another session for some reason that would be fine . We would just create a new room for 
            # them and their old room would be just lost in database and all would be good
            # That would be totally fine cuz their session key has changed and no one's session 
            # will be equal to the same session key that already existed before
            
            # Check if the host already has an existing room
            queryset = Room.objects.filter(host=host)
            if queryset.exists():
                room = queryset[0]
                room.guest_can_pause = guest_can_pause
                room.votes_to_skip = votes_to_skip
                room.save(update_fields=['guest_can_pause', 'votes_to_skip'])
                # print('room existed')
                self.request.session['room_code'] = room.code 
                return Response(RoomSerializer(room).data, status=status.HTTP_200_OK)
            else:
                # Create a new room if none exists for the host
                room = Room(host=host, guest_can_pause=guest_can_pause,
                            votes_to_skip=votes_to_skip)
                room.save()
                # print("room created successfully")
                self.request.session['room_code'] = room.code 
                return Response(RoomSerializer(room).data, status=status.HTTP_201_CREATED)
         # Handle invalid data
        print('invalid request')
        return Response({'Bad Request': 'Invalid data...'}, status=status.HTTP_400_BAD_REQUEST)
    

class UserInRoom(APIView):
    def get(self, request, format=None):
        if not self.request.session.exists(self.request.session.session_key):
            self.request.session.create()
        data = {
            'code': self.request.session.get('room_code')
        }
        return JsonResponse(data, status=status.HTTP_200_OK)
    
class LeaveRoom(APIView):
    def post(self,request, format=None):
        if 'room_code' in self.request.session:
            self.request.session.pop('room_code')
            host_id = self.request.session.session_key
            room_results = Room.objects.filter(host=host_id)
            if len(room_results)>0:
                room = room_results[0]
                room.delete()
        
        return Response({'Message': 'Success'}, status=status.HTTP_200_OK)


class UpdateRoom(APIView):

    serializer_class = UpdateRoomSerializer
    
    def patch(self, request, format=None):
        if not self.request.session.exists(self.request.session.session_key):
            self.request.session.create()
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            guest_can_pause = serializer.data.get('guest_can_pause')
            votes_to_skip = serializer.data.get('votes_to_skip')
            code = serializer.data.get('code')

            queryset = Room.objects.filter(code=code)
            if not queryset.exists():
                return Response({"msg":"Room Not Found."}, status=status.HTTP_404_ROOM_NOT_FOUND)
            
            room = queryset[0]
            user_id = self.request.session.session_key
            if room.host != user_id:
                return Response({"msg":"Your are not the host of this Room."}, status=status.HTTP_403_FORBIDDEN)
            room.guest_can_pause= guest_can_pause
            room.votes_to_skip= votes_to_skip
            room.save(update_fields=['guest_can_pause','votes_to_skip'])
            return Response(RoomSerializer(room).data, status=status.HTTP_200_OK)
        return Response({'Bad Request':"Invalid Data..."}, status=status.HTTP_400_BAD_REQUEST)
