import Post from "../models/Post.js";

export async function getAllPosts(req, res) {
  const postStatus = req.query.status;

  try {
    const results = await Post.find({ status: postStatus }).sort({ createdAt: -1 }).limit(50);
    res.send(results).status(200);
  } catch (err) {
    res.status(500).json({ message: err.message });
  }
}

export async function getLatestPosts(req, res) {
  try {
    const results = await Post.find().sort({ createdAt: -1 }).limit(4);
    res.send(results).status(200);
  } catch (err) {
    res.status(500).json({ message: err.message });
  }
}

export async function createPost(req, res) {
  try {
    const { title, author, content, categoryTags, thumbnailImage, url, viewsReadCount, likesReactions, comments, featured, status } = req.body;

    const newPost = new Post({title, author, content, categoryTags, thumbnailImage, url, viewsReadCount, likesReactions, comments, featured, status});

    await newPost.save();

    res.status(201).json({ message: "Post created successfully", post: newPost });
  } catch (err) {
    res.status(500).json({ message: err.message });
  }
}

export async function getPostById(req, res) {
  const postId = req.params.id;

  try {
    const post = await Post.findById(postId);

    if (!post) {
      return res.status(404).json({ message: "Post not found" });
    }
    res.send(post).status(200);
  } catch (err) {
    res.status(500).json({ message: err.message });
  }
}

export async function getPostByUrl(req, res) {
  const postUrl = req.params.url;

  try {
    const post = await Post.findOne({ url: postUrl });
    if (!post) {
      return res.status(404).json({ message: "Post not found" });
    }
    res.send(post).status(200);
  } catch (err) {
    res.status(500).json({ message: err.message });
  }
}

export async function updatePostById(req, res) {
  const postId = req.params.id;

  try {
    const { title, author, content, categoryTags, thumbnailImage, url, viewsReadCount, likesReactions, comments, featured, status } = req.body;

    const existingPost = await Post.findOne({ _id: postId });

    if (existingPost) {
      const updatedPost = await Post.findOneAndUpdate(
        { _id: postId },
        { $set: {title, author, content, categoryTags, thumbnailImage, url, viewsReadCount, likesReactions, comments, featured, status} },
        { new: true }
      );

      res.send(updatedPost).status(200);
    } else {
      const newPost = new Post({title, author, content, categoryTags, thumbnailImage, url, viewsReadCount, likesReactions, comments, featured, status});

      await newPost.save();

      res.send(newPost).status(201);
    }
  } catch (err) {
    res.status(500).json({ message: err.message });
  }
}

export async function deletePostById(req, res) {
  const postId = req.params.id;

  try {
    const existingPost = await Post.findOne({ _id: postId });

    if (existingPost) {
      await Post.deleteOne({ _id: postId });

      res.status(200).json({ message: "Post deleted successfully." });
    } else {
      res.status(404).json({ message: "Post not found." });

    }
  } catch (err) {
    res.status(500).json({ message: err.message });
  }
}
