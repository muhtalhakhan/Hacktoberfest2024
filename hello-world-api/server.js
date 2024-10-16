// Import the express library and dotenv
const express = require('express');
const dotenv = require('dotenv');

// Load the .env file
dotenv.config();

// Create an instance of an Express application
const app = express();

// Define a simple GET endpoint
app.get('/', (req, res) => {
    res.send('Hello, World!'); // Respond with "Hello, World!"
});

// Set the port for the server (load from .env if available)
const PORT = process.env.PORT ;

// Start the server and listen on the defined port
app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});
