<template>
  <div class="browse-wrapper">
    <button @click="$emit('changeView')">Change Filters</button>
    <div class="current-filters-wrapper">
      <div>
        <div v-if="filters.key !== null">
          Key: {{ availableKeys[filters.key] }}
        </div>
        <div v-if="filters.tempo !== null">Tempo: {{ filters.tempo }}</div>
        <div v-if="filters.genres.length !== 0">
          Genres:
          <span
            style="margin-left: 5px"
            v-for="(g, i) in filters.genres"
            :key="i"
            >{{ g }}</span
          >
        </div>
      </div>
    </div>
    <div class="browse-content">
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
      recommendations: "recommendations",
      filters: "filters",
      availableKeys: "availableKeys",
    }),
  },
  mounted() {
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
