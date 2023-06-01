<script setup lang="ts">
import AppHeaderSearch from '@/components/header/AppHeaderSearch.vue';

import { ref } from 'vue';

const navigationList = ref([
  {
    id: 1,
    title: 'Бренды',
    url: '/'
  },
  {
    id: 2,
    title: 'Скейт',
    url: '/products/?category=skateboards'
  },
  {
    id: 3,
    title: 'Обувь',
    url: '/products/?category=shoes'
  },
  {
    id: 4,
    title: 'Одежда',
    url: '/products/?category=clothes'
  },
  {
    id: 5,
    title: 'Фотоальбом',
    url: '/albums'
  },
  {
    id: 6,
    title: 'О нас',
    url: '/aboutus'
  },
]);

</script>

<template>
  <div class="header-links">
    <nav class="header-links__navigation">
      <ul class="header-links__list">
        <li 
          class="header-links__item"
          v-for="link in navigationList" :key="link.id"
        >
          <router-link
            class="header-links__link"
            :to="link.url"
          >{{ link.title }}</router-link>
        </li>
      </ul>
    </nav>
    <AppHeaderSearch />
  </div>
</template>

<style lang="scss" scoped>
@import '@/assets/scss/_variables.scss';
@import '@/assets/scss/_mixins.scss';
.header-links {
  flex: 1 0 auto;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}
.header-links__navigation {
  
}
.header-links__list {
  display: flex;
  gap: 30px;
  padding: 0;
  margin: 0;
}
.header-links__item {
  list-style: none;
}
.header-links__link {
  @include font(24px, 400, 30px);
  color: $white;
  text-decoration: none;
}
</style>