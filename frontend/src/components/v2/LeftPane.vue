
<template>
  <div id="leftpane">
    <h1>Left Pane</h1>
    <MyButton @increase-by="changeName" />

    <div id="dynamic-component-demo" class="demo">
      <button v-for="(tab, i) in tabs" v-bind:key="tab.name"
        v-bind:class="['tab-button', { active: currentTab.name === tab.name }]" v-on:click="currentTab = tabs[i]">
        {{ tab.name }}
      </button>
      <KeepAlive>
        <component :is="currentTab.comp"></component>
      </KeepAlive>
    </div>

  </div>
</template>



<script setup>
name: 'LeftPane'
import { shallowRef } from 'vue'
import SectionList from "@/components/v2/SectionList.vue";
import SectionFeedList from "@/components/v2/SectionFeedList.vue";
import { reactive, computed } from 'vue'

const tabs = [
  { name: 'Sections', comp: SectionList },
  { name: 'Channels', comp: SectionFeedList }
]

defineEmits(['inFocus', 'submit'])

function buttonClick() {
  emit('submit')
}

function changeName(n) {
  count.value = n
}

// using shallowRef to stop Vue from turning component definitions to reactive objects
// use normal ref to see a warning
const currentTab = shallowRef(tabs[0]);

</script>


<style>
#leftpane {
  /* background-color: cadetblue; */
  bottom: 0;
  /* color: white; */
  color: black;
  /* overflow: hidden; */
  /* position: absolute; */
  border: 1px dotted gray;
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
