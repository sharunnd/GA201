<template>
    <div class="counter">
    <h2>Counter App</h2>
    <div class="counter-value">{{ count }}</div>
    <button @click="increment">Increment</button>
    <button @click="decrement" :disabled="count === 0">Decrement</button>
  </div>
</template>
<script>
export default {
    name: 'CounterDisplay',
    data(){
        return {
            count: 0
        }
    },
    methods:{
        increment(){
            this.count ++;
        },
        decrement(){
            
                this.count--;
            
        }
    }
}
</script>