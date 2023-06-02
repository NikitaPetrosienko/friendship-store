<script setup lang="ts">
import vPicture from '@/components/picture/v-picture.vue';

import { PropType } from 'vue';

import { IProduct } from '@/store/products/products.interfaces';

const props = defineProps({
  item: {
    type: Object as PropType<IProduct>,
    required: true,
  },
  idProduct: {
    type: String,
    required: true
  }
});

import { useProductsStore } from '@/store/products/products';

const productsStore = useProductsStore();

const deleteFavourite = (productId) => {
  productsStore.deleteFavouriteProduct({ id: productId });
}

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
      <router-link
        :to="{
          name: 'ProductPage',
          params: { category: `${item.category.category_name}`, id: `${item.model}`, }
        }"
        class="product__card-title"
        >{{ item.product_name }}
      </router-link>
    </div>

    <div class="product__footer">
      <div class="product__card-price">{{ item.price }} &#8381;</div>
      <button class="favourites-page__btn" type="button" @click="deleteFavourite(idProduct)">Удалить из избранного</button>
    </div>
  </div>
</template>

<style lang="scss" scoped>
@import '@/assets/scss/_variables.scss';
@import '@/assets/scss/_mixins.scss';

.product {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  height: 100%;
}

.product__body {
  position: relative;
  flex: 1 1 auto;
}

.product__card-title {
  display: inline-block;
  vertical-align: top;
  max-width: 100%;
  @include font(24px, 400, 30px);
  color: inherit;
  margin-top: 34px;
  overflow-wrap: break-word;
  text-decoration: none;
}

.product__card-title::after {
  content: '';
  position: absolute;
  width: 100%;
  height: 100%;
  top: 0;
  left: 0;
}

.product__card-price {
  @include font(24px, 400, 30px);
  margin-top: 24px;
}

.favourites-page__btn {
  @include button-reset;
}

.favourites-page__btn {
  @include font(18px, 900, 28px);
  background-color: $danger;
  color: $white;
  padding: 8px 20px;
  margin-top: 24px;
  @include for-size(tablet) {
    @include font(16px, 400, 1.2);
    padding: 6px 15px;
  }
}
</style>