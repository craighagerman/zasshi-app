


<template>
  <h1>3-Panel Zasshi</h1>
  <LeftContainerPanel />
  <FeedPane />
  <ArticlePane />
</template>


<script setup>
name: 'ThreePanelContainer'
import LeftContainerPanel from "@/components/3Panes/LeftContainerPanel.vue";
import FeedPane from "@/components/3Panes/FeedPane.vue";
import ArticlePane from "@/components/3Panes/ArticlePane.vue";

const title = getTitle(this)
if (title) {
  document.title = title
}

function getTitle(vm) {
  return "Zasshi"
}
</script>


<style></style>