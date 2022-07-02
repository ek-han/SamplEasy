<template>
  <div class="login">
    <div class="logo"></div>
    <div class="welcome-text">Welcome</div>
    <button class="login-button" @click="connect">
      <img
        class="spotify-logo"
        src="../assets/spotify-logo.png"
        alt="Spotify logo"
      />
      <span class="login-text">Login with Spotify</span>
    </button>
    <div>
      <input v-model="msg" />
      <button @click="sendMessage">send</button>
      <button @click="receiveMessages">receive</button>
      <div v-for="(m, i) in msgs" :key="i">{{ m }}</div>
    </div>
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
  gap: 6em;
  background: linear-gradient(
    85.99deg,
    #a5d4f7 -5.26%,
    #d6eaff 6.54%,
    #e3f2ff 12.44%,
    #091227 89.06%
  );
}
.logo {
  width: 430px;
  height: 260px;
  left: 425px;
  top: 146px;

  background: #d9d9d9;
}
.welcome-text {
  width: 386px;
  height: 24px;
  left: 448px;
  top: 562px;

  font-family: "Roboto Condensed", sans-serif;
  font-style: italic;
  font-weight: 700;
  font-size: 60px;
  line-height: 24px;

  display: flex;
  align-items: center;
  text-transform: uppercase;

  color: #000000;
}
.login-button {
  box-sizing: border-box;

  width: 716px;
  height: 124px;
  left: 275px;
  top: 697px;

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
  font-size: 3em;
}
</style>
