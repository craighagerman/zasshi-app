<!-- LeftNavBar.vue (was LeftFeedList.vue) -->

<template id="LeftNavBar">
    <div id="left-sidebar">
        <h1>{{ msg }}</h1>
        <ul style="list-style-type: none">
            <li v-for="item in  rssStore.feedUrls ">
                <!-- <a class="rsslink" :href="item">{{ item }}</a> -->
                <!-- <div class="feedTitleDiv" style="cursor:pointer;" @mouseover="showMe" @mouseout="hideMe" @click="feedFetcher(item.xmlUrl)"></div> -->

                <!-- <div class="feedTitleDiv" style="cursor:pointer;" onmouseover="this.style.background='gray';"
                    onmouseout="this.style.background='cadetblue';" @click="feedFetcher(item.xmlUrl)">
                    <p class="feedTitle">{{ item.category }}</p>
                </div> -->


                <SourceList v-bind:category=item.category v-bind:items="item.items" />

            </li>
        </ul>
    </div>
</template>



<script setup>
import { useRssStore } from '@/stores/rssStore'
import { onBeforeMount } from "vue";
import { useArticleStore } from '@/stores/articleStore'
import SourceList from "@/components/v1/SourceList.vue";
const rssStore = useRssStore()
const articleStore = useArticleStore()
const msg = ''

onBeforeMount(async () => {
    await rssStore.fetch_feed_list();
});


function feedFetcher(url) {
    articleStore.fetchAxiosUrl(url);
}

</script>


<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
#left-sidebar {
    background-color: cadetblue;
    bottom: 0;
    color: white;
    /* overflow: hidden; */
    position: absolute;

    /* right: 0; */
    left: 0;
    top: 120px;
    width: 300px;
    /* height: 1000px; */
    height: 100vh;
    /* height: 100%; */
}


html,
body {
    height: 100%;
}

.rsslink {
    color: white
}

.feedTitleDiv {
    padding: 2px;
}

.feedTitle {
    /* color: orange; */
    font-size: 14px;
}
</style>

