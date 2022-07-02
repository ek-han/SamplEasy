import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);

import * as actions from "./actions/index";

export default new Vuex.Store({
  state: {
    artists: [],
    genres: [],
    genreSeeds: [],
  },
  getters: {
    artists: (state) => state.artists,
    genres: (state) => state.genres,
    genreSeeds: (state) => state.genreSeeds,
  },
  mutations: {
    setArtistsAndGenres(state, items) {
      state.artists = items.map((i) => i.name);
      state.genres = [
        ...new Set(items.reduce((acc, i) => acc.concat(i.genres), [])),
      ];
    },
    SetGenreSeeds(state, seeds) {
      state.genreSeeds = seeds;
    },
  },
  actions,
  modules: {},
});
