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

const isShowBurgerMenu = ref(false);

const toggleBurgerMenu = () => {
  isShowBurgerMenu.value = !isShowBurgerMenu.value;
}

</script>

<template>
  <div 
    class="header-burger"
    :class="isShowBurgerMenu ? 'header-burger_active' : ''"
    @click="toggleBurgerMenu">
    <span></span>
    <nav 
      v-if="isShowBurgerMenu"
      class="header-burger__menu"
    >
      <ul class="header-burger__list">
        <li 
          class="header-burger__item" 
          v-for="link in navigationList" :key="link.id"
        >
          <router-link
            class="header-burger__link"
            :to="link.url"
          >{{ link.title }}</router-link>
        </li>
      </ul>
    </nav>
  </div>
</template>

<style lang="scss" scoped>
@import '@/assets/scss/_variables.scss';
@import '@/assets/scss/_mixins.scss';

.header-burger {
  display: none;
  background-color: $blue;
  z-index: 50;

  @include for-size(laptop-s) {
    display: block;
    position: relative;
    width: 30px;
    height: 20px;
  }
}

.header-burger::before,
.header-burger::after {
  content: '';
  position: absolute;
  width: 100%;
  height: 2px;
  left: 0;
  background-color: $white;
}

.header-burger::before {
  top: 0;
}

.header-burger::after {
  bottom: 0;
}

.header-burger span {
  position: absolute;
  width: 100%;
  height: 2px;
  left: 0;
  top: 8px;
  background-color: $white;
}

  /* анимация крестика */
  .header-burger.header-burger_active span{
    transform: scale(0) translate(0px, -50%);
  }
  .header-burger.header-burger_active::before {
    top: 50%;
    transform: rotate(-45deg) translate(0px, -50%);
  }
  .header-burger.header-burger_active::after {
    bottom: 50%;
    transform: rotate(45deg) translate(0px, 50%);
  }
  /* анимация крестика */

.header-burger__menu {
  position: absolute;
  background-color: $blue;
  width: 300px;
  top: 80px;
  right: 0;
  border-radius: 16px;
  z-index: 10px;
}

.header-burger__list {
  list-style: none;
  padding: 0;
  margin: 0;
}
.header-burger__item {
  
}
.header-burger__item:hover {
  background-color: rgb(247, 220, 220);
}
.header-burger__item:first-child:hover {
  border-radius: 16px 16px 0 0;
}
.header-burger__item:last-child:hover {
  border-radius: 0 0 16px 16px;
}

.header-burger__link {
  display: block;
  @include font(24px, 400, 44px);
  color: $white;
  text-transform: uppercase;
  text-decoration: none;
  padding: 15px;
}
.header-burger__link:hover {
  color: $black;
}
</style>