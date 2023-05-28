import { defineStore } from 'pinia';

import axios from 'axios';

import router from '@/router';

export const useAuthStore = defineStore('auth', {
  state: () => ({
    user: {
      id: null
    },
  }),
  actions: {
    async registerUser({ email, password }) {
      try {
        const response = await axios.post('http://127.0.0.1:8000/auth/users/', { email, password});
        const data = await response.data;
        alert('Вы успешно зарегистрированы!');
        router.push('/login');
      } catch (error) {
        console.error(error);
        throw error;
      }
    },
    async loginUser({ email, password }) {
      try {
        const response = await axios.post('http://127.0.0.1:8000/auth/token/login/', { username: email, password});
        const data = await response.data;
        this.user.id = data.auth_token;
        localStorage.setItem("authToken", JSON.stringify(data.auth_token));
        router.push('/');
      } catch (error) {
        console.error(error);
        throw error;
      }
    },
    async logoutUser() {
      try {
        const authToken = JSON.parse(localStorage.getItem("authToken"));
        const headers = {
          Authorization: `Token ${authToken}`,
        };
        const response = await axios.post(
          'http://127.0.0.1:8000/auth/token/logout/',
          {},
          { headers }
        );
        this.user.id = null;
        localStorage.removeItem("authToken");
        router.push('/');
      } catch (error) {
        console.error(error);
        throw error;
      }
    },
    setUserToken(token) {
      this.user.id = token;
    }
  },
  getters: {
    isUserLoggedIn(this) {
      return this.user.id !== null;
    }
  }
})
