import { defineStore } from 'pinia';

import axios from 'axios';

import { IBrand } from '@/store/brands/brands.interfaces';

import { useCommonStore } from '@/store/common/common';

const commonStore = useCommonStore();

export const useBrandsStore = defineStore('brands', {
  state: () => ({
    brands: [] as IBrand[],
  }),
  actions: {
    async fetchBrands() {
      commonStore.clearAlert();
      commonStore.setLoading(true);
      try {
        const respone = await axios.get('http://127.0.0.1:8000/api/v1/brands/');
        this.brands = await respone.data;
        commonStore.setLoading(false);
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
