import express from "express";
import { getAllUsers, getUserByGoogleId, getUserById, createOrUpdateUser } from "../controllers/userController.js";

const router = express.Router();

router.get("/", getAllUsers);
router.get("/getUserByGoogleId", getUserByGoogleId);
router.get("/:id", getUserById);
router.post("/createOrUpdateUser", createOrUpdateUser);

export default router;
