<template>
  <div id="two">
    <h1>Two</h1>
    <ul>
      <li><div @click="openSection('news')">News</div></li>
      <!-- <div @click="feedFetcher(item.xmlUrl)"></div> -->
      <li>Sports</li>
      <li>Politics</li>
      <li>Lifestyle</li>
    </ul>
  </div>
</template>


<script setup>
import { ref } from "vue";
name: "Comp2";

const msg = ref("Hello World!");

function openSection(name) {

}

</script>


<style>
#two {
  background-color: pink;
  color: black;
  width: 250px;
  height: 300px;
}
</style>
