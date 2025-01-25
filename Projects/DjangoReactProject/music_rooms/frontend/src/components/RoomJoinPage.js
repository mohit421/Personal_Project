import React, { useState } from "react";
import { TextField, Button, Grid, Typography } from "@mui/material";
import { Link, useNavigate } from "react-router-dom";

export default function RoomJoinPage() {
  const [roomCode, setRoomCode] = useState(""); // State for room code
  const [error, setError] = useState(""); // State for error message
  const navigate = useNavigate(); // Hook for navigation

  const handleTextFieldChange = (e) => {
    setRoomCode(e.target.value); // Update room code as user types
    setError(""); // Clear error when user starts typing
  };

  const roomButtonPressed = () => {
    if (!roomCode) {
      setError("Room code is required");
      return;
    }

    const requestOptions = {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        code: roomCode, // Send the room code to the server
      }),
    };

    fetch("/api/join-room", requestOptions)
      .then((response) => {
        if (response.ok) {
          navigate(`/room/${roomCode}`); // Navigate to the room if successful
        } else {
          setError("Room Not Found."); // Show error if room code is invalid
        }
      })
      .catch((error) => {
        console.error("Error:", error);
        setError("An error occurred. Please try again."); // Handle fetch errors
      });
  };

  return (
    <Grid container spacing={1} alignItems="center" justifyContent="center" style={{ marginTop: "20px" }}>
      <Grid item xs={12} align="center">
        <Typography variant="h4" component="h4">
          Join A Room
        </Typography>
      </Grid>
      <Grid item xs={12} align="center">
        <TextField
          error={Boolean(error)} // Shows red outline if there's an error
          label="Room Code"
          placeholder="Enter a Room Code"
          value={roomCode} // Controlled input
          helperText={error} // Display error message below the input
          variant="outlined"
          onChange={handleTextFieldChange} // Handle input change
        />
      </Grid>
      <Grid item xs={12} align="center">
        <Button
          variant="contained"
          color="primary"
          onClick={roomButtonPressed} // Handle join room logic
        >
          Enter Room
        </Button>
      </Grid>
      <Grid item xs={12} align="center">
        <Button
          variant="contained"
          color="secondary"
          component={Link}
          to="/" // Link back to home page
        >
          Back
        </Button>
      </Grid>
    </Grid>
  );
}
