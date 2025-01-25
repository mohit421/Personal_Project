import React, { useState, useEffect } from "react";
import { useParams } from "react-router-dom";

const Room = () => {
  const { roomCode } = useParams(); // Get roomCode from URL parameters
  const [votesToSkip, setVotesToSkip] = useState(2);
  const [guestCanPause, setGuestCanPause] = useState(false);
  const [isHost, setIsHost] = useState(false);

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

  return (
    <div>
      <h3>Room Code: {roomCode}</h3>
      <p>Votes Required to Skip: {votesToSkip}</p>
      <p>Guest Can Pause: {guestCanPause ? "Yes" : "No"}</p>
      <p>Host: {isHost ? "Yes" : "No"}</p>
    </div>
  );
};

export default Room;
