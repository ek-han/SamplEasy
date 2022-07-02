import storageService from "../helpers/storage";

// AuthService
const authService = {
  endpoint: "auth",

  isAuthenticated() {
    return !!storageService.getValue("token");
  },
};

export default authService;
