import React, { useState, useEffect } from "react";
import { Grid, Button, Typography, IconButton } from "@material-ui/core";
import NavigateBeforeIcon from "@material-ui/icons/NavigateBefore";
import NavigateNextIcon from "@material-ui/icons/NavigateNext";
import { Link } from "react-router-dom";

const pages = {
  JOIN: "pages.join",
  CREATE: "pages.create",
};

const Info = () => {
  const [page, setPage] = useState(pages.JOIN);

  useEffect(() => {
    console.log("ran");
    return () => console.log("cleanup");
  }, []); // Empty dependency array to run effect only once

  const handlePageChange = () => {
    setPage(page === pages.CREATE ? pages.JOIN : pages.CREATE);
  };

  return (
    <Grid container spacing={1}>
      <Grid item xs={12} align="center">
        <Typography component="h4" variant="h4">
          What is House Party?
        </Typography>
      </Grid>
      <Grid item xs={12} align="center">
        <Typography variant="body1">
          {page === pages.JOIN ? "Join page" : "Create page"}
        </Typography>
      </Grid>
      <Grid item xs={12} align="center">
        <IconButton onClick={handlePageChange}>
          {page === pages.CREATE ? (
            <NavigateBeforeIcon />
          ) : (
            <NavigateNextIcon />
          )}
        </IconButton>
      </Grid>
      <Grid item xs={12} align="center">
        <Button color="secondary" variant="contained" to="/" component={Link}>
          Back
        </Button>
      </Grid>
    </Grid>
  );
};

export default Info;