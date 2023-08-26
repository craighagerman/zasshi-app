
<template>
  <div id="leftpane_n2">
    <ul style="list-style-type: none">
      <li v-for="item in  feedStore.categories ">
        <a :href="item">{{ item }}</a>
        <!-- TODO: Don't use a href above. Use div with @click. see SourceList -->
      </li>
    </ul>
  </div>
</template>



<script setup>
name: 'SectionFeedList'


import { useFeedStore } from '@/stores/feedStore'
import { onBeforeMount } from "vue";
const feedStore = useFeedStore()


onBeforeMount(async () => {
  await feedStore.fetch_categories();
});


</script>



<style>
#leftpane_n2 {
  background-color: cadetblue;
  bottom: 0;
  /* color: white; */
  color: black;
  /* overflow: hidden; */
  /* position: absolute; */
  border: 1px dotted gray;
  /* right: 0; */
  left: 0;
  /* top: 120px; */
  width: 250px;
  /* height: 1000px; */
  height: 100vh;
  /* height: 100%; */
}

ul {
  margin-left: -30px;
}

/* 
li {
  left: -30px;
  margin-left: 0px;
} */
</style>
