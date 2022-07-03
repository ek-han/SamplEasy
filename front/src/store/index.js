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
      genres: ["techno"],
      tempo: null,
      key: null,
      popularity: null,
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
    popularityType: [
      {
        name: "Not at all",
        value: 25,
      },
      {
        name: "A little popular",
        value: 50,
      },
      {
        name: "Popular",
        value: 75,
      },
      {
        name: "The best Hits",
        value: 100,
      },
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
    popularityType: (state) => state.popularityType,
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
      state.filters.tempo = payload.tempo;
      state.filters.key = payload.key;
      state.filters.genres = payload.selectedGenres;
      state.filters.popularity = payload.popularity;
    },
  },
  actions,
  modules: {},
});
