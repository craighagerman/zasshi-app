


<template>
  <h1>Zasshi-v2</h1>
  <!-- <LeftPane /> -->
  <LeftPane2 />
  <!-- <LeftPane3 /> -->
  
  <!-- <LPChannels /> -->
  <FeedPane />
  <ArticlePane />
</template>



<script setup>

name: 'App_v2'
import LPChannels from "@/components/wip/LPChannels.vue";
import LeftPane from "@/components/v2/LeftPane.vue";
import LeftPane2 from "@/components/v2/LeftPane2.vue";
import LeftPane3 from "@/components/v2/LeftPane3.vue";
import FeedPane from "@/components/v2/FeedPane.vue";
import ArticlePane from "@/components/v2/ArticlePane.vue";

const title = getTitle(this)
if (title) {
  document.title = title
}

function getTitle(vm) {
  return "Zasshi"
}

</script>






<style></style>