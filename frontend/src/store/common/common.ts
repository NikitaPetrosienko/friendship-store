import { defineStore } from 'pinia'

interface IState { // ToDo
  loading: boolean,
  error: null | string,
}

export const useCommonStore = defineStore('common', {
  state: () => ({
    loading: false,
    alert: {
      info: null,
      status: '' as 'success' | 'danger' | 'warning' | ''
    },
  }),
  actions: {
    setLoading(payload) {
      this.loading = payload;
    },
    setAlertInfo({info, status}) {
      this.alert.info = info;
      this.alert.status = status;
      setTimeout(() => {
        this.clearAlert();
      }, 5000);
    },
    clearAlert() {
      this.alert.info = null;
      this.alert.status = '';
    },
  },
})
