<template>
  <div class="navbar">
    <!-- <nav> -->
    <RouterLink to="/">Home</RouterLink>
    <RouterLink to="/about">About</RouterLink>
    <!-- </nav> -->

    <!-- <input type="text" size="50" v-model="articleStore.rssFeed">
    <p>RSS url: {{ articleStore.rssUrl }}</p>
    <p>Number of Feeds: {{ articleStore.articles.length }}</p>
    <button v-on:click="articleStore.fetchBBC">Fetch BBC</button> |
    <button v-on:click="articleStore.fetchAxios">Fetch RSS</button> |
    <button v-on:click="articleStore.clear">Clear</button> |
    <button v-on:click="articleStore.reset">Reset</button> -->
  </div>
</template>


<script setup>
import { useArticleStore } from '@/stores/articleStore'
const articleStore = useArticleStore()
</script>


<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.navbar {
  text-align: center;
  /* background-color: cadetblue; */
  padding: 10px;
  height: 120px;
  /* The code that you need to copy */
  position: absolute;
  top: 0px;
  left: 0px;
  right: 0px;
}
</style>
