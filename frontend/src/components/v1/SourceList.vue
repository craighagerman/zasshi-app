<!-- SourceList.vue -->

<template id="SourceList">
  <div class="accordianContainer" v-on:click="toggle()" style="cursor: pointer">
    <h2>{{ category }}</h2>
    <!-- <input type="button" value="Toggle Collapse" v-on:click="toggleButton()" /> -->

    <div  v-show="showSection">
      <ul class="accordianList">
        <li v-for="(item, index) in items" :key="item.id">
          <div class="feedTitleDiv" 
            style="cursor: pointer" 
            onmouseover="this.style.background='gray';"
            onmouseout="this.style.background='white';" 
            @click="feedFetcher(item.xmlUrl)">
            <p class="accordianChannelName">{{ item.title }}</p>
          </div>
        </li>
      </ul>
    </div>
  </div>
</template>



<script setup>
import { ref } from "vue";
import { useFeedStore } from '@/stores/feedStore'
const feedStore = useFeedStore()
let showSection = ref(true);

const props = defineProps({
  category: String,
  items: [],
});

function toggle() {
  this.showSection = !this.showSection;
  console.log(this.showSection)
}

function toggleButton() {
  this.showSection = !this.showSection;
  console.log(this.showSection)
}


function feedFetcher(url) {
  feedStore.fetch_feed(url)
}
</script>




<style scoped>

#accordianContainer {
    background-color: blue;
    bottom: 0;
    color: white;
    /* overflow: hidden; */
    position: absolute;

    /* right: 0; */
    left: 0;
    top: 120px;
    width: 300px;
    /* height: 1000px; */
    height: 100vh;
    /* height: 100%; */
}


.accordianList {
  /* list-style: none; */
  /* style="list-style-type: none" */
  list-style-position: outside;
  padding-left: 1em;
}


li{
  margin: -10px 10px;
}

.feedTitleDiv {
    /* padding: 2px; */
    width: 250px;
}

.accordianChannelName {
    /* color: orange; */
    font-size: 14px;
}

#toggle {
  display: block;
}
</style>
