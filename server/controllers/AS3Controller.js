import { S3Client, PutObjectCommand } from "@aws-sdk/client-s3";
import sharp from "sharp";
import crypto from "crypto";
import "../loadEnvironment.js";

export async function uploadThumbnailImage(req, res) {
  const randomImageName = (bytes = 32) => crypto.randomBytes(bytes).toString("hex") + ".webp";

  try {
    const webpBuffer = await sharp(req.file.buffer)
    .resize(1200, 800)
    .webp()
    .toBuffer();

    const client = new S3Client({
      credentials: {
        accessKeyId: process.env.SERVER_AS3_ACCESS_KEY,
        secretAccessKey: process.env.SERVER_AS3_SECRET_KEY,
      },
      region: process.env.SERVER_AS3_REGION,
    });

    let key = req.params.key;

    if (!key) {
      key = `posts-thumbnails/${randomImageName()}`;
    
      console.log("New key:", key);
    }
    
    console.log("Same key:", key);
    
    const params = {
      Bucket: process.env.SERVER_AS3_BUCKET,
      Key: key,
      Body: webpBuffer,
      ContentType: "image/webp",
    };
    
    const putCommand = new PutObjectCommand(params);
    await client.send(putCommand);

    const url = `https://${process.env.SERVER_AS3_BUCKET}.s3.${process.env.SERVER_AS3_REGION}.amazonaws.com/${key}`;

    res.status(200).json({ url });
  } catch (error) {
    console.error("Error uploading media:", error);
    res.status(500).json({ error: "Failed to upload media" });
  }
}