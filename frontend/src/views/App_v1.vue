
<template>
  <!-- <TopNavBar msg="Top Sidebar" /> -->
  <LeftNavBar msg="Left Sidebar" />
  <ArticleList msg="RSS News Feeds" />
</template>



<script setup>

name: 'App_v1'

import LeftNavBar from "@/components/v1/LeftNavBar.vue";
import ArticleList from "@/components/v1/ArticleList.vue";
import TopNavBar from "@/components/v1/TopNavBar.vue";

const title = getTitle(this)
if (title) {
  document.title = title
}

function getTitle(vm) {
  return "Zasshi"
}

</script>




<style scoped>
html,
body {
  height: 100%;
}

.app {
  text-align: center;
  background-color: rgb(206, 223, 118);
  /* The code that you need to copy */
  position: absolute;
  top: 0px;
  left: 0px;
  right: 0px;

  width: 600px;
}

/* .mainbody {
  text-align: center;
  position: absolute;
  top: 200px;
  left: 0px;
  right: 0px;
} */

#rsssetup {
  background-color: cadetblue;
  color: white;
  padding: 10px;
}

/* #wrapper {
  text-align: left;
} */
</style>
