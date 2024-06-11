import axios from "axios";

const axiosInstance = axios.create({
  baseURL: process.env.VUE_APP_URL,
});

axiosInstance.interceptors.request.use(
  (config) => {
    config.headers["secret-api-key"] = process.env.VUE_APP_API_KEY;
    return config;
  },
  (error) => {
    return Promise.reject(error);
  }
);

export default axiosInstance;
