<!-- 
  Left Panel
-->

<template>
  <div id="left_panel">
  <h2>Left Container Panel</h2>
    <!-- <LeftNavAccordian /> -->

    <component :is=LeftNavAccordian></component>
  
    <!-- <KeepAlive>
      <component :is="currentTab.comp"></component>
    </KeepAlive> -->
  </div>
</template>



<script setup>
name: 'LeftPanel'
import LeftNavAccordian from "@/components/v1/LeftNavAccordian.vue";

// <script>
// import { ref, shallowRef, reactive, computed, watch } from 'vue'
// import { useSettingsStore } from "@/stores/settingsStore";
// import { onBeforeMount } from "vue";
// import LeftNavAccordian from "@/components/v1/LeftNavAccordian.vue";
// import LeftPane from "@/components/v2/LeftPane.vue";

// import LeftP_no2 from "@/components/v2/LeftP_no2.vue";
// import LeftNavBar from "@/components/v1/LeftNavBar.vue";


// export default {
//   setup() {
//     const settingsStore = useSettingsStore()


//     const tabs = [
//       { name: 'LeftPane', comp: LeftPane },
//       { name: 'LeftNavAccordian', comp: LeftP_no2 },
//     ];

//     var currentTab = ref(tabs[1]);

//     onBeforeMount(() => {
//       // const settingsStore = useSettingsStore()
//       const ui_mode = settingsStore.ui_mode
//       console.log("ui mode: " + ui_mode)
//       if (ui_mode == "navigationStack") {
//         currentTab = tabs[0]
//       } else if (ui_mode == "accordion") {
//         currentTab = tabs[1]
//       } else {
//         // just go with default behavior
//         currentTab = tabs[0]
//       }
//       console.log("current Component = " + currentTab.name)
//     });

//     return {
//       tabs,
//       currentTab,
//     };
//   },
  
//   data() {
//     return { settingsStore: useSettingsStore() }
//   },
// };


</script>



<style>
</style>
