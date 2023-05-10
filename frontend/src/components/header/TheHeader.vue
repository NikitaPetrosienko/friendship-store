<script setup lang="ts">
import AppHeaderLinks from '@/components/header/AppHeaderLinks.vue'
import AppHeaderPanel from '@/components/header/AppHeaderPanel.vue'
</script>

<template>
  <header class="header">
    <div class="container header__container">
      <img class="header__logo" src="../../assets/img/logo.png" alt="Дружба Store">

      <AppHeaderLinks />

      <AppHeaderPanel />

    </div>
  </header>
</template>

<style lang="scss" scoped>
@import '@/assets/scss/_variables.scss';
@import '@/assets/scss/_mixins.scss';

.header {
  background-color: $blue;
  padding: 27px 0 37px;
}
.header__container {
  display: flex;
  align-items: center;
}
.header__logo {
  display: block;
  margin-right: 20px;
}

</style>