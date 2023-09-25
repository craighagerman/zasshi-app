


<template>
  <h1>3-Panel Zasshi</h1>
  <LeftContainerPanel />
  <FeedPane />
  <ArticlePane />
</template>


<script setup>
name: 'ThreePanelContainer'
import LeftContainerPanel from "@/components/v2/LeftContainerPanel.vue";
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