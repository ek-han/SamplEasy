<template>
  <div class="browse-content">
    <div class="track" v-for="t in tracks" :key="t.id">
      <img :src="t.img" :alt="t.album" />
      <div class="name-and-artist">
        <div class="name">{{ t.name }}</div>
        <div class="artist">{{ t.mainArtist }}</div>
      </div>
      <button class="uri" :data-spotify-id="t.uri" />
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
  mounted() {
    let externalScript = document.createElement("script");
    externalScript.setAttribute(
      "src",
      "https://open.spotify.com/embed-podcast/iframe-api/v1"
    );
    document.head.appendChild(externalScript);
  },
  watch: {
    tracks() {
      window.onSpotifyIframeApiReady = (IFrameAPI) => {
        let element = document.getElementById("embed-iframe");
        let options = {
          width: "60%",
          height: "200",
          uri: "spotify:episode:7makk4oTQel546B0PZlDM5",
        };
        console.log("API:", IFrameAPI);
        console.log("element:", element);
        console.log("options:", options);
        let callback = (EmbedController) => {
          document.querySelectorAll(".uri").forEach((episode) => {
            episode.addEventListener("click", () => {
              EmbedController.loadUri(episode.dataset.spotifyId);
            });
          });
        };
        console.log("callback:", callback);
        IFrameAPI.createController(element, options, callback);
      };
    },
  },
  created() {
    console.log("Tracks:", this.tracks);
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
  background: #121212;
  padding: 15px;
  border-radius: 5px;
}
.name-and-artist {
  display: flex;
  flex-direction: column;
  gap: 10px;
}
.name {
  font-weight: 600;
  font-size: 1.3rem;
}
.uri {
  width: 64px;
  height: 64px;
}
</style>
