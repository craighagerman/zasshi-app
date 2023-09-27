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
import LeftNavAccordian from "@/components/v2/LeftNavAccordian.vue";
import LeftPane from "@/components/v2/LeftPane.vue";
import { useSettingsStore } from "@/stores/settingsStore";
import { storeToRefs } from 'pinia'
const settingsStore = useSettingsStore()
const { ui_mode } = storeToRefs(settingsStore);
</script>


<style>
</style>
