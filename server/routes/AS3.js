import express from "express";
import multer from "multer";
import { uploadThumbnailImage } from "../controllers/AS3Controller.js";

const storage = multer.memoryStorage();
const uploadFeature = multer({ storage: storage });

const router = express.Router();

router.post("/upload", uploadFeature.single("thumbnailImage"), uploadThumbnailImage);

export default router;
