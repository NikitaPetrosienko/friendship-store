import { defineStore } from 'pinia';

import axios from 'axios';

import { IBrand } from '@/store/brands/brands.interfaces';

export const useBrandsStore = defineStore('brands', {
  state: () => ({
    brands: [] as IBrand[],
  }),
  actions: {
    async fetchBrands() {
      try {
        const respone = await axios.get('http://127.0.0.1:8000/api/v1/brands/');
        this.brands = await respone.data;
      } catch (error) {
        console.error(error);
        throw error;
      }
    },
  },
})
