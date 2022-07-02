<template>
  <div class="browse-music">
    <div>BROWSE MUSIC</div>
    <div class="browse-music-header">
      <div class="genres-wrapper">
        <button v-if="state !== 'genreSelection'" @click="chooseGenres">
          Select genres
        </button>
        <button v-else @click="browse">Browse</button>
        <div v-if="selectedGenres.length === 0">None</div>
        <div v-else>
          <span class="genres-text" v-for="(g, i) in selectedGenres" :key="i">
            {{ g }}
          </span>
        </div>
      </div>
    </div>
    <div class="browse-music-content">
      <browse-content v-if="state === 'browse'" />
      <genre-selection v-if="state === 'genreSelection'" />
    </div>
  </div>
</template>

<script>
import { mapGetters } from "vuex";
import GenreSelection from "@/components/GenreSelection";
import BrowseContent from "@/components/BrowseContent";

export default {
  name: "BrowseMusic",
  components: { BrowseContent, GenreSelection },
  data() {
    return {
      state: "browse",
    };
  },
  computed: {
    ...mapGetters({
      selectedGenres: "selectedGenres",
      genreSeeds: "genreSeeds",
    }),
  },
  methods: {
    chooseGenres() {
      this.state = "genreSelection";
    },
    browse() {
      this.state = "browse";
    },
  },
};
</script>

<style scoped>
.browse-music {
  color: white;
}
</style>
