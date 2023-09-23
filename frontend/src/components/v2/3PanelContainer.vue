


<template>
  <h1>3-Panel Zasshi</h1>
  <LeftPanel />
  
  <!-- <LeftPane /> -->
  <!-- <LeftP_no2 /> -->
  <!-- <LeftNavAccordian /> -->
  <FeedPane />
  <ArticlePane />
</template>



<script setup>

name: 'ThreePanelContainer'

import LeftPanel from "@/components/v2/LeftPanel.vue";
import LeftNavAccordian from "@/components/v1/LeftNavAccordian.vue";
import LeftP_no2 from "@/components/v2/LeftP_no2.vue";
import LeftPane from "@/components/v2/LeftPane.vue";
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