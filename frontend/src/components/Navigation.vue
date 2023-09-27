<template>
  <div class="navbar">
    <ul>
      <li>
        <router-link to="/">Home</router-link>
      </li>
      <li>
        <router-link to="/about">About</router-link>
      </li>
      <li>
        <router-link to="/todos">Todos</router-link>
      </li>
      <!-- <li>
        <router-link to="/v1">Zasshi-v1</router-link>
      </li> -->
      <li>
        <router-link to="/v2">Zasshi-v2</router-link>
      </li>
      <li>
        <router-link to="/settings">Settings</router-link>
      </li>
      <li><h2>Zasshi</h2></li>
    </ul>
  </div>
</template>

<script setup>
name: 'Navigation'
import { onBeforeMount } from "vue";

// onBeforeMount(async () => {
  // console.log('window.innerWidth: ' + window.innerWidth)
// });

// window.innerHeight
</script>

<style scoped>
ul {
  margin: 0;
  padding: 0;
}

li {
  display: inline-block;
  padding: 1em 0.5em;
}

.navbar {
  /* white-space : nowrap;  */
  /* overflow : hidden;  */
  border: 1px dotted gray;
  /* display: inline-block; */


  /* background-color: lightgrey; */
  /* padding: 10px; */
  /* height: 120px; */
  /* The code that you need to copy */
  /* position: absolute; */
  top: 0px;
  left: 0px;
  right: 0px;
}
</style>