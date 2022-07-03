<template>
  <div class="browse-music">
    <browse-content v-if="state === 'browse'" @changeView="selectFilters" />
    <filter-selection v-if="state === 'filter'" @changeView="browse" />
  </div>
</template>

<script>
import { mapGetters } from "vuex";
import BrowseContent from "@/components/BrowseContent";
import FilterSelection from "@/components/FiltersSelection";

export default {
  name: "BrowseMusic",
  components: { FilterSelection, BrowseContent },
  data() {
    return {
      state: "browse",
    };
  },
  computed: {
    ...mapGetters({
      filterIsEmpty: "filterIsEmpty",
    }),
  },
  created() {
    if (this.filterIsEmpty) {
      this.state = "filter";
    }
  },
  methods: {
    selectFilters() {
      this.state = "filter";
    },
    browse() {
      this.state = "browse";
    },
  },
};
</script>

<style scoped>
.browse-music {
  color: white;
}
</style>
