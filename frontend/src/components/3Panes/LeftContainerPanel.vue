<!-- 
  Left Panel
-->

<template>
  <div id="left_panel">
    <component v-if="ui_mode === 'accordian'" :is=LeftNavAccordian></component>
    <component v-else :is=LeftPane></component>
  </div>
</template>


<script setup>
name: 'LeftContainerPanel'
import LeftNavAccordian from "@/components/3Panes/LeftNavAccordian.vue";
import LeftPane from "@/components/3Panes/LeftPane.vue";
import { useSettingsStore } from "@/stores/settingsStore";
import { storeToRefs } from 'pinia'
const settingsStore = useSettingsStore()
const { ui_mode } = storeToRefs(settingsStore);
</script>


<style>
</style>
