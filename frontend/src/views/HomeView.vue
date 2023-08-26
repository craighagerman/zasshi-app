<template>
  <div class="home">
    <!-- <div class="count">
      {{ storeCounter.count }}
    </div>    
    <div class="buttons">
      <button @click="storeCounter.decreaseCount">-</button>
      <button @click="storeCounter.increaseCount">+</button>
    </div>    
    <hr>
    <div>
      This counter is: {{ storeCounter.oddOrEven }}
    </div>
    <hr>
    <div>
      <h3>Edit Counter: </h3>
      <input 
        v-model="storeCounter.count"
        type="number"
      >
    </div> -->
  </div>
</template>



<script setup>
  // import { ref, computed } from 'vue'
  // import { useCounterStore } from '@/stores/counter'

  // const storeCounter = useCounterStore()

  // const count = ref(0)

  // const increaseCount = () => {
  //   count.value++
  // }

  // const decreaseCount = () => {
  //   count.value--
  // }

  // const oddOrEven = computed(() => {
  //   if (count.value % 2 === 0) return 'even'
  //   return 'odd'
  // })
</script>

<style>
  .count {
    font-size: 60px;
    margin: 20px;
  }
  .buttons button {
    font-size: 40px;
    margin: 10px;
  }
</style>

