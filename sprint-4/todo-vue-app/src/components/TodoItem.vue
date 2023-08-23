<template>
    <div class="todo-item">
      <h3>{{ copiedTodo.title }}</h3>
      <p>{{ copiedTodo.description }}</p>
      <button @click="toggleCompletion">
        {{ copiedTodo.completed ? 'Completed' : 'Completed' }}
      </button>
      <button @click="deleteTodoItem">Delete</button>
    </div>
  </template>
  
  <script>
  import { ref } from 'vue';
  import { updateTodo, deleteTodo } from '../todos';
  
  export default {
    props: {
      todo: Object
    },
    setup(props, { emit }) {
      const copiedTodo = ref({ ...props.todo }); // Create a copy of the todo prop
  
      const toggleCompletion = () => {
        copiedTodo.value.completed = !copiedTodo.value.completed;
        updateTodo(copiedTodo.value);
      };
  
      const deleteTodoItem = () => {
        deleteTodo(copiedTodo.value.id);
        emit('todo-deleted', copiedTodo.value.id); // Emit an event to notify parent
      };
  
      return {
        copiedTodo,
        toggleCompletion,
        deleteTodoItem
      };
    }
  };
  </script>
  
  <style scoped>
  .todo-item {
    border: 1px solid #ccc;
    padding: 10px;
    margin: 10px 0;
  }
  </style>
  