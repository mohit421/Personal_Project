import React from "react";
import { createRoot } from "react-dom/client"; // React 18+


// // Main App Component
const App = () => (
  <div className="center">
    <HomePage />
  </div>
);

// Initialize the App
const appDiv = document.getElementById("app");
if (appDiv) {
  createRoot(appDiv).render(<App />);
}
