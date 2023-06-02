import { defineStore } from 'pinia';

import axios from 'axios';
import { AuthApi } from '@/api/AuthApi';
import { DefaultAPIInstance } from '@/api';

import router from '@/router';

import { useCommonStore } from '@/store/common/common';

const commonStore = useCommonStore();

export const useAuthStore = defineStore('auth', {
  state: () => ({
    credentials: {
      token: localStorage.getItem('token') || null
    },
  }),
  actions: {
    async loginUser({ email, password }) {
      commonStore.clearAlert();
      commonStore.setLoading(true);
      try {
        const response = await AuthApi.login(email, password);
        const data = await response.data;
        this.credentials.token = data.auth_token;
        localStorage.setItem("token", data.auth_token);
        DefaultAPIInstance.defaults.headers['Authorization'] = `Token ${this.credentials.token}`
        commonStore.setLoading(false);
        router.push('/');
      } catch (error) {

        commonStore.setLoading(false);
        commonStore.setAlertInfo({
          info: JSON.parse(error.response.request.response),
          status: 'danger'
        }); // ToDO
        throw error;
      }
    },
    async logoutUser() {
      commonStore.clearAlert();
      commonStore.setLoading(true);
      try {
        const response = await AuthApi.logout();
        const data = await response.data;
        this.credentials.token = null;
        localStorage.removeItem("token");
        delete DefaultAPIInstance.defaults.headers['Authorization'];

        commonStore.setLoading(false);
        commonStore.setAlertInfo({
          info: 'Вы успешно вышли из аккаунта!',
          status: 'success'
        });
      } catch (error) {
        commonStore.setLoading(false);
        commonStore.setAlertInfo({
          info: 'Возникла ошибка с выходом из аккаунта!',
          status: 'danger'  
        }); // ToDO;
        throw error;
      }
    },
    async registerUser({ email, password }) {
      commonStore.clearAlert();
      commonStore.setLoading(true);
      try {
        const response = await AuthApi.register(email, password);
        const data = await response.data;
        commonStore.setLoading(false);
        commonStore.setAlertInfo({
          info: 'Вы успешно зарегистрировались!',
          status: 'success'
        });
        setTimeout(() => {
          router.push('/login');
        }, 3000);
      } catch (error) {
        commonStore.setLoading(false);
        commonStore.setAlertInfo({
          info: JSON.parse(error.response.request.response),
          status: 'danger'  
        }); // ToDO
        throw error;
      }
    },
  },
  getters: {
    isUserLoggedIn(this) {
      return this.credentials.token !== null;
    }
  }
})
