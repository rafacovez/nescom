import "../loadEnvironment.js";

const auth = async (req, res, next) => {
  const apiKey = req.headers["secret-api-key"];
  const validApiKey = process.env.SERVER_API_KEY;

  if (!apiKey) {
    return res.status(404).json({ message: "API key is missing." });
  }

  if (apiKey !== validApiKey) {
    return res.status(403).json({ message: "Invalid API key." });
  }

  try {
    next();
  } catch (error) {
    console.error("Error verifying API key:", error);
    return res.status(401).json({ message: "Invalid API key." });
  }
};

export default auth;
