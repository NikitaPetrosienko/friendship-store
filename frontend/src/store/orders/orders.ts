import { defineStore } from 'pinia';

import axios from 'axios';

import { IOrder } from '@/store/orders/orders.interfaces';

export const useOrdersStore = defineStore('orders', {
  state: () => ({
    order: {} as IOrder,
  }),
  actions: {
    async createOrder() {
      try {
        const respone = await axios.post('http://127.0.0.1:8000/api/v1/order/', this.order);
      } catch (error) {
        console.error(error);
        throw error;
      }
    },
    setOrderInfo(orderInfo: IOrder) {
      this.order = orderInfo;
    }
  },
})
