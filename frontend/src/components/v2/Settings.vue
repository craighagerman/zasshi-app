<!-- 
  Left Panel
-->

<template>
  <div id="left_panel">

    <h1>Hello World! </h1>
    <h3>- Settings -</h3>

    <!-- <ul> -->
      <!-- <li v-for="item in ui_modes" :key="item.id"> -->
        <!-- <p class="modeName">{{ mode }}</p> -->
        <!-- <input type="radio" :model="mode" >{{ item.name }} -->
      <!-- </li> -->
    <!-- </ul> -->

    <!-- <label><input type="radio" v-model="color" value="white" />White </label> -->
    <!-- <label><input type="radio" v-model="color" value="red" /> Red </label> -->
    <!-- <label><input type="radio" v-model="color" value="blue" /> Blue </label> -->
    <label><input type="radio" v-model="ui_mode" value="accordian" /> accordian </label>
    <label><input type="radio" v-model="ui_mode" value="navigationStack" /> navigationStack </label>
    <br>
    <div>Mode: {{ settingsStore.ui_mode }}</div>

    <input type="button" value="save" v-on:click="save()" />

  </div>
</template>



<script setup>
name: 'Settings'

import { useSettingsStore } from "@/stores/settingsStore";
import { storeToRefs } from 'pinia'
const settingsStore = useSettingsStore()
import { ref } from "vue"

const color = ref("white")
// const the_mode = ref("accordian")

const { ui_mode } = storeToRefs(settingsStore);


function save() {
  settingsStore.ui_mode = ui_mode
  console.log("NEW ui_mode = " + settingsStore.ui_mode);
}



// const selectedMode = ref([]);

// const ui_modes = [
//   {"id": 0, "name": "accordian" },
//   {"id": 1, "name": "navigationStack" }, 
// ]

// const gender = computed(() => settingsStore.currentMode)

// const mode = settingsStore.currentMode

// const onSubmit = () => {}


// onBeforeMount(async () => {
//   const mode = settingsStore.ui_mode
//   console.log("BEFORE: ui_mode= " + mode);
//   var idx = 0
//   if (mode === "accordion") {
//     console.log("YES! ui_mode IS " + mode);
//     idx = 0
//   } else {
//     idx = 1
//   }
//   console.log("idx: " + idx)
//   currentTab = tabs[idx]
// });

// function setMode() {
//   const mode = settingsStore.ui_mode
//   console.log("ui_mode= " + mode);
//   var comp = LeftPane
//   if (mode == "accordian") {
//     console.log("YES! ui_mode IS " + mode);
//     comp = LeftNavAccordian;
//   } else {
//     comp = LeftPane;
//   }
//   return comp
// }
</script>



<style></style>
