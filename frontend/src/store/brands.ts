import { defineStore } from 'pinia';

import axios from 'axios';

export const useBrandsStore = defineStore('brands', {
  state: () => ({
    brands: [
      { id: 1, imagePath: "src/assets/img/brands/img1.png" },
      { id: 2, imagePath: "src/assets/img/brands/img2.png" },
      { id: 3, imagePath: "src/assets/img/brands/img3.png" },
    ],
  }),
  actions: {
    async fetchBrands() {
      try {
        const respone = await axios.get('https://jsonplaceholder.typicode.com/posts');
        const data = await respone.data;
      } catch (error) {
        console.error(error);
        throw error;
      }
    }
  },
})
