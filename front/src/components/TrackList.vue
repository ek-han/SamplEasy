<template>
  <div class="browse-content">
    <div class="track" v-for="t in tracks" :key="t.id">
      <iframe
        style="border-radius: 12px"
        :src="`https://open.spotify.com/embed/track/${t.id}`"
        width="100%"
        height="100"
        allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture"
      />
    </div>
    <div id="embed-iframe"></div>
  </div>
</template>

<script>
export default {
  name: "TrackList",
  props: {
    tracks: {
      type: Array,
      default: () => [],
    },
  },
};
</script>

<style scoped>
.browse-content {
  display: flex;
  flex-direction: column;
  gap: 5px;
  align-items: center;
}
.track {
  width: 80%;
  display: flex;
  gap: 10px;
}
</style>
