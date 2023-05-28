<script setup lang="ts">
import { RouterView } from 'vue-router';

import { useAuthStore } from '@/store/auth/auth';

const authStore = useAuthStore();

const token = JSON.parse(localStorage.getItem("authToken"));

if (token) {
  authStore.setUserToken(token);
}
</script>

<template>
  <RouterView />
</template>

<style lang="scss">
@import '@/assets/scss/style.scss';

</style>