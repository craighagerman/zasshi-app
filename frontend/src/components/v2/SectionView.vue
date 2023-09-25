
<template>
  <div id="leftpane">
    <h3>Section View</h3>

    <ul style="list-style-type: none">
      <!-- <li v-for="item in  feedStore.sections "></li> -->
      <!-- <a :href="item">{{ item }}</a> -->
      
            <li v-for="(item, index) in feedStore.sections" :key="item.id">
              <div class="feedTitleDiv" style="cursor: pointer" onmouseover="this.style.background='gray';"
                onmouseout="this.style.background='white';" @click="feedFetcher(item.xmlUrl)">
                <p class="feedTitle">{{ item.name }}</p>
              </div>
            </li>

    </ul>
  </div>
</template>



<script setup>
name: 'SectionView'

import { useFeedStore } from '@/stores/feedStore'
import { onBeforeMount } from "vue";
const feedStore = useFeedStore()

onBeforeMount(async () => {
  await feedStore.fetch_categories();
});

</script>
