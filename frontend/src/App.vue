<template>
  <div id="app">
    <navigation />
    <router-view></router-view>
  </div>
</template>

<script>
import Navigation from "@/components/Navigation.vue";
export default {
  name: "App",
  components: {
    navigation: Navigation
  }
};
</script>

<style>
#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
  margin: 2em;
}
</style>
