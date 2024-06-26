import dotenv from 'dotenv';
import path from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const envFilePath = process.env.NODE_ENV === 'production' ? '../.env.production' : '../.env.development';

dotenv.config({ path: path.resolve(__dirname, envFilePath) });
