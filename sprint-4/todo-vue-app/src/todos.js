import todosData from './data';

let todos = [...todosData];

export function getTodos() {
  return todos;
}

export function addTodo(todo) {
  todos.push(todo);
}

export function updateTodo(updatedTodo) {
    const index = todos.findIndex(todo => todo.id === updatedTodo.id);
    if (index !== -1) {
      todos[index] = updatedTodo;
    }
  }
  
export function deleteTodo(todoId) {
    todos = todos.filter(todo => todo.id !== todoId);
}
// Implement updateTodo and deleteTodo functions
