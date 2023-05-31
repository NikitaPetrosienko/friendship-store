import { defineStore } from 'pinia';

import axios from 'axios';

import { IProduct, IProductPage, IFavouriteProduct } from '@/store/products/products.interfaces';

import { useCommonStore } from '@/store/common/common';

import { useAuthStore } from '@/store/auth/auth';

export const useProductsStore = defineStore('products', {
  state: () => ({
    products: [] as IProduct[],
    currentProduct: {} as IProductPage,
    filters: {
      minPrice: 100,
      maxPrice: 99999,
      sortStatus: 'increase'
    },
    favoritesProducts : [] as IFavouriteProduct[]
  }),
  actions: {
    async fetchProductsByBrand(brandName) {
      console.log('filters: ', { min_price: this.filters.minPrice, max_price: this.filters.maxPrice, sort_by: this.filters.sortStatus });
      const commonStore = useCommonStore();
      commonStore.clearError();
      commonStore.setLoading(true);
      try {
        const respone = await axios.get(`http://127.0.0.1:8000/api/v1/product_by_brand/${brandName}`);
        this.products = await respone.data;
        setTimeout(() => {
          commonStore.setLoading(false);
        }, 2000); // ToDO
      } catch (error) { 
        commonStore.setLoading(false);
        commonStore.setError(error);
        throw error;
      }
    },
    async fetchProductsByCategory(categoryName) {
      console.log('filters: ', { min_price: this.filters.minPrice, max_price: this.filters.maxPrice, sort_by: this.filters.sortStatus });
      try {
        const respone = await axios.get(`http://127.0.0.1:8000/api/v1/product_by_category/${categoryName}`);
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
    async addToCart({ user_id, product_id}) { //ToDO
      console.log('addToCart: ', { user_id, product_id })
    },
    async getUserCart({ user_id}) { // ToDo
      try {
        const respone = await axios.get('http://127.0.0.1:8000/api/v1/basket/1/', { user_id });
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
      try {
        const response = await axios.delete(`http://127.0.0.1:8000/api/v1/delete_favorite/${id}`);
        const authStore = useAuthStore();
        this.fetchFavouriteProducts({ token: authStore.user.id})
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
