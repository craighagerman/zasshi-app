<template>
  <ul v-if="todos.length > 0">
    <li v-for="todo in todos" :key="todo.id">
      <span :class="todo.completed ? 'completed' : ''">
        {{ todo.title }}
      </span>
      <input type="checkbox" id="checkbox" v-model="todo.completed" />
    </li>
  </ul>
</template>

<script>
export default {
  name: 'TodoList',
  props: [
    'todos'
  ]
}
</script>

<style scoped>
.completed {
  color: gray;
  text-decoration: line-through;
}

ul {
  margin-top: 2em;
  margin-left: 1em;
}

li {
  list-style: square;
}
</style>