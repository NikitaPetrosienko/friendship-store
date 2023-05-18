<script setup lang="ts">
import { ref } from 'vue';
import { useRoute } from 'vue-router';

const brands = ref([
  { id: 1, imagePath: "src/assets/img/brands/img1.png" },
  { id: 2, imagePath: "src/assets/img/brands/img2.png" },
  { id: 3, imagePath: "src/assets/img/brands/img3.png" },
]);

const route = useRoute();

console.log('route: ', route.params);
 
</script>

<template>
  <div class="home-page-brands">
    <div class="container">
      <div class="home-page-brands__row">
        <div class="home-page-brands__column" v-for="brand in brands" :key="brand.id">
          <div class="home-page-brands__card">
            <img class="home-page-brands__img" :src="brand.imagePath" alt="brand">
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style lang="scss" scoped>
@import '@/assets/scss/_variables.scss';
@import '@/assets/scss/_mixins.scss';
.home-page-brands {
  padding-top: 40px;
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
  padding: 0 38px;
  @include for-size(tablet) {
    width: 100%;
    padding: 0 24px;
  }
}

.home-page-brands__column+.home-page-brands__column {
  @include for-size(tablet) {
    margin-top: 40px;
  }
}
.home-page-brands__card {
}
.home-page-brands__img {
}
</style>