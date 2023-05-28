<script setup lang="ts">
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
    <div class="header-links__search">
      <input class="header-links__input" type="text" placeholder="Поиск">
      <button class="header-links__button" type="button">Найти</button>
    </div>
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
.header-links__search {
  display: flex;
}
.header-links__input {
  width: 100%;
  padding: 12px 0 13px 19px;
  border: 2px solid #000000
}
.header-links__button {
  width: 102px;
  height: 63px;
  background-color: $gray;
  background-image: url(../../assets/img/svg/search.svg);
  background-position: center;
  background-repeat: no-repeat;
  background-size: 35px 35px;
  padding: 14px 32px;
  font-size: 0;
  overflow: hidden;
  cursor: pointer;
}
</style>