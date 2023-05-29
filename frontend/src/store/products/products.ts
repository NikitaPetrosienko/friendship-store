import { defineStore } from 'pinia';

import axios from 'axios';

import { IProduct, IProductPage } from '@/store/products/products.interfaces';

export const useProductsStore = defineStore('products', {
  state: () => ({
    products: [] as IProduct[],
    currentProduct: {} as IProductPage,
  }),
  actions: {
    async fetchProductsByBrand(brandName) {
      try {
        const respone = await axios.get(`http://127.0.0.1:8000/api/v1/product_by_brand/${brandName}`);
        this.products = await respone.data;
      } catch (error) { 
        console.error(error);
        throw error;
      }
    },
    async fetchProductsByCategory(categoryName) {
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
    }
  },
})
