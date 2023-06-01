<script setup lang="ts">
import AppProductsForm from '@/components/home-page/product/AppProdutctsForm.vue';
import AppProduct from '@/components/home-page/product/AppProduct.vue';

import { watch } from 'vue';
import { useRoute } from 'vue-router';

const route = useRoute();

import { useProductsStore } from '@/store/products/products';
import { useCommonStore } from '@/store/common/common';

const productsStore = useProductsStore();
const commonStore = useCommonStore();

// const productsMock = ref([
//   { id: 1, imagePath: "/src/assets/img/brands/adidas/adidas1.jpeg", title: "Кеды Adidas Busenitz Vulc II Core Black FTWWHT VIVRED", price: 6700 },
//   { id: 2, imagePath: "/src/assets/img/brands/adidas/adidas2.jpeg", title: "Толстовка Adidas ELEVATED3HOODIE Collegiate Navy", price: 7150 },
//   { id: 3, imagePath: "/src/assets/img/brands/adidas/adidas3.png", title: "Толстовка adidas LIGHTWZIPTRACK Night Indigo Collegiate Green White", price: 5990 },
//   { id: 4, imagePath: "/src/assets/img/brands/adidas/adidas4.png", title: "Кеды adidas 3MC COLLEGIATE NAVY FTWWHT GRETWO", price: 4490 },
// ]);

if (route.query.brand) {
  // console.log("route.query.brand: ", route.query.brand);
  productsStore.fetchProductsByBrand(route.query.brand);
}
if (route.query.category) {
  // console.log("route.query.category: ", route.query.category);
  productsStore.fetchProductsByCategory(route.query.category);
}

watch(() => route.query.brand, (newValue) => {
    productsStore.fetchProductsByBrand(newValue);
  }
);

watch(() => route.query.category,(newValue) => {
    productsStore.fetchProductsByCategory(newValue);
  }
);

</script>

<template>
  <div class="homepage-products" id="products">
    <div v-if="!commonStore.loading" class="container">
      <div v-if="route.query.brand" class="homepage-products__title">{{ route.query.brand }}</div>
      <div v-else class="homepage-products__title">Продукты</div>
      
      <AppProductsForm />

      <div class="homepage-products__row">
        <div class="homepage-products__column" v-for="product in productsStore.products" :key="product.id">
          <AppProduct :item="product"/>
        </div>
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
.homepage-products {
  padding: 40px 0;
}

.homepage-products__title {
  @include font(48px, 400, 60px);
  margin: 0 0 20px;
  @include for-size(tablet) {
    @include font(30px, 400, 1.2);
  }
}

.homepage-products__row {
  display: flex;
  flex-wrap: wrap;
  margin: 30px -15px 0;
}
.homepage-products__column {
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