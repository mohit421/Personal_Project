import React, { useState, useEffect } from "react";
import { useParams, useNavigate } from "react-router-dom";
import { Grid, Typography, Button } from "@mui/material";
import CreateRoomPage from "./CreateRoomPage";

const Room = () => {
  const { roomCode } = useParams(); // Get roomCode from URL parameters
  const navigate = useNavigate(); // Hook for navigation
  const [votesToSkip, setVotesToSkip] = useState(2);
  const [guestCanPause, setGuestCanPause] = useState(false);
  const [isHost, setIsHost] = useState(false);
  const [showSettings, setShowSettings] = useState(false); // Manage showSettings state
  
  // Fetch room details when the component mounts
  useEffect(() => {
    getRoomDetails();
  }, [roomCode]);

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
      })
      .catch((error) => console.error("Error fetching room details:", error));
  };

  // Function to handle leave button press
  const leaveButtonPressed = () => {
    const requestOptions = {
      method: "POST",
      headers: { "Content-Type": "application/json" },
    };

    fetch("/api/leave-room", requestOptions)
      .then((response) => {
        if (response.ok) {
          navigate("/"); // Redirect to home after leaving room
        } else {
          console.error("Error leaving room");
        }
      })
      .catch((error) => console.error("Error leaving room:", error));
  };

  // Function to render settings content
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
              getRoomDetails(); // Refresh room details after update
            }}
          />
        </Grid>
        <Grid item xs={12} align="center">
          <Button
            variant="contained"
            color="secondary"
            onClick={() => setShowSettings(false)} // Fix onClick handler
          >
            Close
          </Button>
        </Grid>
      </Grid>
    );
  };

  // Function to render settings button
  const renderSettingsButton = () => {
    return (
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
  };

  return (
    <Grid container spacing={1}>
      {showSettings ? (
        renderSettings()
      ) : (
        <>
          <Grid item xs={12} align="center">
            <Typography variant="h6" component="h6">
              Room Code: {roomCode}
            </Typography>
          </Grid>
          <Grid item xs={12} align="center">
            <Typography variant="h6" component="h6">
              Votes Required to Skip: {votesToSkip}
            </Typography>
          </Grid>
          <Grid item xs={12} align="center">
            <Typography variant="h6" component="h6">
              Guest Can Pause: {guestCanPause ? "Yes" : "No"}
            </Typography>
          </Grid>
          <Grid item xs={12} align="center">
            <Typography variant="h6" component="h6">
              Host: {isHost ? "Yes" : "No"}
            </Typography>
          </Grid>
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
