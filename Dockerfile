# Use an official Node runtime as a parent image
FROM node:16

# Set the working directory for the server
WORKDIR /usr/src/app

# Copy server package.json and package-lock.json
COPY server/package*.json ./server/

# Install server dependencies
RUN cd ./server && npm install

# Set the working directory for the client
WORKDIR /usr/src/app

# Copy client package.json and package-lock.json
COPY client/package*.json ./client/

# Install client dependencies
RUN cd ./client && npm install

# Copy the rest of the server and client application code
COPY . .

# Expose the ports the app runs on
EXPOSE 3000 8080

# Make start.sh executable
RUN chmod +x ./start.sh

# Debug step: Verify start.sh permissions
RUN ls -la ./start.sh

# Run the application
CMD ["bash", "./start.sh", "development"]
