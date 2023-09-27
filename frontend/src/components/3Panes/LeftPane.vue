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
  <div id="navigationStack">
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
import SectionList from "@/components/3Panes/SectionList.vue";
import SectionFeedList from "@/components/3Panes/SectionFeedList.vue";
import ChannelView from "@/components/3Panes/ChannelView.vue";

export default {
  setup() {
    const section_list = shallowRef(SectionList)
    const section_feed_list = shallowRef(SectionFeedList)
    const channel_view = shallowRef(ChannelView)

    const tabs = [
      { name: 'Sections', comp: section_list },
      { name: 'Inspect', comp: section_feed_list },
      { name: 'Channels', comp: channel_view },
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
#navigationStack {
  /* background-color: lightcyan; */

  /* color: white; */
  color: black;
  /* overflow: hidden; */
  /* position: absolute; */
  /* border: 1px dotted gray; */
  /* top: 120px; */
  left: 0;
  /* right: 0; */
  bottom: 0;
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
