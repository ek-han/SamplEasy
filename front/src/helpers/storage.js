const storageService = {
  setValue(key, hash) {
    localStorage.setItem(key, hash);
  },
  getValue(key) {
    return localStorage.getItem(key);
  },
  removeValue(key) {
    return localStorage.setItem(key, "");
  },
};

export default storageService;
