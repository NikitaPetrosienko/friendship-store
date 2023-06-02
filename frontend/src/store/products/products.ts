import { defineStore } from 'pinia';

import axios from 'axios';

import { IProduct, IProductPage, IFavouriteProduct } from '@/store/products/products.interfaces';

import { useCommonStore } from '@/store/common/common';

import { useAuthStore } from '@/store/auth/auth';

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
      const commonStore = useCommonStore();
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
        commonStore.setAlertInfo(error);
        throw error;
      }
    },
    async fetchProductsByCategory(categoryName) {
      try {
        const respone = await axios.get(`http://127.0.0.1:8000/api/v1/product_by_category/${categoryName}/?min_price=${this.filters.minPrice}&max_price=${this.filters.maxPrice}&sort_by=${this.filters.sortStatus}`);
        this.products = await respone.data;
      } catch (error) { 
        console.error(error);
        throw error;
      }
    },
    async fetchProductBySlug(productSlug) {
      try {
        const respone = await axios.get(`http://127.0.0.1:8000/api/v1/product/${productSlug}`);
        this.currentProduct = await respone.data;
      } catch (error) { 
        console.error(error);
        throw error;
      }
    },
    async searchProductsByUserInput({ word }) {
      try {
        const respone = await axios.get(`http://127.0.0.1:8000/api/v1/search/${word}`);
        this.searchListProducts = await respone.data;
        console.log('searchListProducts: ', this.searchListProducts)
      } catch (error) { 
        console.error(error);
        throw error;
      }
    },
    async addToFavourites({ token, product_id}) {
      try {
        const respone = await axios.post('http://127.0.0.1:8000/api/v1/favorites/', { token, product_id});
      } catch (error) { 
        console.error(error);
        throw error;
      }
    },
    async fetchFavouriteProducts({ token }) {
      try {
        const respone = await axios.get(`http://127.0.0.1:8000/api/v1/favorites/${token}`);
        this.favoritesProducts = await respone.data;
      } catch (error) { 
        console.error(error);
        throw error;
      }
    },
    async deleteFavouriteProduct({ id }) {
      const authStore = useAuthStore();
      try {
        const response = await axios.delete(`http://127.0.0.1:8000/api/v1/delete_favorite/${id}`);
        this.fetchFavouriteProducts({ token: authStore.credentials.token})
      } catch (error) { 
        console.error(error);
        throw error;
      }
    },
    async addComment({ name_user, product_id, body}) {
      try {
        const respone = await axios.post('http://127.0.0.1:8000/api/v1/review/', { name_user, product_id, body});
        this.fetchProductBySlug(this.currentProduct.product.model);
      } catch (error) { 
        console.error(error);
        throw error;
      }
    },
  },
})
