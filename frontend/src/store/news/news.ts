import { defineStore } from 'pinia';

import axios from 'axios';

import { INews } from '@/store/news/news.interfaces';

import { useCommonStore } from '@/store/common/common';

const commonStore = useCommonStore();

export const useNewsStore = defineStore('news', {
  state: () => ({
    news: [] as INews[],
  }),
  actions: {
    async fetchNews() {
      commonStore.clearAlert();
      commonStore.setLoading(true);
      try {
        const respone = await axios.get('http://127.0.0.1:8000/api/v1/news/');
        this.news = await respone.data;
        commonStore.setLoading(false);
      } catch (error) {
        commonStore.setLoading(false);
        commonStore.setAlertInfo({  
          info: error.response.data.error,
          status: 'danger'
        });
        throw error;
      }
    }
  },
})
