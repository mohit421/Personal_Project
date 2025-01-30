import React, { useState, useEffect } from "react";
import { useParams, useNavigate } from "react-router-dom";
import { Grid, Typography, Button } from "@mui/material";
import CreateRoomPage from "./CreateRoomPage";

const Room = () => {
  const { roomCode } = useParams();
  const navigate = useNavigate();

  const [votesToSkip, setVotesToSkip] = useState(2);
  const [guestCanPause, setGuestCanPause] = useState(false);
  const [isHost, setIsHost] = useState(false);
  const [showSettings, setShowSettings] = useState(false);
  const [spotifyAuthenticated, setSpotifyAuthenticated] = useState(false);
  const [song, setSong] = useState(null);

  const componentDidMount = () =>{
    interval = setInterval(getCurrentSong, 1000)
  }

  const componentWillUnmount = () => {
    clearInterval(interval)
  }

  useEffect(() => {
    const getRoomDetails = () => {
      fetch(`/api/get-room?code=${roomCode}`)
        .then((response) => {
          if (!response.ok) {
            throw new Error("Failed to fetch room details");
          }
          return response.json();
        })
        .then((data) => {
          setVotesToSkip(data.votes_to_skip);
          setGuestCanPause(data.guest_can_pause);
          setIsHost(data.is_host);

          if (data.is_host) {
            authenticateSpotify();
          }
        })
        .catch((error) => console.error("Error fetching room details:", error));
    };

    const authenticateSpotify = () => {
      fetch("/spotify/is-authenticated")
        .then((response) => response.json())
        .then((data) => {
          setSpotifyAuthenticated(data.status);
          if (!data.status) {
            fetch("/spotify/get-auth-url")
              .then((response) => response.json())
              .then((data) => {
                window.location.replace(data.url);
              })
              .catch((error) =>
                console.error("Error getting Spotify auth URL:", error)
              );
          }
        })
        .catch((error) =>
          console.error("Error checking Spotify authentication:", error)
        );
    };

    getRoomDetails();
  }, [roomCode]);

  useEffect(() => {
    const getCurrentSong = () => {
      fetch("/spotify/current-song")
        .then((response) => {
          if (!response.ok) {
            return {};
          }
          return response.json();
        })
        .then((data) => {
          setSong(data);
          console.log(data)
        }
          
      )
        .catch((error) =>
          console.error("Error fetching current song:", error)
        );
    };

    getCurrentSong();
    const interval = setInterval(getCurrentSong, 5000); // Fetch song every 5 seconds
    return () => clearInterval(interval); // Cleanup on unmount
  }, []);

  const leaveButtonPressed = () => {
    const requestOptions = {
      method: "POST",
      headers: { "Content-Type": "application/json" },
    };

    fetch("/api/leave-room", requestOptions)
      .then((response) => {
        if (response.ok) {
          navigate("/");
        } else {
          console.error("Error leaving room");
        }
      })
      .catch((error) => console.error("Error leaving room:", error));
  };

  const renderSettings = () => {
    return (
      <Grid container spacing={1}>
        <Grid item xs={12} align="center">
          <CreateRoomPage
            update={true}
            votesToSkip={votesToSkip}
            guestCanPause={guestCanPause}
            roomCode={roomCode}
            updateCallback={() => {
              setShowSettings(false);
              fetch(`/api/get-room?code=${roomCode}`)
                .then((response) => response.json())
                .then((data) => {
                  setVotesToSkip(data.votes_to_skip);
                  setGuestCanPause(data.guest_can_pause);
                })
                .catch((error) =>
                  console.error("Error refreshing room details:", error)
                );
            }}
          />
        </Grid>
        <Grid item xs={12} align="center">
          <Button
            variant="contained"
            color="secondary"
            onClick={() => setShowSettings(false)}
          >
            Close
          </Button>
        </Grid>
      </Grid>
    );
  };

  const renderSettingsButton = () => (
    <Grid item xs={12} align="center">
      <Button
        variant="contained"
        color="primary"
        onClick={() => setShowSettings(true)}
      >
        Settings
      </Button>
    </Grid>
  );

  return (
    <Grid container spacing={1}>
      {showSettings ? (
        renderSettings()
      ) : (
        <>
          <Grid item xs={12} align="center">
            <Typography variant="h6">Room Code: {roomCode}</Typography>
          </Grid>

          {song ? (
            <Grid item xs={12} align="center">
              <Typography variant="h6">Now Playing:</Typography>
              <Typography variant="subtitle1">{song.title}</Typography>
              <Typography variant="subtitle2">
                By: {song.artist || "Unknown"}
              </Typography>
              <img
                src={song.image_url}
                alt="Album Cover"
                style={{ width: "200px", borderRadius: "10px" }}
              />
            </Grid>
          ) : (
            <Grid item xs={12} align="center">
              <Typography variant="h6">No song currently playing</Typography>
            </Grid>
          )}

          {isHost && renderSettingsButton()}
          <Grid item xs={12} align="center">
            <Button
              color="secondary"
              variant="contained"
              onClick={leaveButtonPressed}
            >
              Leave Room
            </Button>
          </Grid>
        </>
      )}
    </Grid>
  );
};

export default Room;
