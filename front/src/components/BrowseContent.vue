<template>
  <div class="browse-wrapper">
    <div v-if="selectedGenres.length === 0">No Genre Selected</div>
    <div v-else class="browse-content">
      <div v-for="r in recommendations" :key="r.id">
        {{ r.name }} {{ r.mainArtist }} {{ r.popularity }}
      </div>
    </div>
  </div>
</template>

<script>
import { mapGetters } from "vuex";

export default {
  name: "BrowseContent",
  computed: {
    ...mapGetters({
      selectedGenres: "selectedGenres",
      recommendations: "recommendations",
    }),
  },
  mounted() {
    if (this.selectedGenres.length !== 0)
      this.$store.dispatch("GetRecommendations");
  },
};
</script>

<style scoped>
.browse-content {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}
</style>
