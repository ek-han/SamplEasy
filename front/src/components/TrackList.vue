<template>
  <div class="browse-content">
    <div v-for="t in recommendations" :key="r.id">
      {{ r.name }} {{ r.mainArtist }} {{ r.popularity }}
    </div>
  </div>
</template>

<script>
export default {
  name: "TrackList",
  props: {
    tracks: {
      type: Object,
      default: () => {},
    },
  },
};
</script>

<style scoped></style>
