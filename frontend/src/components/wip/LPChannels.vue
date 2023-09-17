<!-- 
  Display list of channels for a given section
  - 3rd Left Pane component
-->

<template>
  <div id="leftpane">
    <h2>{{ feedStore.section_name }} Channels</h2>
    <p>Pane #3/3</p>

    <div id="dynamic-component-demo" class="demo">
      <button @click="$emit('go-to-component', 1)">Go Back</button>
      
      <ul style="list-style-type: square">
        <li v-for="item in feedStore.channels">
          <div style="cursor: pointer" 
            @click="load_feed(item)"
            onmouseover="this.style.background='lightgray';"
            onmouseout="this.style.background='white';"
          >{{ item.title }}</div>
        </li>
      </ul>
    </div>
  </div>
</template>



<script setup>
name: 'LPChannels'
import { shallowRef } from 'vue'
import { useFeedStore } from '@/stores/feedStore'
import { onBeforeMount } from "vue";
import { ref, reactive, computed, watch } from 'vue'
const feedStore = useFeedStore()

function load_feed(item) {
  feedStore.clear_feed_list()
  console.log("Loading url... " + item.xmlUrl)
  feedStore.feed_pane_title = item.title
  feedStore.fetch_feed(item.xmlUrl);
}
</script>


<style>
#leftpane {
  /* background-color: lightcyan; */
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
