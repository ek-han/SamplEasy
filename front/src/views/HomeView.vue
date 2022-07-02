<template>
  <div>
    <div>Home</div>
    <button @click="disconnect">Disconnect</button>
    <button @click="load">Load</button>
    <div class="category">
      <div>Genre Seeds:</div>
      <div class="item" v-for="g in genreSeeds" :key="g">{{ g }}</div>
    </div>
  </div>
</template>

<script>
import storageService from "@/helpers/storage";
import { mapGetters } from "vuex";

export default {
  name: "HomeVue",
  computed: {
    ...mapGetters({
      genreSeeds: "genreSeeds",
    }),
  },
  methods: {
    disconnect() {
      storageService.removeValue("token");
      this.$router.push({ name: "login" });
    },
    load() {
      this.$store.dispatch("loadGenreSeeds");
    },
  },
};
</script>

<style scoped>
.category {
  margin-top: 10px;
}
.item {
  margin-left: 5px;
  margin-top: 2px;
}
</style>
