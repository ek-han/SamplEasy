// Default HTTP client library for ajax calls
import axios from "axios";
import storageService from "../helpers/storage";

export default function request(options) {
  // If token available, set it in headers
  if (storageService.getValue("token")) {
    axios.defaults.headers.common.Authorization = `Bearer ${storageService.getValue(
      "token"
    )}`;
  }

  return axios(options)
    .then((response) => response.data)
    .catch((error) => {
      console.log("Request Error:", error);
      throw error;
    });
}
