// Import the Express module
const express = require("express");

// Create a new Express application
const app = express();

// Define a route for the root URL
app.get("/", (req, res) => {
  res.send("Hi FossHack this is :bitspace, W");
});

// Start the server on port 3000
const PORT = 3000;
app.listen(PORT, () => {
  console.log(`Server is running on http://localhost:${PORT}`);
});
