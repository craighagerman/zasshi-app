<!-- SourceList.vue (was FeedList.vue) -->

<template id="SourceList">
  <div class="section" v-on:click="toggle()" style="cursor: pointer" onmouseover="this.style.background='gray';"
    onmouseout="this.style.background='cadetblue';">
    <h2>{{ category }}</h2>
    <!-- <input type="button" value="Toggle Collapse" v-on:click="toggle()" /> -->

    <div class="container" v-show="showSection">
      <ul class="srcList">
        <li v-for="(item, index) in items" :key="item.id">
          <div class="feedTitleDiv" style="cursor: pointer" onmouseover="this.style.background='gray';"
            onmouseout="this.style.background='cadetblue';" @click="feedFetcher(item.xmlUrl)">
            <p class="feedTitle">{{ item.title }}</p>
          </div>
        </li>
      </ul>
    </div>
  </div>
</template>



<script setup>
import { ref } from "vue";
import { useArticleStore } from "@/stores/articleStore";
const articleStore = useArticleStore();

let showSection = ref(true);

const props = defineProps({
  category: String,
  items: [],
});

function feedFetcher(url) {
  articleStore.fetchAxiosUrl(url);
}

function toggle() {
  // this.showSection = !this.showSection;
  console.log(this.showSection)
}
</script>

<style scoped>
.srcList {
  /* list-style: none; */
  /* style="list-style-type: none" */
  list-style-position: outside;

  padding-left: 1em;
}

#toggle {
  display: block;
}
</style>
