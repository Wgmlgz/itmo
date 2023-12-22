// Create a new file, e.g., api.js

import axios from 'axios';

const api = axios.create({
  baseURL: 'http://localhost:3000', // Replace with your backend server URL
  timeout: 5000, // Set a reasonable timeout
});

export default api;
