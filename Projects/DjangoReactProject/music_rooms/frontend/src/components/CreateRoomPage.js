import React, { useState } from "react";
import Button from "@mui/material/Button";
import TextField from "@mui/material/TextField";
import Typography from "@mui/material/Typography";
import FormHelperText from "@mui/material/FormHelperText";
import FormControl from "@mui/material/FormControl";
import Radio from "@mui/material/Radio";
import RadioGroup from "@mui/material/RadioGroup";
import FormControlLabel from "@mui/material/FormControlLabel";
import Grid from "@mui/material/Grid";
import {Link, useNavigate } from "react-router-dom";

export default function CreateRoomPage() {
  const defaultVotes = 2;
  const [guestCanPause, setGuestCanPause] = useState(true);
  const [votesToSkip, setVotesToSkip] = useState(defaultVotes);
  const navigate = useNavigate();

  const handleVotesChange = (e) => {
    const value = parseInt(e.target.value, 10);
    setVotesToSkip(value > 0 ? value : 1); // Ensure value is at least 1
  };

  const handleGuestCanPauseChange = (e) => {
    setGuestCanPause(e.target.value === "true");
  };

  const handleRoomButtonPressed = () => {
    const requestOptions = {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        votes_to_skip: votesToSkip,
        guest_can_pause: guestCanPause,
      }),
    };

    fetch("/api/create-room", requestOptions)
      .then((response) => {
        if (!response.ok) {
          throw new Error("Failed to create room");
        }
        return response.json();
      })
      .then((data) => {
        navigate(`/room/${data.code}`); // Redirect to the new room page
      })
      .catch((error) => console.error("Error creating room:", error));
  };

  return (
    <Grid
      container
      spacing={0}
      alignItems="center"
      justifyContent="center"
      style={{ marginTop: "20px" }}
    >
      <Grid item xs={12} align="center" style={{ marginBottom: "10px" }}>
        <Typography component="h4" variant="h4">
          Create A Room
        </Typography>
      </Grid>

      <Grid item xs={12} sm={8} md={6} align="center" style={{ marginBottom: "10px" }}>
        <FormControl component="fieldset">
          <FormHelperText>
            <div align="center">Guest Control of Playback State</div>
          </FormHelperText>
          <RadioGroup row value={guestCanPause.toString()} onChange={handleGuestCanPauseChange}>
            <FormControlLabel
              value="true"
              control={<Radio color="primary" />}
              label="Play/Pause"
            />
            <FormControlLabel
              value="false"
              control={<Radio color="secondary" />}
              label="No Control"
            />
          </RadioGroup>
        </FormControl>
      </Grid>

      <Grid item xs={12} sm={8} md={6} align="center" style={{ marginBottom: "10px" }}>
        <FormControl>
          <TextField
            required
            type="number"
            onChange={handleVotesChange}
            value={votesToSkip}
            inputProps={{
              min: 1,
              style: { textAlign: "center" },
            }}
          />
          <FormHelperText>
            <div align="center">Votes Required To Skip Song</div>
          </FormHelperText>
        </FormControl>
      </Grid>

      <Grid item xs={12} align="center" style={{ marginBottom: "10px" }}>
        <Button color="secondary" variant="contained" onClick={handleRoomButtonPressed}>
          Create A Room
        </Button>
      </Grid>

      <Grid item xs={12} align="center">
        <Button
          variant="contained"
          color="primary"
          component={Link}
          to="/" // Link back to home page
        >
          Back
        </Button>
      </Grid>
    </Grid>
  );
}
