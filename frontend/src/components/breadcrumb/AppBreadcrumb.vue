
<script setup lang="ts">

</script>

<template>
  <nav class="breadcrumb">
    <ul class="breadcrumb__list">
      <li class="breadcrumb__item">
        <router-link class="breadcrumb__link" to="/" >Главная</router-link>
      </li>
      <li class="breadcrumb__item">
        <router-link class="breadcrumb__link" to="/">О магазине</router-link>
      </li>
    </ul>
  </nav>
</template>

<style lang="scss" scoped>
@import '@/assets/scss/_variables.scss';
@import '@/assets/scss/_mixins.scss';
.breadcrumb__list {
  display: flex;
  padding: 14px 0 0;
  margin: 0 0;
  list-style: none;
  color: $gray2;
}
.breadcrumb__item {
  @include font(18px, 400, 22px);
}
.breadcrumb__item::after {
  content: '>>';
  margin: 0 8px;
}

.breadcrumb__item:last-child::after {
  content: '';
}

.breadcrumb__link {
  color: $gray2;
  text-decoration: none;
}
</style>