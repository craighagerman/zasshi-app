<!-- 
  Left Panel
-->

<template>
  <div id="left_panel">
    <h3>- Settings -</h3>
    <label><input type="radio" v-model="ui_mode" value="accordian" /> accordian </label>
    <label><input type="radio" v-model="ui_mode" value="navigationStack" /> navigationStack </label>
    <br>
    <div>Mode: {{ settingsStore.ui_mode }}</div>

    <!-- <input type="button" value="save" v-on:click="save()" /> -->
  </div>
</template>



<script setup>
name: 'SettingsView'
import { useSettingsStore } from "@/stores/settingsStore";
import { storeToRefs } from 'pinia'
const settingsStore = useSettingsStore()
import { ref } from "vue"
const color = ref("white")
const { ui_mode } = storeToRefs(settingsStore);

function save() {
  settingsStore.ui_mode = ui_mode
}
</script>



<style></style>
