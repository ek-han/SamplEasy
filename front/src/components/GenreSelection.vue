<template>
  <div class="genre-selection">
    <div v-for="(gs, i) in genreSeeds" :key="i" class="genre-input">
      <input
        v-model="gs.selected"
        :disabled="maxGenreSelected(gs)"
        type="checkbox"
      />
      <span class="genre-text">{{ gs.name }}</span>
    </div>
  </div>
</template>

<script>
import { mapGetters } from "vuex";

export default {
  name: "GenreSelection",
  computed: {
    ...mapGetters({
      genreSeeds: "genreSeeds",
      selectedGenres: "selectedGenres",
    }),
  },
  created() {
    this.$store.dispatch("loadGenreSeeds");
  },
  methods: {
    // toggleGenre(genre) {
    //   this.$store.commit("toggleGenre", genre);
    // },
    maxGenreSelected(gs) {
      return (
        this.selectedGenres.length === 5 &&
        !this.selectedGenres.includes(gs.name)
      );
    },
  },
};
</script>

<style scoped>
.genre-selection {
  display: flex;
  flex-wrap: wrap;
  justify-content: flex-start;
  gap: 10px;
}
.genre-input {
  margin: 5px;
  width: 10rem;
  font-size: 1.5rem;
}
.genre-text {
  margin-left: 5px;
}
</style>
