
<template>
  <div id="leftpane">
    <H3>Section List</H3>
    <p>Pane #2/3</p>

    <ul style="list-style-type: none">
        <li v-for="item in  feedStore.categories ">
          <div style="cursor: pointer" @click="fetch_feeds(item.id)">{{ item.name }}</div>
        </li>
    </ul>
  </div>
</template>



<script setup>
name: 'SectionList'

import { useFeedStore } from '@/stores/feedStore'
import { onBeforeMount } from "vue";
const feedStore = useFeedStore()

onBeforeMount(async () => {
  await feedStore.fetch_categories();
});


function fetch_feeds(url) {
  console.log("Fetch feeds for category id: " + url)
  feedStore.fetch_feeds(url);
}

</script>
