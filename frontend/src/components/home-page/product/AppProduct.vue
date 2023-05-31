<script setup lang="ts">
import vPicture from '@/components/picture/v-picture.vue';

import { PropType } from 'vue';

import { IProduct } from '@/store/products/products.interfaces';

const props = defineProps({
  item: {
    type: Object as PropType<IProduct>,
    required: true,
  },
});

</script>

<template>
  <div class="product">
    <div class="product__body">
      <v-picture
        :class-container="'product__picture'"
        :class-image="'product__img'"
        :image-url="item.main_image"
        :alt-text="item.product_name"
      />
      <div class="product__card-title">{{ item.product_name }}</div>
    </div>

    <div class="product__footer">
      <div class="product__card-title">{{ item.price }} &#8381;</div>
      <router-link 
        :to="{
          name: 'ProductPage',
          params: { category: `${item.category.category_name}`, id: `${item.model}`, }
        }"
        class="product__link"
      ></router-link>
    </div>
  </div>
</template>

<style lang="scss" scoped>
@import '@/assets/scss/_variables.scss';
@import '@/assets/scss/_mixins.scss';
.product {
  position: relative;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  height: 100%;
}

.product__body {
  flex: 1 1 auto;
}
.product__link {
  @include font(24px, 400, 30px);
  display: inline-block;
  vertical-align: top;
  width: 100%;
  height: 1px;
  max-width: 100%;
  color: inherit;
  background-color: $blue;
  margin-top: 34px;
  text-decoration: none;
  overflow-wrap: break-word;
}

.product__link::after {
  content: '';
  position: absolute;
  width: 100%;
  height: 100%;
  top: 0;
  left: 0;
}
.product__card-title {
  margin-top: 24px;
}
</style>