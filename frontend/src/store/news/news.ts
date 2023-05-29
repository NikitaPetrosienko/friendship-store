import { defineStore } from 'pinia';

import axios from 'axios';

import { INews } from '@/store/news/news.interfaces';

export const useNewsStore = defineStore('news', {
  state: () => ({
    news: [] as INews[],
  }),
  actions: {
    async fetchNews() {
      try {
        const respone = await axios.get('http://127.0.0.1:8000/api/v1/news/');
        this.news = await respone.data;
      } catch (error) {
        console.error(error);
        throw error;
      }
    }
  },
})
