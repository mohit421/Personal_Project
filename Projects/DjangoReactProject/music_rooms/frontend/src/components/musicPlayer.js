import React, { useEffect, useState } from "react";
import {
  Grid,
  Typography,
  Card,
  IconButton,
  LinearProgress,
  Slider,
} from "@mui/material";
import PlayArrowIcon from "@mui/icons-material/PlayArrow";
import PauseIcon from "@mui/icons-material/Pause";
import SkipNextIcon from "@mui/icons-material/SkipNext";
import SkipPreviousIcon from "@mui/icons-material/SkipPrevious";
import { VolumeUp, VolumeOff } from "@mui/icons-material";
import { debounce } from "lodash";
import RepeatIcon from "@mui/icons-material/Repeat";
import RepeatOneIcon from "@mui/icons-material/RepeatOne";

// ✅ Debounced volume change function (prevents too many API requests)
const debouncedVolumeChange = debounce(async (newVolume) => {
  try {
    const response = await fetch("/spotify/volume/", {
      method: "PUT",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ volume: newVolume }),
    });

    if (!response.ok) throw new Error("Failed to update volume");

    console.log("✅ Volume updated successfully!");
  } catch (error) {
    console.error("❌ Volume update error:", error);
  }
}, 500);

// ✅ Repeat Button Component
const RepeatButton = ({ repeatMode, onToggleRepeat }) => (
  <IconButton onClick={onToggleRepeat} color={repeatMode ? "primary" : "default"}>
    {repeatMode === 2 ? <RepeatOneIcon /> : <RepeatIcon />}
  </IconButton>
);

// ✅ Volume Control Component
const VolumeControl = ({ volume, onVolumeChange }) => {
  const [localVolume, setLocalVolume] = useState(volume ?? 50); // ✅ Ensure default value
  const [muted, setMuted] = useState(false);

  // ✅ Keep local state in sync when `volume` changes
  useEffect(() => {
    if (volume !== undefined) {
      setLocalVolume(volume);
    }
  }, [volume]);

  const handleVolumeChange = (newValue) => {
    setLocalVolume(newValue);
    debouncedVolumeChange(newValue);
    onVolumeChange(newValue);
  };

  const toggleMute = () => {
    const newMutedState = !muted;
    setMuted(newMutedState);
    const newVolume = newMutedState ? 0 : (volume ?? 50); // ✅ Ensure fallback
    setLocalVolume(newVolume);
    debouncedVolumeChange(newVolume);
    onVolumeChange(newVolume);
  };

  return (
    <Grid container alignItems="center" spacing={2} sx={{ width: 250 }}>
      <Grid item>
        <IconButton onClick={toggleMute} color="primary">
          {muted || localVolume === 0 ? <VolumeOff /> : <VolumeUp />}
        </IconButton>
      </Grid>

      <Grid item xs>
        <Slider
          value={muted ? 0 : localVolume} // ✅ Ensure `value` is always defined
          onChange={(e, newValue) => handleVolumeChange(newValue)}
          min={0}
          max={100}
          step={1}
          aria-labelledby="continuous-slider"
          sx={{
            color: "green",
            "& .MuiSlider-thumb": {
              width: 15,
              height: 15,
            },
          }}
        />
      </Grid>
    </Grid>
  );
};

// ✅ Main MusicPlayer Component
const MusicPlayer = ({
  image_url,
  title,
  artist,
  is_playing,
  time,
  duration,
  votes,
  votes_required,
  volume,
}) => {
  const [localVolume, setLocalVolume] = useState(volume || 50);
  const [repeatMode, setRepeatMode] = useState(0); // 0 = Off, 1 = Repeat All, 2 = Repeat One

  useEffect(() => {
    setLocalVolume(volume);
  }, [volume]);

  const toggleRepeat = async () => {
    try {
      // Define repeat modes as per Spotify API: "off", "context" (repeat all), "track" (repeat one)
      const modes = ["off", "context", "track"];
      
      // Determine the next mode
      const newMode = modes[(repeatMode + 1) % 3];
  
      // ✅ Send request to Spotify API
      const response = await fetch("http://127.0.0.1:8000/spotify/repeat/", {
        method: "PUT",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ state: newMode }), // Send repeat mode in request
      });
  
      if (!response.ok) {
        throw new Error("Failed to update repeat mode");
      }
  
      // ✅ Update state after a successful request
      setRepeatMode((prev) => (prev + 1) % 3);
      console.log(`✅ Repeat mode set to: ${newMode}`);
    } catch (error) {
      console.error("❌ Error setting repeat mode:", error);
    }
  };
  

  const skipSong = async () => {
    await fetch("/spotify/skip", { method: "POST", headers: { "Content-Type": "application/json" } });
  };

  const prevSong = async () => {
    await fetch("/spotify/prev", { method: "POST", headers: { "Content-Type": "application/json" } });
  };

  const pauseSong = async () => {
    await fetch("/spotify/pause", { method: "PUT", headers: { "Content-Type": "application/json" } });
  };

  const playSong = async () => {
    await fetch("/spotify/play", { method: "PUT", headers: { "Content-Type": "application/json" } });
  };

  const songProgress = (time / duration) * 100;

  return (
    <Card>
      <Grid container alignItems="center">
        <Grid item align="center" xs={4}>
          <img src={image_url} alt="Album Cover" height="100%" width="100%" />
        </Grid>
        <Grid item align="center" xs={8}>
          <Typography component="h5" variant="h5">
            {title}
          </Typography>
          <Typography color="textSecondary" variant="subtitle1">
            {artist}
          </Typography>
          <div>
            <IconButton onClick={prevSong}>
              {votes} / {votes_required}
              <SkipPreviousIcon />
            </IconButton>
            <IconButton onClick={is_playing ? pauseSong : playSong}>
              {is_playing ? <PauseIcon /> : <PlayArrowIcon />}
            </IconButton>
            <IconButton onClick={skipSong}>
              {votes} / {votes_required}
              <SkipNextIcon />
            </IconButton>

            {/* ✅ Use RepeatButton Component */}
            <RepeatButton repeatMode={repeatMode} onToggleRepeat={toggleRepeat} />
          </div>

          {/* ✅ Volume Control Component */}
          <VolumeControl volume={localVolume} onVolumeChange={setLocalVolume} />
        </Grid>
      </Grid>
      <LinearProgress variant="determinate" value={songProgress} />
    </Card>
  );
};

export default MusicPlayer;
