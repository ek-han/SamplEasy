<template>
  <div class="home">
    <header-component />
    <div class="content">
      <chat-component v-if="activeTab === 'chat'" />
      <my-gallery v-if="activeTab === 'gallery'" />
      <browse-music v-if="activeTab === 'music'" />
    </div>
  </div>
</template>

<script>
import { mapGetters } from "vuex";
import HeaderComponent from "@/components/HeaderComponent";
import BrowseMusic from "@/components/BrowseMusic";
import ChatComponent from "@/components/ChatComponent";
import MyGallery from "@/components/MyGallery";

export default {
  name: "HomeVue",
  components: { MyGallery, ChatComponent, BrowseMusic, HeaderComponent },
  computed: {
    ...mapGetters({
      genreSeeds: "genreSeeds",
      activeTab: "activeTab",
    }),
  },
  methods: {
    load() {
      this.$store.dispatch("loadGenreSeeds");
    },
  },
};
</script>

<style scoped>
.home {
  height: 100%;
  width: 100%;
  background-color: #091227;
  position: relative;
}
.content {
  width: 100%;
  position: relative;
}
</style>
