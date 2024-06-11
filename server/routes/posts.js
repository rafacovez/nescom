import express from "express";
import {
  getAllPosts,
  getLatestPosts,
  getPostById,
  getPostByUrl,
  updatePostById,
  createPost,
  deletePostById
} from "../controllers/postController.js";

const router = express.Router();

router.get("/getPostById/:id", getPostById);
router.get("/getPostByURL/:url", getPostByUrl);
router.post("/updatePostById/:id", updatePostById);
router.delete("/deletePostById/:id", deletePostById);
router.post("/createPost", createPost);
router.get("/getLatest", getLatestPosts);
router.get("/", getAllPosts);

export default router;
