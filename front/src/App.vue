<template>
  <div id="app">
    <router-view />
  </div>
</template>

<script>
export default {};
</script>

<style lang="scss">
* {
  margin: 0;
  padding: 0;
}

html,
body {
  height: 100vh;
}

#app {
  position: relative;
  margin: 0;
  padding: 0;
  height: 100%;
}
</style>
