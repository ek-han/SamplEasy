<template>
  <div>
    <div>Login view</div>
    <button @click="connect">Connect with spotify</button>
  </div>
</template>

<script>
import storageService from "@/helpers/storage";

export default {
  name: "LoginView",
  data() {
    return {
      connectLink:
        "http://accounts.spotify.com/authorize?" +
        "client_id=28ffcff09ef14b88883d00d860f4c680&" +
        "client_secret=9e206a28d9934fd9812251d25de963f5&" +
        "response_type=token&" +
        "redirect_uri=http://localhost:8080/callback&" +
        "scope=user-top-read&" +
        "show_dialog=true",
    };
  },
  methods: {
    connect() {
      const popup = window.open(
        this.connectLink,
        "Login with Spotify",
        "width=800,height=600"
      );

      window.spotifyCallback = async (token) => {
        storageService.setValue("token", token);
        await this.$router.push({ name: "home" });
        if (popup) {
          popup.close();
        }
      };
    },
  },
};
</script>

<style scoped></style>
