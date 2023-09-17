
<template>
  <div id="leftpane_n2">
    <p>Pane #2/3</p>
    <ul style="list-style-type: none">
      <li v-for="item in  feedStore.categories ">
        <div style="cursor: pointer" @click="set_category(item.id)">{{ item.name }}</div>        
      </li>
    </ul>
  </div>
</template>


<script setup>
name: 'SectionFeedList'

import { useFeedStore } from '@/stores/feedStore'
import { defineEmits, onBeforeMount } from "vue";
const feedStore = useFeedStore()

const emit = defineEmits(['go-to-component'])

onBeforeMount(async () => {
  await feedStore.fetch_categories();
});

function set_category(cat_id) {
  // feedStore.channel_name = cat_id
  feedStore.category_name = cat_id
  feedStore.fetch_channels(cat_id);
  // feedStore.channel_name = cat_id
  console.log(`cat_id  =  ${cat_id} `)
  // console.log(`feedStore.channel_name  =  ${feedStore.channel_name} `)
  console.log(`feedStore.channel_name  =  ${feedStore.category_name} `)
  emit('go-to-component', 2)
}

</script>



<style>
#leftpane_n2 {
  /* background-color: cadetblue; */
  bottom: 0;
  /* color: white; */
  color: black;
  /* overflow: hidden; */
  /* position: absolute; */
  /* border: 1px dotted gray; */
  /* right: 0; */
  left: 0;
  /* top: 120px; */
  width: 250px;
  /* height: 1000px; */
  height: 100vh;
  /* height: 100%; */
}

ul {
  margin-left: -30px;
}

/* 
li {
  left: -30px;
  margin-left: 0px;
} */
</style>
