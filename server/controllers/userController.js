import User from "../models/User.js";

export async function getAllUsers(req, res) {
  try {
    const results = await User.find().limit(50);
    res.send(results).status(200);
  } catch (err) {
    res.status(500).json({ message: err.message });
  }
}

export async function getUserById(req, res) {
  const userId = req.params.id;

  try {
    const user = await User.findById(userId);
    if (!user) {
      return res.status(404).json({ message: "User not found" });
    }
    res.send(user).status(200);
  } catch (err) {
    res.status(500).json({ message: err.message });
  }
}

export async function getUserByGoogleId(req, res) {
  try {
    const { googleId } = req.query;

    const user = await User.findOne({ googleId: googleId });

    if (!user) {
      return res.status(404).json({ message: 'User not found' });
    }
 
    res.status(200).json(user);
  } catch (err) {
    res.status(500).json({ message: err.message });
  }
}

export async function getUserByEmail(req, res) {
  try {
    const { email } = req.query;

    const user = await User.findOne({ email: email });

    if (!user) {
      return res.status(404).json({ message: 'User not found' });
    }
 
    res.status(200).json(user);
  } catch (err) {
    res.status(500).json({ message: err.message });
  }
}

export async function createOrUpdateUser(req, res) {
  try {
    
    const { displayName, googleId, profilePicture, email, receiveEmails, role } = req.body;
    
    const username = email.split('@')[0];
    
    let existingUser = await User.findOne({ email: email });

    if (existingUser) {
      const updatedUser = await User.findOneAndUpdate(
        { email: email },
        { $set: {displayName, googleId, profilePicture, receiveEmails, role} },
        { new: true }
      );

      res.status(200).json({ message: "User updated successfully", user: updatedUser });
    } else {
      const newUser = new User({displayName, username, googleId, profilePicture, email, receiveEmails, role});

      await newUser.save();

      res.status(201).json({ message: "User created successfully", user: newUser });
    }
  } catch (err) {
    res.status(500).json({ message: err.message });
  }
}