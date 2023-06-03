import { defineStore } from 'pinia';

import axios from 'axios';

import { IOrder } from '@/store/orders/orders.interfaces';

import { useCommonStore } from '@/store/common/common';

const commonStore = useCommonStore();

export const useOrdersStore = defineStore('orders', {
  state: () => ({
    order: {} as IOrder,
  }),
  actions: {
    async createOrder() {
      commonStore.clearAlert();
      commonStore.setLoading(true);
      try {
        const respone = await axios.post('http://127.0.0.1:8000/api/v1/order/', this.order);
        commonStore.setLoading(false);
        commonStore.setAlertInfo({
          info: 'Заказ был успешно создан',
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
    setOrderInfo(orderInfo: IOrder) {
      this.order = orderInfo;
    }
  },
})
