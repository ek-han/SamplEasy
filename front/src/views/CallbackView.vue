<template>
  <div />
</template>

<script>
export default {
  name: "CallbackView",
  async mounted() {
    const token = window.location.hash.substr(1).split("&")[0].split("=")[1];
    if (token) {
      await window.opener.spotifyCallback(token);
    }
  },
};
</script>
