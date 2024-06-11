import express from "express";

// Import routes
import posts from "./posts.js";
import users from "./users.js";
import emails from "./emails.js";
import AS3 from "./AS3.js";

const router = express.Router();

// Mount routes
router.use("/posts", posts);
router.use("/users", users);
router.use("/emails", emails);
router.use("/media", AS3);

export default router;
