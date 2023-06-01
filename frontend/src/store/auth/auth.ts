import { defineStore } from 'pinia';

import axios from 'axios';
import { AuthApi } from '@/api/AuthApi';
import { DefaultAPIInstance } from '@/api';

import router from '@/router';

export const useAuthStore = defineStore('auth', {
  state: () => ({
    credentials: {
      token: localStorage.getItem('token') || null
    },
  }),
  actions: {
    async loginUser({ email, password }) {
      try {
        const response = await AuthApi.login(email, password);
        const data = await response.data;
        this.credentials.token = data.auth_token;
        localStorage.setItem("token", data.auth_token);
        DefaultAPIInstance.defaults.headers['Authorization'] = `Token ${this.credentials.token}`
        console.log('DefaultAPIInstance.defaults.headers["Authorization"]: ', DefaultAPIInstance.defaults.headers['authoriaztion']);
        router.push('/');
      } catch (error) {
        console.error(error);
        throw error;
      }
    },
    // async loginUser({ email, password }) {
    //   try {
    //     const response = await axios.post('http://127.0.0.1:8000/auth/token/login/', { username: email, password});
    //     const data = await response.data;
    //     this.user.id = data.auth_token;
    //     localStorage.setItem("authToken", JSON.stringify(data.auth_token));
    //     router.push('/');
    //   } catch (error) {
    //     console.error(error);
    //     throw error;
    //   }
    // },
    async logoutUser() {
      try {
        const response = await AuthApi.logout();
        const data = await response.data;
        this.credentials.token = null;
        localStorage.removeItem("token");
        delete DefaultAPIInstance.defaults.headers['Authorization'];
      } catch (error) {
        console.error(error);
        throw error;
      }
    },
    // async logoutUser() {
    //   try {
    //     const authToken = JSON.parse(localStorage.getItem("authToken"));
    //     const headers = {
    //       Authorization: `Token ${authToken}`,
    //     };
    //     const response = await axios.post(
    //       'http://127.0.0.1:8000/auth/token/logout/',
    //       {},
    //       { headers }
    //     );
    //     this.user.id = null;
    //     localStorage.removeItem("authToken");
    //     router.push('/');
    //   } catch (error) {
    //     console.error(error);
    //     throw error;
    //   }
    // },
    async registerUser({ email, password }) {
      try {
        const response = await AuthApi.register(email, password);
        const data = await response.data;
        alert('Вы успешно зарегистрированы!');
        router.push('/login');
      } catch (error) {
        console.error(error);
        throw error;
      }
    },
    // async registerUser({ email, password }) {
    //   try {
    //     const response = await axios.post('http://127.0.0.1:8000/auth/users/', { email, password});
    //     const data = await response.data;
    //     alert('Вы успешно зарегистрированы!');
    //     router.push('/login');
    //   } catch (error) {
    //     console.error(error);
    //     throw error;
    //   }
    // },
  },
  getters: {
    isUserLoggedIn(this) {
      return this.credentials.token !== null;
    }
  }
})
