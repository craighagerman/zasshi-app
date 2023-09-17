

<template>
  <div class="scrollable" id="articlepane">
    <h1>Article Pane</h1>
    <div v-html="feedStore.article" />
  </div>
</template>


<script setup>
name: 'ArticlePane'

import { useFeedStore } from '@/stores/feedStore'
// import { onBeforeMount } from "vue";
import { watch } from 'vue'
import { storeToRefs } from 'pinia'
const feedStore = useFeedStore()

const article = storeToRefs(feedStore);


// Note: In general, you can watch values inside composables.
// But, to watch a pinia state it has to be inside an arrow function
// It's like watching a reactive object.
// You can also watch a property inside a store using setup() way of describing a store.
watch(() => article, (n) => {
  console.log(n, " value changed")
});




function span(text) {
  return `<span> ${text} </span>`
}

</script>


<style>
#articlepane {
  /* background-color: lightblue; */
  padding: 10px;
  bottom: 0;
  color: black;
  position: absolute;
  /* border: 1px dotted gray; */
  /* left: 800px; */
  margin-left: 800px;
  /* width: 100%; */

  /* width: window.innerHeight; */
  height: 100vh;
}

h1 {
  font-weight: bold;
}

h3 {
  font-weight: bold;
}

p {
  font-size: 1.2em;
  padding: 10px;
}


img.resize {
  padding: 10px;
  width: 800px;
  /* height: 40px; */
}
</style>
