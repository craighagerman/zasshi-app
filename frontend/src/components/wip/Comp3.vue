<template>
  <div id="three">
    <h1>Three - B</h1>
    <!-- <button @click="$emit('call-test')">Click Me</button> -->
    <!-- <button @click="message">Click Me Again</button> -->
    <button @click="$emit('go-back')">Go Back</button>
    <button @click="$emit('call-test', 42)">Click Me</button>
    <ul>
      <li>News</li>
      <li>Sports</li>
      <li>Politics</li>
      <li>Lifestyle</li>
    </ul>
  </div>
</template>


<script>
import { ref } from "vue";
import { defineComponent } from "vue";
export default defineComponent({
  name: "Comp3",
  methods: {
    message() {
      this.$emit("call-test"); // 'this' is needed.
    },
  },
});
</script>


<style>
#three {
  background-color: palegreen;
  color: black;
  width: 250px;
  height: 300px;
}
</style>
