<template>
  <div id="app" class="d-flex flex-column min-vh-100">
    <Menubar v-if="shouldShowMenubar" />
    <div class="flex-fill d-flex flex-column">
      <router-view class="flex-fill" />
    </div>
  </div>
</template>

<script lang="ts">
import Vue from "vue";
import Menubar from "./components/Menubar.vue";
import { Route } from "vue-router";
import Component from "vue-class-component";
import { GeneralStore } from "./store";
import AppConstants from "./constants";
import Login from "./data/Login.vue";
import EDFList from "./data/EDFList.vue";
@Component({
  components: {
    Menubar,
    EDFList
  },
})
export default class App extends Vue {
  private store: GeneralStore = GeneralStore.CreateProxy(
    this.$store,
    GeneralStore
  );

  // Determine whether to show the Menubar based on the current route's meta field
  get shouldShowMenubar() {
    return (
      this.$route.meta &&
      this.$route.meta.showMenubar === true
    );
  }
}
</script>

<style>
html,
body {
  height: 100%;
}
</style>
