import mongoose from "mongoose";

const { Schema } = mongoose;

const postSchema = new Schema(
  {
    title: {
      type: String,
      required: true,
    },
    author: {
      type: mongoose.Schema.Types.ObjectId,
      ref: "User",
      required: true,
    },
    content: {
      type: String,
      required: true,
    },
    categoryTags: {
      type: [String],
    },
    thumbnailImage: {
      type: String,
    },
    url: {
      type: String,
      required: true,
      unique: true,
    },
    viewsReadCount: {
      type: Number,
      default: 0,
    },
    likesReactions: {
      type: Number,
      default: 0,
    },
    comments: {
      type: [String],
      default: [],
    },
    featured: {
      type: Boolean,
      default: false,
    },
    status: {
      type: String,
      enum: ["published", "draft", "archived"],
      default: "draft",
    },
    relatedArticles: {
      type: [mongoose.Schema.Types.ObjectId],
      ref: "Post",
    },
  },
  {
    timestamps: true,
  }
);

const Post = mongoose.model("Post", postSchema);

export default Post;
