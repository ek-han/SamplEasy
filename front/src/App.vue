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
  box-sizing: border-box;
}

@font-face {
  font-family: "Gotham";
  src: local("Gotham-Font"),
    url(./fonts/Gotham-Font/GothamMedium.ttf) format("truetype");
}

@font-face {
  font-family: "GothamLight";
  src: local("Gotham-Font"),
    url(./fonts/Gotham-Font/GothamLight.ttf) format("truetype");
}

@font-face {
  font-family: "GothamThin";
  src: local("Gotham-Font"),
    url(./fonts/Gotham-Font/Gotham-Thin.otf) format("opentype");
}

@font-face {
  font-family: "GothamBold";
  src: local("Gotham-Font"),
    url(./fonts/Gotham-Font/GothamBold.ttf) format("truetype");
}

body {
  height: 100vh;
  background-color: #212121;
}

#app {
  position: relative;
  margin: 0;
  padding: 0;
  height: 100%;
}
</style>
