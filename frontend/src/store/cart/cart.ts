import { defineStore } from 'pinia';

import axios from 'axios';

import { ICart } from '@/store/cart/cart.interfaces';

import { useAuthStore } from '@/store/auth/auth';

export const useCartStore = defineStore('cart', {
  state: () => ({
    userCart: {} as ICart, 
  }),
  actions: {
    
    async addToCart({ token, product_id }) {
      console.log('addToCart: ', { token, product_id })
      try {
        const respone = await axios.post('http://127.0.0.1:8000/api/v1/basket/', { token, product_id });
      } catch (error) { 
        console.error(error);
        throw error;
      }
    },
    async fetchUserCart({ token }) {
      try {
        const respone = await axios.get(`http://127.0.0.1:8000/api/v1/basket/${token}/`);
        this.userCart = await respone.data;
      } catch (error) { 
        console.error(error);
        throw error;
      }
    },
    async decreaseProductCount({ basket_id }) {
      const authStore = useAuthStore();
      try {
        const respone = await axios.get(`http://127.0.0.1:8000/api/v1/basket/${basket_id}/decr/`);
        this.fetchUserCart({ token: authStore.credentials.token});
      } catch (error) { 
        console.error(error);
        throw error;
      }
    },
    async increseProductCount({ basket_id }) {
      const authStore = useAuthStore();
      try {
        const respone = await axios.get(`http://127.0.0.1:8000/api/v1/basket/${basket_id}/incr/`);
        this.fetchUserCart({ token: authStore.credentials.token});
      } catch (error) { 
        console.error(error);
        throw error;
      }
    },
  },
})
