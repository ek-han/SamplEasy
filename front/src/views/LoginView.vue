<template>
  <div class="login">
    <div class="welcome-text">SamplEasy</div>
    <button class="login-button" @click="connect">
      <img
        class="spotify-logo"
        src="../assets/spotify-logo.png"
        alt="Spotify logo"
      />
      <span class="login-text">Login with Spotify</span>
    </button>
  </div>
</template>

<script>
import storageService from "@/helpers/storage";

export default {
  name: "LoginView",
  data() {
    return {
      msg: "",
      msgs: [],
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
    sendMessage() {
      this.$store.dispatch("sendMessage", { msg: this.msg });
    },
    receiveMessages() {
      this.$store.dispatch("receiveMessages").then((msgs) => {
        console.log("RECEIVED:", msgs);
        this.msgs = msgs;
      });
    },
  },
};
</script>

<style lang="scss" scoped>
.login {
  position: absolute;
  padding-top: 5em;
  width: 100%;
  height: 100%;
  overflow: hidden;
  display: flex;
  flex-direction: column;
  align-content: center;
  justify-content: center;
  align-items: center;
  gap: 4em;
}

.welcome-text {
  width: 386px;
  height: 24px;
  top: 562px;

  font-family: "Gotham", sans-serif;
  font-weight: 700;
  font-size: 80px;
  line-height: 24px;

  display: flex;
  align-items: center;
  align-content: center;
  justify-content: center;

  color: white;
}
.login-button {
  box-sizing: border-box;

  width: 500px;
  height: 124px;
  top: 697px;

  align-content: center;
  justify-content: center;

  background: rgba(255, 255, 255, 0.05);
  border: 3px solid rgba(0, 0, 0, 0.31);
  border-radius: 117px;

  &:hover {
    background: rgba(200, 200, 200, 0.5);
  }

  display: flex;
  padding: 1.5em;
  align-content: center;
  justify-content: center;
  align-items: center;
  gap: 2em;
}
.spotify-logo {
  width: 80px;
  height: 78px;
}
.login-text {
  font-family: "Gotham", sans-serif;
  font-size: 2em;
  color: white;
}
</style>
