<template>
  <div>
    <h1>Menu</h1>
    <ul>
      <li v-for="dish in dishes" :key="dish.dish_id">
        {{ dish.dish_name }} - ${{ dish.price }}
      </li>
    </ul> 
  </div>
</template>

<script>
import { ref } from 'vue';
import axios from 'axios';

export default {
  data() {
    return {
      dishes: ref([]) // To store fetched dishes
    };
  },
  mounted() {
    // Fetch dishes from Django backend using Axios
    this.fetchDishes();
  },
  methods: {
    async fetchDishes() {
      try {
        const response = await axios.get('http://127.0.0.1:8000/api/get_dishes');
        this.dishes = response.data;
      } catch (error) {
        console.error('Error fetching dishes:', error);
      }
    }
  }
};
</script>