<template>
  <div id="app">
    <CounterDisplay />
  </div>
</template>

<script>
import CounterDisplay from './components/CounterDisplay.vue';

export default {
  name: 'App',
  components: {
    CounterDisplay
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
