<!-- LeftNavAccordian (was LeftNavBar.vue ... was LeftFeedList.vue) -->

<template id="LeftNavAccordian">
    <div id="accordian-sidebar">
        <p id="dev_label">Accordian</p>
        <ul style="list-style-type: none">
            <li v-for="item in  feedStore.section_channels ">
                <AccordianChannels v-bind:category=item.category v-bind:items="item.items" />
            </li>
        </ul>
    </div>
</template>



<script setup>
import AccordianChannels from "@/components/3Panes/AccordianChannels.vue";
import { onBeforeMount } from "vue";
import { useFeedStore } from '@/stores/feedStore'
const feedStore = useFeedStore()

onBeforeMount(async () => {
    await feedStore.fetch_section_channels();
});
</script>


<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.rsslink {
    color: white
}

#dev_label {
    color: orange
}

</style>

