<template>
  <div class="filter-info">
    <div class="filter-info-header">
      <div class="filter-title">Current Filter:</div>
      <button @click="$emit('changeView')">Change</button>
    </div>
    <div class="current-filters-wrapper">
      <div class="current-filter">
        <div class="filer-name">Key:</div>
        <div class="filter-value">{{ filters.key ? availableKeys[filters.key] : "none" }}</div>
      </div>
      <div class="current-filter">
        <div class="filer-name">Tempo:</div>
        <div class="filter-value">{{ filters.tempo || "none" }}</div>
      </div>
      <div class="current-filter">
        <div class="filer-name">Genres:</div>
        <div v-if="filters.genres.length === 0" class="filter-value">none</div>
        <div v-else class="filter-value">{{ filters.genres.join(", ") }}</div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapGetters } from "vuex";

export default {
  name: "FilterInfo",
  computed: {
    ...mapGetters({
      recommendations: "recommendations",
      filters: "filters",
      availableKeys: "availableKeys",
    }),
  },
};
</script>

<style scoped>
.filter-info {
  font-size: 1.5rem;
  margin-bottom: 20px;
}
.filter-info-header {
  display: flex;
  gap: 20px;
}
.filter-title {
  font-size: 2rem;
}
.current-filters-wrapper {
  margin-left: 20px;
  display: flex;
  flex-direction: column;
  gap: 10px;
}
.current-filter {
  display: flex;
}
.filer-name {
  width: 5rem;
}
</style>
