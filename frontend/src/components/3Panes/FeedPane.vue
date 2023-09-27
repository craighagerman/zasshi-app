
<template>
  <div class="scrollable" id="feedpane">
    <!-- <h1>Feed Pane xyz</h1> -->
    <h2>Channel: {{ feedStore.feed_pane_title }}</h2>
    <ul style="list-style-type: none">
      <div id="wrapper">
        <ArticleCard v-for="article in feedStore.feed_list" :key="article.id" :title="article.title"
          :published="article.published" :link="article.link" :source="article.source" :description="article.description">
        </ArticleCard>
      </div>
    </ul>
  </div>
</template>


<script setup>
name: 'FeedPane'
import ArticleCard from "@/components/3Panes/ArticleCard.vue";
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
  color: black;
  /* overflow: hidden; */
  position: absolute;
  /* border: 1px dotted gray; */
  top: 100px;
  left: 250px;
  /* right: 0; */
  bottom: 0;
  width: 550px;
  /* height: 1000px; */
  height: 100vh;
  /* height: 100%; */
}
</style>
