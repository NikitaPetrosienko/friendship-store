import { defineStore } from 'pinia';

import axios from 'axios';

import { ICart } from '@/store/cart/cart.interfaces';

import { useCommonStore } from '@/store/common/common';
import { useAuthStore } from '@/store/auth/auth';

const commonStore = useCommonStore();
const authStore = useAuthStore();

export const useCartStore = defineStore('cart', {
  state: () => ({
    userCart: {} as ICart, 
  }),
  actions: {
    
    async addToCart({ token, product_id }) {
      commonStore.clearAlert();
      commonStore.setLoading(true);
      try {
        const respone = await axios.post('http://127.0.0.1:8000/api/v1/basket/', { token, product_id });
        commonStore.setLoading(false);
        commonStore.setAlertInfo({
          info: 'Товар был добавлен в корзину',
          status: 'success'
        });
      } catch (error) { 
        commonStore.setLoading(false);
        commonStore.setAlertInfo({
          info: error.response.data.error,
          status: 'danger'
        });
        throw error;
      }
    },
    async fetchUserCart({ token }) {
      commonStore.clearAlert();
      commonStore.setLoading(true);
      try {
        const respone = await axios.get(`http://127.0.0.1:8000/api/v1/basket/${token}/`);
        this.userCart = await respone.data;
        commonStore.setLoading(false);
      } catch (error) { 
        commonStore.setLoading(false);
        commonStore.setAlertInfo({
          info: 'Невозможно загрузить корзину',
          status: 'danger'
        });
        throw error;
      }
    },
    async decreaseProductCount({ basket_id }) {
      commonStore.clearAlert();
      commonStore.setLoading(true);
      try {
        const respone = await axios.get(`http://127.0.0.1:8000/api/v1/basket/${basket_id}/decr/`);
        this.fetchUserCart({ token: authStore.credentials.token});
        commonStore.setLoading(false);
        commonStore.setAlertInfo({
          info: 'Количество товара было изменено',
          status: 'warning'
        });
      } catch (error) { 
        commonStore.setLoading(false);
        commonStore.setAlertInfo({
          info: error.response.data.error,
          status: 'danger'
        });
        throw error;
      }
    },
    async increseProductCount({ basket_id }) {
      try {
        const respone = await axios.get(`http://127.0.0.1:8000/api/v1/basket/${basket_id}/incr/`);
        this.fetchUserCart({ token: authStore.credentials.token});
        commonStore.setLoading(false);
        commonStore.setAlertInfo({
          info: 'Количество товара было изменено',
          status: 'warning'
        });
      } catch (error) { 
        commonStore.setLoading(false);
        commonStore.setAlertInfo({
          info: error.response.data.error,
          status: 'danger'
        });
        throw error;
      }
    },
  },
})
