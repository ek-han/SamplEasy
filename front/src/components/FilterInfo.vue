<template>
  <div class="filter-info">
    <div class="filter-info-header">
      <div class="filter-title">Filter</div>
      <button class="change-button" @click="$emit('changeView')">CHANGE</button>
    </div>
    <div class="current-filters-wrapper">
      <div class="current-filter">
        <div class="filer-name">Popularity:</div>
        <div class="filter-value">{{ filters.popularity?.name || "none" }}</div>
      </div>
      <div class="current-filter">
        <div class="filer-name">Genres:</div>
        <div v-if="filters.genres.length === 0" class="filter-value">none</div>
        <div v-else class="filter-value">{{ filters.genres.join(", ") }}</div>
      </div>
      <div class="current-filter">
        <div class="filer-name">Tempo:</div>
        <div class="filter-value">{{ filters.tempo || "none" }}</div>
      </div>
      <div class="current-filter">
        <div class="filer-name">Key:</div>
        <div class="filter-value">
          {{ filters.key ? availableKeys[filters.key] : "none" }}
        </div>
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
  margin-top: 20px;
  margin-bottom: 60px;
  margin-left: 50px;
  margin-right: 50px;
  padding-bottom: 50px;
  border-bottom: 1px solid white;
}
.filter-info-header {
  display: flex;
  gap: 15px;
}
.filter-title {
  font-size: 2rem;
  margin-left: 27px;
  margin-bottom: 20px;
  font-family: "Gotham", sans-serif;
}
.current-filters-wrapper {
  margin-left: 50px;
  display: flex;
  flex-direction: column;
  gap: 10px;
}
.current-filter {
  display: flex;
  font-family: "GothamThin", sans-serif;
}
.filer-name {
  width: 10rem;
  font-family: "Gotham", sans-serif;
}
.change-button {
  font-family: "GothamBold", sans-serif;
  font-size: 1rem;
  padding: 4px 8px;
  background-color: #1db954;
  border-radius: 10px;
  border-color: white;
  color: white;
  height: 35px;
}
</style>
