#!/bin/bash

# Start the Node.js server in the background
cd server
npm run start &

# Start the React.js development server (or build for production)
cd ../client
npm run dev
