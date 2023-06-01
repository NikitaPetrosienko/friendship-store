<script setup lang="ts">
import AppFavouriteProduct from '@/components/favourites-page/AppFavouriteProduct.vue';

import { ref, watch } from 'vue';

import { useProductsStore } from '@/store/products/products';
import { useAuthStore } from '@/store/auth/auth';
import { useCommonStore } from '@/store/common/common';

const productsStore = useProductsStore();
const authStore = useAuthStore();
const commonStore = useCommonStore();

productsStore.fetchFavouriteProducts({ token: authStore.credentials.token })

// const productsMock = ref([
//   { id: 1, imagePath: "/src/assets/img/brands/adidas/adidas1.jpeg", title: "Кеды Adidas Busenitz Vulc II Core Black FTWWHT VIVRED", price: 6700 },
//   { id: 2, imagePath: "/src/assets/img/brands/adidas/adidas2.jpeg", title: "Толстовка Adidas ELEVATED3HOODIE Collegiate Navy", price: 7150 },
//   { id: 3, imagePath: "/src/assets/img/brands/adidas/adidas3.png", title: "Толстовка adidas LIGHTWZIPTRACK Night Indigo Collegiate Green White", price: 5990 },
//   { id: 4, imagePath: "/src/assets/img/brands/adidas/adidas4.png", title: "Кеды adidas 3MC COLLEGIATE NAVY FTWWHT GRETWO", price: 4490 },
// ]);

</script>

<template>
  <div class="favourites-page">
    <div v-if="!commonStore.loading" class="container">
      <div class="favourites-page__title">Мои избранные</div>

      <div 
        v-if="productsStore.favoritesProducts.length !== 0" 
        class="favourites-page__row"
      >
        <div class="favourites-page__column" v-for="product in productsStore.favoritesProducts" :key="product.id">
          <AppFavouriteProduct :item="product.product_id" :id-product="product.id"/>          
        </div>
      </div>

      <div 
        v-else
        class="favourites-page__placeholder"
      >
        Добавьте свой первый товар
      </div>

    </div>
    <div v-else class="container">
      Загрузка данных..
    </div>
  </div>
</template>

<style lang="scss" scoped>
@import '@/assets/scss/_variables.scss';
@import '@/assets/scss/_mixins.scss';
.favourites-page {
  padding: 40px 0;
}

.favourites-page__title {
  @include font(48px, 400, 60px);
  margin: 0 0 20px;
  @include for-size(tablet) {
    @include font(30px, 400, 1.2);
  }
}

.favourites-page__row {
  display: flex;
  justify-content: space-between;
  flex-wrap: wrap;
  margin: 30px -15px 0;
}

.favourites-page__placeholder {
  @include font(30px, 400, 1.2);
  margin-top: 50px;
  text-align: center;
}
.favourites-page__column {
  width: calc(100% / 4);
  padding: 15px;
  @include for-size(tablet) {
    width: calc(100% / 2);
  }
  @include for-size(mobile) {
    width: 100%;
  }
}
</style>