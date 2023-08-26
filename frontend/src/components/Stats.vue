<template>
  <span>{{ label }} ({{ value }})</span>
</template>

<script>
export default {
  name: 'Stats',
  props: [
    'label',
    'value'
  ]
}
</script>

<style scoped>
span {
  margin-right: 1em;
}
</style>