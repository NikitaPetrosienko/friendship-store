import { defineStore } from 'pinia'

interface IState {
  loading: boolean,
  error: null | string,
}

export const useCommonStore = defineStore('common', {
  state: () => ({
    loading: false,
    error: null,
  } as IState),
  actions: {
    setLoading(payload: boolean) {
      this.loading = payload;
    },
    setError(payload: string | null) {
      this.error = payload;
    },
    clearError() {
      this.error = null;
    },
  },
})
