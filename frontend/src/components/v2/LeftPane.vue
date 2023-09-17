<!-- 
  Left Pane in a 3-panel UI
  - container to be populated by one of (in order)
    1. SectionList
    2. SectionFeedList
    3. LPChannels
  - n.b behavior of switching between these three components is a combination of 
    a toggle-able replacement view and a navigation stack
-->

<template>
  <div id="leftpane">
    <h1>Left Pane</h1>
    <div id="dynamic-component-demo" class="demo">
    <button
      v-for="(tab, i) in tabs.slice(0,2)"
      v-bind:key="tab.name"
      v-bind:class="['tab-button', { active: currentTab.name === tab.name }]"
      v-on:click="changeTab(i)"
    >
      {{ tab.name }}
    </button>
      <KeepAlive>
        <component :is="currentTab.comp" @go-to-component="goToComponent"></component>
      </KeepAlive>
    </div>
  </div>
</template>


<script>
import { ref, shallowRef, reactive, computed, watch } from 'vue'
import SectionList from "@/components/v2/SectionList.vue";
import SectionFeedList from "@/components/v2/SectionFeedList.vue";
import LPChannels from "@/components/wip/LPChannels.vue";

export default {
  setup() {

    const tabs = [
      { name: 'Sections', comp: SectionList },
      { name: 'Drilldown', comp: SectionFeedList },
      { name: 'Channels', comp: LPChannels },
    ];
    var currentTab = ref(tabs[0]);
    return {
      tabs,
      currentTab,
    };
  },

  // Methods are functions that mutate state and trigger updates.
  // They can be bound as event handlers in templates.
  methods: {
    changeTab(idx) {
      this.currentTab = this.tabs[idx];
      console.log("currentTab.name " + this.currentTab.name);
    },
    goBack() {
      this.changeTab(0);
    },
    goToComponent(idx) {
      this.changeTab(idx);
    },
  },
};
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
