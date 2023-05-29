<script setup lang="ts">
import vInput from '@/components/input/v-input.vue';

import { ref } from 'vue';

const minPrice = ref('');
const maxPrice = ref('');

</script>

<template>
  <form class="products-form" action="#">
    
    <fieldset class="products-form__fieldset">
      <div class="products-form__legend">Цена:</div>
      <!-- <label class="products-form__label" for="priceMin">От</label>
      <input class="products-form__input" id="priceMin" type="number">
      

      <label class="products-form__label" for="priceMax">До</label>
      <input class="products-form__input" id="priceMax" type="number"> -->

      <v-input
        name="name"
        placeholder="100"
        type="number"
        width="100%"
        v-model:value="minPrice"
      />

      <v-input
        name="name"
        placeholder="99999"
        type="number"
        width="100%"
        v-model:value="maxPrice"
      />
    </fieldset>

    <fieldset class="products-form__fieldset">
      <label class="products-form__select-label" for="filterPrice">Сортировать по</label>
      <select class="products-form__select" id="filterPrice">
        <option class="products-form__option" value="increase">возрастание</option>
        <option class="products-form__option" value="decrease">убывание</option>
      </select>
  </fieldset>
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
</style>