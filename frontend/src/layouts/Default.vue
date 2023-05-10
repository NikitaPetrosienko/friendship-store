<template>
  <div>
    <TheHeader />
    <main>
      <router-view />
    </main>
  </div>
</template>

<script setup lang="ts">
import TheHeader from '@/components/header/TheHeader.vue';

</script>

<style scoped>

</style>