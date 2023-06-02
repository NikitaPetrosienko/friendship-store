<script setup lang="ts">
import TheHeader from '@/components/header/TheHeader.vue';
import AppAlert from '@/components/alert/AppAlert.vue';

</script>

<template>
  <div class="default-layout">
    <div class="container container_alert">
      <AppAlert class="alert"/>
    </div>
    <TheHeader />
    <main>
      <router-view />
    </main>
  </div>
</template>

<style lang="scss" scoped>
.container_alert {
  position: relative;
}

.alert {
  position: absolute;
  top: 0;
  left: 0;
  z-index: 60;
  width: 100%;
}
</style>