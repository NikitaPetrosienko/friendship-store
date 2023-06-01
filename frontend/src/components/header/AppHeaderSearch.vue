<script setup lang="ts">
import { useProductsStore } from '@/store/products/products';

import { ref } from 'vue';

const productsStore = useProductsStore();

const searchInput = ref('');

const searchPanelProducts = () => {
  isShowList.value = true;
  productsStore.searchProductsByUserInput({ word: searchInput.value });
}

const isShowList = ref(false);

const closeProductsList = () => {
  isShowList.value = false;
}

</script>

<template>
  <div class="header-search__search">
    <input class="header-search__input" v-model="searchInput" @input="searchPanelProducts" type="text" placeholder="Поиск">
    <div v-if="productsStore.searchListProducts.length !== 0 && isShowList" class="header-search__select">
      <router-link
        v-for="item in productsStore.searchListProducts"
        :key="item.id"
        :to="{
          name: 'ProductPage',
          params: { category: `${item.category.category_name}`, id: `${item.model}`, }
        }"
        class="header-search__option"
        @click="closeProductsList"
        >{{ item.product_name }}
      </router-link >
    </div>
    <button class="header-search__button" type="button">Найти</button>
  </div>
</template>

<style lang="scss" scoped>
@import '@/assets/scss/_variables.scss';
@import '@/assets/scss/_mixins.scss';
.header-search__search {
  display: flex;
  position: relative;
}
.header-search__input {
  width: 100%;
  padding: 12px 0 13px 19px;
  border: 2px solid #000000
}
.header-search__button {
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
.header-search__select {
  position: absolute;
  top: 70px;
  left: 0;
  z-index: 10;
  width: 100%;
  background-color: $white;
  padding: 10px;
  border-radius: 15px;
  box-shadow: 0px 4px 10px rgba(187, 225, 250, 0.9);
}

.header-search__option {
  display: block;
  text-decoration: none;
  color: $blue;
  padding: 5px;
  transition: all 0.3s ease;
}

.header-search__option:hover {
  background-color: $blue;
  color: $white;
}

.header-search__option + .header-search__option {
  margin-top: 10px;
}
</style>