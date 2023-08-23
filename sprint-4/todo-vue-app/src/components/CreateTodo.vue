<template>
    <div class="create-todo">
      <h2 class="create-todo-title">Create Todo</h2>
      <router-link class="go-to-todos-link" to="/">Go to Todos</router-link>
      <form class="todo-form" @submit.prevent="createTodo">
        <label for="title">Title</label>
        <input type="text" id="title" v-model="title" required />
        <label for="description">Description</label>
        <textarea id="description" v-model="description" required></textarea>
        <button class="create-todo-button" type="submit">Create Todo</button>
      </form>
    </div>
  </template>
  
  <script>
  // ... (unchanged)
  </script>
  
  <style scoped>
  .create-todo {
    max-width: 600px;
    margin: 0 auto;
    padding: 20px;
  }
  
  .create-todo-title {
    font-size: 24px;
    margin-bottom: 10px;
  }
  
  .go-to-todos-link {
    display: block;
    margin-bottom: 20px;
    color: #007bff;
    text-decoration: none;
  }
  
  .todo-form label {
    display: block;
    margin-top: 10px;
    font-weight: bold;
  }
  
  .todo-form input,
  .todo-form textarea {
    width: 100%;
    padding: 8px;
    margin-top: 5px;
    margin-bottom: 15px;
    border: 1px solid #ccc;
    border-radius: 4px;
  }
  
  .create-todo-button {
    background-color: #007bff;
    color: white;
    border: none;
    padding: 10px 20px;
    cursor: pointer;
    transition: background-color 0.3s;
  }
  
  .create-todo-button:hover {
    background-color: #0056b3;
  }
  </style>
  