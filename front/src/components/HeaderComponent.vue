<template>
  <div class="header">
    <div class="logo">SamplEasy</div>
    <div class="navigation">
      <div
        class="navigation-text"
        :class="{
          selected: activeTab === 'chat',
        }"
        @click="navigate('chat')"
      >
        Chat
      </div>
      <div
        class="navigation-text"
        :class="{
          selected: activeTab === 'gallery',
        }"
        @click="navigate('gallery')"
      >
        Favorites
      </div>
      <div
        class="navigation-text"
        :class="{
          selected: activeTab === 'music',
        }"
        @click="navigate('music')"
      >
        Browse
      </div>
      <button class="button" @click="disconnect">SIGN OUT</button>
    </div>
  </div>
</template>

<script>
import { mapGetters } from "vuex";
import storageService from "@/helpers/storage";

export default {
  name: "HeaderComponent",
  computed: {
    ...mapGetters({
      activeTab: "activeTab",
    }),
  },
  methods: {
    navigate(tab) {
      if (this.activeTab !== tab) this.$store.commit("changeActiveTab", tab);
    },
    disconnect() {
      storageService.removeValue("token");
      this.$router.push({ name: "login" });
    },
  },
};
</script>

<style lang="scss" scoped>
.header {
  width: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  position: relative;
  height: 7em;
  left: 0;
  top: 0;
  filter: drop-shadow(0px 6px 6px rgba(0, 83, 125, 0.1));
  font-family: "Gotham", sans-serif;
}
.logo {
  font-size: 4em;
  font-weight: 550;
  height: 100%;
  width: 5em;
  display: flex;
  justify-content: center;
  align-items: center;
  position: absolute;
  left: 50px;
  color: white;
}
.navigation {
  font-size: 2.15rem;
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  position: absolute;
  right: 50px;
  gap: 7rem;
}
.navigation-text {
  color: white;

  &.selected {
    border-bottom: 4px solid white;
  }

  &:hover:not(.selected) {
    transform: translateY(-10px);
    transition: all 0.3s ease;
  }
}
.button {
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
