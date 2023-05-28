<script setup lang="ts">
import vPicture from '@/components/picture/v-picture.vue';
import HomePageNews from '@/components/home-page/HomePageNews.vue';

import { ref } from 'vue';

import { useBrandsStore } from '@/store/brands/brands';

const brandsStore = useBrandsStore();
brandsStore.fetchBrands();

</script>

<template>
  <div class="home-page-brands">
    <div class="container">

      <div class="home-page-brands__row">
        <div class="home-page-brands__column" v-for="brand in brandsStore.brands" :key="brand.id">
          <div class="home-page-brands__card">
            <router-link :to="{ name: 'HomePageProducts', params: { brand: `${brand.barnd_name}` }}" class="home-page-brands__link">
              <v-picture
                :class-container="'home-page-brands__picture'"
                :class-image="'home-page-brands__img'"
                :image-url="brand.image"
                :alt-text="brand.barnd_name"
              />
            </router-link>
          </div>
        </div>
      </div>

      <HomePageNews />
      
    </div>
  </div>
</template>

<style lang="scss" scoped>
@import '@/assets/scss/_variables.scss';
@import '@/assets/scss/_mixins.scss';
.home-page-brands {
  padding: 40px 0;
}
.home-page-brands__row {
  display: flex;
  justify-content: flex-start;
  flex-wrap: wrap;
  margin: 0 -38px;
  @include for-size(tablet) {
    margin: 0 -24px;
  }
}
.home-page-brands__column {
  width: calc(100% / 3);
  padding: 38px;
  @include for-size(tablet) {
    width: calc(100% / 2);
    padding: 24px;
  }
  @include for-size(mobile) {
    width: 100%;
  }
}
.home-page-brands__card {
}
.home-page-brands__img {
}
</style>