import express from "express";
import mongoose from "mongoose";
import routes from "./routes/index.js";
import auth from "./middleware/auth.js";
import cors from "cors";
import path from "path";
import fs from "fs";
import https from "https";
import "./loadEnvironment.js";

const ATLAS_URI = process.env.SERVER_ATLAS_URI || "";
const PORT = process.env.VUE_APP_PORT || 3000;
const app = express();

// Middleware
app.use(cors({
  origin: "*",
  allowedHeaders: ["Content-Type", "secret-api-key"]
}));
app.use(express.json());
app.use("/api", auth);

// Connect to MongoDB using Mongoose with error handling
mongoose.connect(ATLAS_URI)
  .then(() => console.log("Connected to MongoDB"))
  .catch(err => {
    console.error("Failed to connect to MongoDB", err);
    process.exit(1);
  });

// All routes under "/api"
app.use("/api", routes);

// Serve static files from the Vue app
const __dirname = path.resolve();
app.use(express.static(path.join(__dirname, '../client/dist')));

// Handle client-side routing, return index.html for all non-API routes
app.get('*', (req, res) => {
  res.sendFile(path.join(__dirname, '../client/dist/index.html'));
});

// Global error handling
app.use((err, _req, res, next) => {
  console.error(err);
  res.status(500).send("Uh oh! An unexpected error occurred.");
});

if (process.env.NODE_ENV === "production") {
  const options = {
    key: fs.readFileSync("../privkey.pem"),
    cert: fs.readFileSync("../fullchain.pem")
  };
  
  https.createServer(options, app).listen(PORT, () => {
    console.log(`Express app listening on port: ${PORT}`);
  });
} else {
  app.listen(PORT, () => {
    console.log(`Express app listening on port: ${PORT}`);
  });
}
