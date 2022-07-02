import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);

import * as actions from "./actions/index";

export default new Vuex.Store({
  state: {
    activeTab: "music",
    artists: [],
    genres: [],
    genreSeeds: [],
    recommendations: [],
  },
  getters: {
    artists: (state) => state.artists,
    genres: (state) => state.genres,
    genreSeeds: (state) => state.genreSeeds,
    activeTab: (state) => state.activeTab,
    recommendations: (state) => state.recommendations,
    selectedGenres: (state) =>
      state.genreSeeds.filter((gs) => gs.selected).map((gs) => gs.name),
  },
  mutations: {
    setArtistsAndGenres(state, items) {
      state.artists = items.map((i) => i.name);
      state.genres = [
        ...new Set(items.reduce((acc, i) => acc.concat(i.genres), [])),
      ];
    },
    SetGenreSeeds(state, seeds) {
      if (state.genreSeeds.length === 0) {
        state.genreSeeds = seeds.map((gs) => {
          return {
            name: gs,
            selected: false,
          };
        });
      }
    },
    changeActiveTab(state, tab) {
      state.activeTab = tab;
    },
    setRecommendations(state, data) {
      state.recommendations = data;
    },
    // toggleGenre(state, genre) {
    //   const idx = state.genreSeeds.findIndex((gs) => gs.name === genre.name);
    //   if (idx !== -1) {
    //     Vue.set(
    //       state.genreSeeds[idx],
    //       "selected",
    //       !state.genreSeeds[idx].selected
    //     );
    //   }
    // },
  },
  actions,
  modules: {},
});
