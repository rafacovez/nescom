const path = require("path");
const dotenv = require("dotenv");

const envPath =
  process.env.NODE_ENV === "production"
    ? path.resolve(__dirname, "../.env.production")
    : path.resolve(__dirname, "../.env.development");

dotenv.config({ path: envPath });
