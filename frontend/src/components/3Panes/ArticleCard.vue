
<template id="ArticleCard">
  <!-- <a class="block-link" :href="link" target="_blank"> -->


  <div class="card" style="cursor: pointer" @click="fetchArticle(link)">
    <div class="container">
      <h3>{{ title }}</h3>
      <p class="cardMeta">{{ source }} | {{ published }}</p>
      <p class="description">{{ description }}</p>
      <!-- <test v-on:click.native="testFunction"></test> -->
    </div>
  </div>
  <!-- </a> -->
</template>



<script setup>
name: 'ArticleCard'

import { useFeedStore } from '@/stores/feedStore'
const feedStore = useFeedStore()

const props = defineProps({
  title: String,
  published: String,
  source: String,
  description: String,
  link: String
})


function fetchArticle(url) {
  feedStore.fetch_article(url);
}
</script>



<style scoped>
h3 {
  background-color: cadetblue;
}

.block-link {
  display: block;
  margin-left: 0px;
  /* margin-left: auto; */
  /* margin-right: auto; */
  color: black;
}

.card {
  /* Add shadows to create the "card" effect */
  /* margin: 25px 25px 25px 25px; */
  margin: 5px 0px 5px 0px;
  box-shadow: 0 4px 4px 0 rgba(0, 0, 0, 0.2);
  transition: 0.3s;
  width: 500px;
  text-align: left;
}

.description {
  font-size: small;
  padding: 0px;
}

.cardMeta {
  /* font-weight: lighter; */
  color: cadetblue;
  padding: 0px;
}

/* On mouse-over, add a deeper shadow */
.card:hover {
  box-shadow: 0 8px 16px 0 rgba(0, 0, 0, 0.2);
}

/* Add some padding inside the card container */
.container {
  padding: 2px 16px;
}

/* Add rounded corners to the top left and the top right corner of the image */
img {
  border-radius: 5px 5px 0 0;
  height: 200px;
  width: 50px;
}
</style>