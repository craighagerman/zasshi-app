
<template>
  <!-- class="scrollable" -->
  <div class="scrollable" id="feedpane">
    <h1>Feed Pane</h1>
    <ul style="list-style-type: none">

      <div id="wrapper">
        <ArticleCard_v2 v-for="article in feedStore.feed_list" :key="article.id" :title="article.title"
          :published="article.published" :link="article.link" :source="article.source" :description="article.description">
        </ArticleCard_v2>
      </div>


    </ul>

  </div>
</template>


<script setup>
name: 'FeedPane'

import ArticleCard_v2 from "@/components/v2/ArticleCard_v2.vue";
import { useFeedStore } from '@/stores/feedStore'
import { onBeforeMount } from "vue";
const feedStore = useFeedStore()


onBeforeMount(async () => {
  await feedStore.fetch_feed_list();
});

</script>




<style>
#feedpane {
  /* background-color: pink; */
  bottom: 0;
  /* color: white; */
  color: black;
  /* overflow: hidden; */
  position: absolute;
  border: 1px dotted gray;
  /* right: 0; */
  left: 250px;
  /* top: 100px; */
  width: 550px;
  /* height: 1000px; */
  height: 100vh;
  /* height: 100%; */
}
</style>
