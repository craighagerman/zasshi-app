
<!--
diff from Driver3 -> Driver 4
  Use script setup
-->


<template>
  <h1>{{ msg }}</h1>

  <button v-for="(tab, i) in tabs" v-bind:key="tab.name"
    v-bind:class="['tab-button', { active: currentTab.name === tab.name }]" v-on:click="changeTab(i)">
    {{ tab.name }}
  </button>

  <keep-alive>
    <component :is="currentTab.comp" @go-back="goBack"></component>
  </keep-alive>
</template>


<script setup>
name: 'LeftPane3'
import { ref } from "vue";
import Comp1 from "@/components/wip/Comp1.vue";
import Comp2 from "@/components/wip/Comp2.vue";
import Comp3 from "@/components/wip/Comp3.vue";

const msg = "LeftPane3";

const input = ref(null);
const tabs = [
  { name: "One", comp: Comp1 },
  { name: "Two", comp: Comp2 },
  { name: "Three", comp: Comp3 },
];
const emit = defineEmits(['go-back'])
var currentTab = ref(tabs[0]);

function changeTab(idx) {
  // this.currentTab = this.tabs[idx];
  this.currentTab = this.tabs[idx];
  console.log("currentTab.name " + this.currentTab.name);
}
function test(num) {
  alert(num);
}
function goBack() {
  // this.changeTab(1);
  // changeTab(1);
  // console.log("goBack to idx: " + idx);
  // this.currentTab = this.tabs[1];

  const foo = tabs[1]
  currentTab = foo;
  // alert(42)
}
</script>