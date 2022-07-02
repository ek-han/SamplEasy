<template>
  <div>
    <div>Home</div>
    <button @click="disconnect">Disconnect</button>
  </div>
</template>

<script>
import storageService from "@/helpers/storage";

export default {
  name: "HomeVue",
  created() {
    this.$store.dispatch("loadTopArtists");
  },
  methods: {
    disconnect() {
      storageService.removeValue("token");
      this.$router.push({ name: "login" });
    },
  },
};
</script>

<style scoped></style>
