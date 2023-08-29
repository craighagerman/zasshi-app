
<template>
  <div id="leftpane">
    <H3>Sections</H3>

    <ul style="list-style-type: none">
      <li v-for="item in  feedStore.categories "></li>
      <a :href="item">{{ item }}</a>
      <!-- TODO: Don't use a href above. Use div with @click. see SourceList -->
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

</script>
