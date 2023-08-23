<template>
    <div class="todo-list">
      <h2 class="title">Todos</h2>
      <router-link class="link" to="/create">Create New Todo</router-link>
      <ul class="todos-list">
        <TodoItem
          v-for="todo in todos"
          :key="todo.id"
          :todo="todo"
          @todo-deleted="handleTodoDeleted"
        />
      </ul>
    </div>
  </template>
  
  <script>
  import { ref } from 'vue';
  import { getTodos } from '../todos';
  import TodoItem from './TodoItem.vue';
  
  export default {
    components: {
      TodoItem
    },
    setup() {
      const todos = ref(getTodos());
  
      const handleTodoDeleted = (deletedTodoId) => {
        todos.value = todos.value.filter((todo) => todo.id !== deletedTodoId);
      };
  
      return {
        todos,
        handleTodoDeleted
      };
    }
  };
  </script>
  
  <style scoped>
  .todo-list {
    max-width: 600px;
    margin: 0 auto;
    padding: 20px;
  }
  
  .title {
    font-size: 24px;
    margin-bottom: 10px;
  }
  
  .link {
    display: block;
    margin-bottom: 20px;
    color: #007bff;
    text-decoration: none;
  }
  
  .todos-list {
    list-style: none;
    padding: 0;
  }
  
  /* Style the TodoItem component if needed */
  .todo-item {
    border: 1px solid #ccc;
    padding: 10px;
    margin: 10px 0;
  }
  </style>
  