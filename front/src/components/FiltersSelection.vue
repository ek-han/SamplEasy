<template>
  <div class="filter-selection">
    <div class="filer-title">Filter Your Music!</div>
    <div class="filter-wrapper">
      <div class="tempo-wrapper">
        <div class="tempo-text">Tempo</div>
        <input type="number" v-model="tempo" />
      </div>
      <div class="key-wrapper">
        <div class="key-text">Key</div>
        <div class="genre-input-wrapper left">
          <div
            v-for="(k, i) in availableKeys"
            :key="i"
            class="genre-input"
            :class="{ selected: key === i }"
            @click="key = i"
          >
            {{ k }}
          </div>
        </div>
      </div>
      <div class="popularity-wrapper">
        <div class="popularity-title">Popularity</div>
        <div
          v-for="(k, i) in popularityType"
          :key="i"
          class="genre-input"
          :class="{ selected: popularity && popularity.value === k.value }"
          @click="popularity = k"
        >
          {{ k.name }}
        </div>
      </div>
      <div class="genre-wrapper">
        <div class="genre-text">
          You can select up to 5 genres ({{ selectedGenres.length }}/5)
        </div>
        <div class="genre-input-wrapper">
          <div
            v-for="(gs, i) in genreSeeds"
            :key="i"
            class="genre-input"
            :class="{ selected: selectedGenres.includes(gs) }"
            @click="toggleGenre(gs)"
          >
            {{ gs }}
          </div>
        </div>
      </div>
    </div>
    <div class="button-wrapper">
      <button class="button" :disabled="filterIsEmpty" @click="saveAndBrowse">
        Filter
      </button>
    </div>
  </div>
</template>

<script>
import { mapGetters } from "vuex";

export default {
  name: "FilterSelection",
  data() {
    return {
      tempo: null,
      key: null,
      selectedGenres: [],
      popularity: null,
    };
  },
  computed: {
    ...mapGetters({
      genreSeeds: "genreSeeds",
      availableKeys: "availableKeys",
      popularityType: "popularityType",
    }),
    filterIsEmpty() {
      return (
        this.tempo === null &&
        this.key === null &&
        this.selectedGenres.length === 0
      );
    },
  },
  created() {
    this.$store.dispatch("loadGenreSeeds");
  },
  methods: {
    toggleGenre(genre) {
      if (this.maxGenreSelected(genre)) return;
      const idx = this.selectedGenres.findIndex((gs) => gs === genre);
      if (idx === -1) {
        this.selectedGenres.push(genre);
      } else {
        this.selectedGenres.splice(idx, 1);
      }
    },
    maxGenreSelected(genre) {
      return (
        this.selectedGenres.length >= 5 && !this.selectedGenres.includes(genre)
      );
    },
    saveAndBrowse() {
      this.$store.commit("saveFilters", {
        tempo: this.tempo,
        key: this.key,
        selectedGenres: this.selectedGenres,
        popularity: this.popularity,
      });
      this.$emit("changeView");
    },
  },
};
</script>

<style lang="scss" scoped>
.filter-selection {
  font-size: 1.5rem;
  margin: 10px;
}
.filer-title {
  font-size: 3rem;
  display: flex;
  justify-content: center;
  text-decoration: underline;
}
.filter-wrapper {
  display: flex;
  flex-direction: column;
  gap: 20px;
}
.popularity-wrapper {
  display: flex;
  gap: 10px;
}
.tempo-wrapper {
  display: flex;
  gap: 10px;
}
.key-text {
  display: flex;
  align-items: center;
}
.genre-input-wrapper {
  position: relative;
  width: 100%;
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  padding: 15px;
  gap: 5px;

  &.left {
    justify-content: start;
  }
}
.genre-input {
  font-size: 1.5rem;
  border: 1px solid gray;
  padding: 5px;
  border-radius: 5px;

  &:hover {
    background-color: #162d57;
  }

  &.selected {
    background-color: #162d57;
  }
}
.button-wrapper {
  display: flex;
  justify-content: center;
  margin-top: 50px;
}
.button {
  font-size: 3rem;
  padding: 10px 30px;
  background-color: #03a9f1;
  border-radius: 10px;
  color: white;
}
</style>
