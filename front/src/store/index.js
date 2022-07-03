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
    filters: {
      genres: [],
      tempo: null,
      key: null,
    },
    availableKeys: [
      "C",
      "C#",
      "D",
      "D#",
      "E",
      "F",
      "F#",
      "G",
      "G#",
      "A",
      "A#",
      "B",
    ],
  },
  getters: {
    artists: (state) => state.artists,
    genres: (state) => state.genres,
    genreSeeds: (state) => state.genreSeeds,
    activeTab: (state) => state.activeTab,
    filters: (state) => state.filters,
    recommendations: (state) => state.recommendations,
    availableKeys: (state) => state.availableKeys,
    selectedGenres: (state) =>
      state.genreSeeds.filter((gs) => gs.selected).map((gs) => gs.name),
    filterIsEmpty: (state) =>
      state.filters.genres.length === 0 &&
      state.filters.tempo === null &&
      state.filters.key === null,
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
    changeActiveTab(state, tab) {
      state.activeTab = tab;
    },
    setRecommendations(state, data) {
      state.recommendations = data;
    },
    saveFilters(state, payload) {
      console.log("P:", payload);
      state.filters.tempo = payload.tempo;
      state.filters.key = payload.key;
      state.filters.genres = payload.selectedGenres;
    },
  },
  actions,
  modules: {},
});
