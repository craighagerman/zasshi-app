
<template id="ArticleList">
  <div class="mainbody">
    <h1>{{ msg }}</h1>

    <div id="wrapper">
      <ArticleCard v-for="article in articleStore.articles" :key="article.id" :title="article.title"
        :published="article.published" :link="article.link" :source="article.source" :description="article.description">
      </ArticleCard>
    </div>

  </div>
</template>


<script setup>
import ArticleCard from "@/components/v1/ArticleCard.vue";
import { useArticleStore } from '@/stores/articleStore'
const articleStore = useArticleStore()
const msg = ''

</script>


<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
#wrapper {
  display: block;
}

.mainbody {
  /* background-color: grey; */
  /* text-align: left; */
  position: absolute;
  margin: auto;
  top: 120px;
  left: 300px;
  /* width: 300px; */

  /* width: 40%; */
  /* left: 160px; */
  /* right: 0px;  */
}
</style>
