<template>
  <div class="todos">
    <h1>Todos</h1>
    <stats :value="total" label="Total"></stats>
    <stats :value="completed" label="Completed"></stats>
    <stats :value="pending" label="Pending"></stats>
    <todo-list :todos="todos"></todo-list>
  </div>
</template>

<script>
import Stats from '@/components/Stats.vue';
import TodoList from '@/components/TodoList.vue';

export default {
  name: 'Home',
  components: {
    'todo-list': TodoList,
    'stats': Stats
  },
  data() {
    return {
      limit: 20,
      todos: []
    }
  },
  computed: {
    total: function () {
      return this.todos.length;
    },
    completed: function () {
      return this.todos.filter(function (todo) {
        return todo.completed == true;
      }).length;
    },
    pending: function () {
      return this.todos.filter(function (todo) {
        return todo.completed == false;
      }).length;
    }
  },
  created: function () {
    this.getTodos();
  },
  methods: {
    getTodos: function () {
      var self = this;

      fetch('https://jsonplaceholder.typicode.com/todos?_limit=' + this.limit)
        .then(function (response) {
          return response.json();
        })
        .then(function (data) {
          self.todos = data;
        });
    }
  }
}
</script>