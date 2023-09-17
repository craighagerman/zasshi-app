


<template>
  <h1>Zasshi-v2</h1>
  <LeftPane />
  <FeedPane />
  <ArticlePane />
</template>



<script setup>

name: 'App_v2'
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