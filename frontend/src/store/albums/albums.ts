import { defineStore } from 'pinia';

import axios from 'axios';

import { IAlbum } from '@/store/albums/albums.interfaces';

export const useAlbumsStore = defineStore('albums', {
  state: () => ({
    albums: [] as IAlbum[],
  }),
  actions: {
    async fetchAlbums() {
      try {
        const respone = await axios.get('http://127.0.0.1:8000/api/v1/albums/');
        this.albums = await respone.data;
      } catch (error) {
        console.error(error);
        throw error;
      }
    },
  },
})
