<template>
  <div id="one">
    <h1>One</h1>
    <ul>
      <li>News</li>
      <li>Sports</li>
      <li>Politics</li>
      <li>Lifestyle</li>
    </ul>
  </div>
</template>


<script setup>
import { ref } from "vue";
name: "Comp1";

const msg = ref("Hello World!");
</script>



<style>
#one {
  background-color: cadetblue;
  color: white;
  width: 250px;
  height: 300px;
}
</style>
