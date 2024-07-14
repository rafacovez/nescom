import express from "express";
import {
  getAllUsers,
  getUserByGoogleId,
  getUserByEmail,
  getUserById,
  createOrUpdateUser
} from "../controllers/userController.js";

const router = express.Router();

router.get("/", getAllUsers);
router.get("/getUserByGoogleId", getUserByGoogleId);
router.get("/getUserByEmail", getUserByEmail);
router.get("/:id", getUserById);
router.post("/createOrUpdateUser", createOrUpdateUser);

export default router;
