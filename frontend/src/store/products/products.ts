import { defineStore } from 'pinia';

import axios from 'axios';

import { IProduct, IProductPage, IFavouriteProduct } from '@/store/products/products.interfaces';

import { useCommonStore } from '@/store/common/common';
import { useAuthStore } from '@/store/auth/auth';

const commonStore = useCommonStore();
const authStore = useAuthStore();


export const useProductsStore = defineStore('products', {
  state: () => ({
    products: [] as IProduct[],
    searchListProducts: [] as IProduct[],
    currentProduct: {} as IProductPage,
    filters: {
      minPrice: 100,
      maxPrice: 99999,
      sortStatus: 'incr'
    },
    favoritesProducts : [] as IFavouriteProduct[],
  }),
  actions: {
    async fetchProductsByBrand(brandName) {
      commonStore.clearAlert();
      commonStore.setLoading(true);
      try {
        const respone = await axios.get(`http://127.0.0.1:8000/api/v1/product_by_brand/${brandName}/?min_price=${this.filters.minPrice}&max_price=${this.filters.maxPrice}&sort_by=${this.filters.sortStatus}`);
        if (this.filters.sortStatus === 'incr') {
          this.products = await respone.data.sort((a, b) => a - b);
        } else {
          this.products = await respone.data.sort((a, b) => b - a);
        }
        
        this.products = await respone.data;
        commonStore.setLoading(false);
      } catch (error) { 
        commonStore.setLoading(false);
        commonStore.setAlertInfo({
          info: error.response.data.error,
          status: 'error'
        });
        throw error;
      }
    },
    async fetchProductsByCategory(categoryName) {
      commonStore.clearAlert();
      commonStore.setLoading(true);
      try {
        const respone = await axios.get(`http://127.0.0.1:8000/api/v1/product_by_category/${categoryName}/?min_price=${this.filters.minPrice}&max_price=${this.filters.maxPrice}&sort_by=${this.filters.sortStatus}`);
        this.products = await respone.data;
        commonStore.setLoading(false);
      } catch (error) { 
        commonStore.setLoading(false);
        commonStore.setAlertInfo({
          info: error.response.data.error,
          status: 'error'
        });
        throw error;
      }
    },
    async fetchProductBySlug(productSlug) {
      commonStore.clearAlert();
      commonStore.setLoading(true);
      try {
        const respone = await axios.get(`http://127.0.0.1:8000/api/v1/product/${productSlug}`);
        this.currentProduct = await respone.data;
        commonStore.setLoading(false);
      } catch (error) { 
        commonStore.setLoading(false);
        commonStore.setAlertInfo({
          info: error.response.data.error,
          status: 'error'
        });
        throw error;
      }
    },
    async searchProductsByUserInput({ word }) {
      commonStore.clearAlert();
      commonStore.setLoading(true);
      try {
        const respone = await axios.get(`http://127.0.0.1:8000/api/v1/search/${word}`);
        this.searchListProducts = await respone.data;
        commonStore.setLoading(false);
      } catch (error) { 
        commonStore.setLoading(false);
        commonStore.setAlertInfo({
          info: error.response.data.error,
          status: 'error'
        });
        throw error;
      }
    },
    async addToFavourites({ token, product_id}) {
      commonStore.clearAlert();
      commonStore.setLoading(true);
      try {
        const respone = await axios.post('http://127.0.0.1:8000/api/v1/favorites/', { token, product_id});
        commonStore.setLoading(false);
        commonStore.setAlertInfo({
          info: 'Товар был добавлен в избранное',
          status: 'success'
        });
      } catch (error) { 
        commonStore.setLoading(false);
        commonStore.setAlertInfo({
          info: error.response.data.error,
          status: 'error'
        });
        throw error;
      }
    },
    async fetchFavouriteProducts({ token }) {
      commonStore.clearAlert();
      commonStore.setLoading(true);
      try {
        const respone = await axios.get(`http://127.0.0.1:8000/api/v1/favorites/${token}`);
        this.favoritesProducts = await respone.data;
      } catch (error) { 
        commonStore.setLoading(false);
        commonStore.setAlertInfo({
          info: error.response.data.error,
          status: 'error'
        });
        throw error;
      }
    },
    async deleteFavouriteProduct({ id }) {
      commonStore.clearAlert();
      commonStore.setLoading(true);
      try {
        const response = await axios.delete(`http://127.0.0.1:8000/api/v1/delete_favorite/${id}`);
        this.fetchFavouriteProducts({ token: authStore.credentials.token});
        commonStore.setLoading(false);
        commonStore.setAlertInfo({
          info: 'Товар был удален из избранных',
          status: 'success'
        });
      } catch (error) { 
        commonStore.setLoading(false);
        commonStore.setAlertInfo({
          info: error.response.data.error,
          status: 'error'
        });
        throw error;
      }
    },
    async addComment({ name_user, product_id, body}) {
      commonStore.clearAlert();
      commonStore.setLoading(true);
      try {
        const respone = await axios.post('http://127.0.0.1:8000/api/v1/review/', { name_user, product_id, body});
        this.fetchProductBySlug(this.currentProduct.product.model);
        commonStore.setLoading(false);
        commonStore.setAlertInfo({
          info: 'Комментарий был успешно добавлен',
          status: 'success'
        });
      } catch (error) { 
        commonStore.setLoading(false);
        commonStore.setAlertInfo({
          info: error.response.data.error,
          status: 'error'
        });
        throw error;
      }
    },
  },
})
