<script setup lang="ts">
import vInput from '@/components/input/v-input.vue';

import { reactive, watch } from 'vue';

import { useRoute } from 'vue-router';

const route = useRoute();

import { useProductsStore } from '@/store/products/products';

const productsStore = useProductsStore();

const filtersConfig = reactive({
  minPrice: productsStore.filters.minPrice,
  maxPrice: productsStore.filters.maxPrice,
  sortStatus: productsStore.filters.sortStatus
});

watch(filtersConfig, (newNumber, oldNumber) => {
  if (filtersConfig.minPrice < 0) {
    filtersConfig.minPrice = 1;
  }
  if (!isNaN(parseInt(filtersConfig.minPrice))) {
    productsStore.filters.minPrice = parseInt(filtersConfig.minPrice);
  }

  if (!isNaN(parseInt(filtersConfig.maxPrice))) {
    productsStore.filters.maxPrice = parseInt(filtersConfig.maxPrice);
  }

  productsStore.filters.sortStatus = filtersConfig.sortStatus;

  if (route.query.brand) {
    productsStore.fetchProductsByBrand(route.query.brand);
  }
  if (route.query.category) {
    productsStore.fetchProductsByCategory(route.query.category);
  }

});


</script>

<template>
  <form class="products-form" action="#">
    
    <fieldset class="products-form__fieldset">
      <div class="products-form__legend">Цена:</div>
      <!-- <label class="products-form__label" for="priceMin">От</label>
      <input class="products-form__input" id="priceMin" v-model="filtersConfig.minPrice" type="number">
      

      <label class="products-form__label" for="priceMax">До</label>
      <input class="products-form__input" id="priceMax" v-model="filtersConfig.maxPrice" type="number"> -->
      
      <v-input
        name="name"
        placeholder="100"
        type="number"
        width="100%"
        v-model:value="filtersConfig.minPrice"
      />

      <v-input
        name="name"
        placeholder="99999"
        type="number"
        width="100%"
        v-model:value="filtersConfig.maxPrice"
      />
    </fieldset>

    <fieldset class="products-form__fieldset">
      <label class="products-form__select-label" for="filterPrice">Сортировать по</label>
      <select class="products-form__select" id="filterPrice" v-model="filtersConfig.sortStatus">
        <option class="products-form__option" value="incr">возрастание</option>
        <option class="products-form__option" value="decr">убывание</option>
      </select>
    </fieldset>

    <div class="products-form__line"></div>
  </form>
</template>

<style lang="scss" scoped>
@import '@/assets/scss/_variables.scss';
@import '@/assets/scss/_mixins.scss';
.products-form {
  display: flex;
  align-items: center;
  flex-wrap: wrap;
  gap: 20px;
  justify-content: space-between;
}
.products-form__legend {
  @include font(24px, 500, 1.2);
  text-transform: uppercase;
}
.products-form__fieldset {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 0;
  margin: 0;
  border: 0;
}
.products-form__label {
  @include font(24px, 500, 1.2);
  text-transform: lowercase;
  display: inline-block;
  max-width: 100%;
}

.products-form__input {
  @include input-reset;
}

.products-form__input {
  height: 40px;
  width: 115px;
  padding: 0 10px;
  border: 1px solid $blue;
  border-radius: 7px;
}

.products-form__select-label {
  @include font(24px, 500, 1.2);
  display: inline-block;
  text-transform: uppercase;
  white-space:  nowrap;
  @include for-size(tablet) {
    @include font(16px, 400, 1.2);
  }
}
.products-form__select {
  @include select-reset;
}
.products-form__select {
  @include font(16px, 400, 17px);
  width: auto;  
  outline: 0px;
  vertical-align: baseline;
}

.products-form__line {
  width: 100%;
  background-color: $blue;
  height: 1px;
}
</style>