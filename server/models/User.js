import mongoose from "mongoose";

const { Schema } = mongoose;

const userSchema = new Schema(
  {
    displayName: {
      type: String,
      required: true,
    },
    username: {
      type: String,
      required: true,
      unique: true,
    },
    googleId: {
      type: String,
      unique: true,
    },
    profilePicture: {
      type: String,
    },
    email: {
      type: String,
      required: true,
      unique: true,
    },
    receiveEmails: {
      type: Boolean,
      default: false,
    },
    role: {
      type: String,
      enum: ["notify","registered", "admin"],
      default: "notify",
    },
  },
  { timestamps: true }
);

const User = mongoose.model("User", userSchema);

export default User;
