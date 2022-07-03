<template>
  <div class="browse-wrapper">
    <filter-info @changeView="$emit('changeView')" />
    <track-list :track="recommendations" />
  </div>
</template>

<script>
import { mapGetters } from "vuex";
import FilterInfo from "@/components/FilterInfo";
import TrackList from "@/components/TrackList";

export default {
  name: "BrowseContent",
  components: { TrackList, FilterInfo },
  computed: {
    ...mapGetters({
      recommendations: "recommendations",
    }),
  },
  mounted() {
    this.$store.dispatch("GetRecommendations");
  },
};
</script>

<style scoped>
.browse-wrapper {
  margin-left: 10px;
}
.browse-content {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}
</style>
