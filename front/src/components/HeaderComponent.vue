<template>
  <div class="header">
    <div class="logo">LOGO</div>
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
        My Gallery
      </div>
      <div
        class="navigation-text"
        :class="{
          selected: activeTab === 'music',
        }"
        @click="navigate('music')"
      >
        Browse Music
      </div>
      <button class="button" @click="disconnect">Disconnect</button>
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
}
.logo {
  font-size: 5em;
  height: 100%;
  width: 5em;
  display: flex;
  justify-content: center;
  align-items: center;
  position: absolute;
  left: 0;
}
.navigation {
  font-size: 2.8rem;
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  position: absolute;
  right: 50px;
  gap: 2.7rem;
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
  font-size: 1rem;
  padding: 10px 20px;
  background-color: #b00505;
  border-radius: 10px;
  color: white;
}
</style>
