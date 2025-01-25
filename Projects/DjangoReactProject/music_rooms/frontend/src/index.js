import React from "react";
import { createRoot } from "react-dom/client";
import HomePage from "./components/HomePage";

const appDiv = document.getElementById("app");
if (appDiv) {
  const root = createRoot(appDiv);
  root.render(<HomePage />);
}