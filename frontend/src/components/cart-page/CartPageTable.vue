<script setup lang="ts">
import { ref } from 'vue';

// const mockCartList = ref([
//   {
//     id: 1,
//     title: 'Дека Footwork Progress Universe fwsb-prguniverse (multi)',
//     count: 1,
//     imageURL: 'assets/img/skateboards/img1.png',
//     totalPrice: '2630.00' 
//   }
// ]);


import { useProductsStore } from '@/store/products/products';
import { useAuthStore } from '@/store/auth/auth';
import { useCartStore } from '@/store/cart/cart';

const productsStore = useProductsStore();
const authStore = useAuthStore();
const cartStore = useCartStore();

cartStore.getUserCart({ token: authStore.user.id });

</script>

<template>
   <table class="cartpage-table">
    <thead>
      <tr>
        <th class="cartpage-table__th">Товар</th>
        <th class="cartpage-table__th">Кол-во</th>
        <th class="cartpage-table__th">Итого</th>
      </tr>
    </thead>
    <tbody>
      <tr 
        v-for="item in cartStore.userCart.basket"
        :key="item.id"
      >
        <td class="cartpage-table__td cartpage-table__td_main-info">
          <img 
            class="cartpage-table__img"
            :src="item.product_id.main_image" 
            alt="cart-product"
          >
          <div class="cartpage-table__title">{{ item.product_id.product_name }}</div>
        </td>
        <td class="cartpage-table__td cartpage-table__td-counters cartpage-table__td_main-info">
          <button class="cartpage-table__control cartpage-table__control_decrease"></button>
          <span class="cartpage-table__product-count">{{ item.quantity }}</span>
          <button class="cartpage-table__control cartpage-table__control_increase"></button>
        </td>
        <td class="cartpage-table__td cartpage-table__td_main-info">
          <div class="cartpage-table__product-price">{{ item.quantity * parseInt(item.product_id.price) }}р</div>
        </td>
      </tr>

      <tr>
        <td class="cartpage-table__td cartpage-table__delivery-info">Доставка</td>
        <td class="cartpage-table__td cartpage-table__delivery-info"></td>
        <td class="cartpage-table__td cartpage-table__delivery-info">300.00 &#8381;</td>
      </tr>

      <tr>
        <td class="cartpage-table__td cartpage-table__total-price cartpage-table__td_extra-info" colspan="2">Сумма заказа: {{ cartStore.userCart.total_price }} &#8381;</td>
        <td class="cartpage-table__td cartpage-table__td_extra-info">
          <router-link class="cartpage-table__btn" to="/form">Далее</router-link>
        </td>
      </tr>
    </tbody>
  </table>
</template>

<style lang="scss" scoped>
@import '@/assets/scss/_variables.scss';
@import '@/assets/scss/_mixins.scss';
.cartpage-table {
  width: 100%;
  border-collapse: collapse;
  text-align: center;
}
.cartpage-table__th {
  @include font(38px, 900, 1.2);
  text-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
  @include for-size(tablet) {
    @include font(20px, 900, 1.2);
  }
}
.cartpage-table__td {
  // border: 1px solid grey;
}

.cartpage-table__td {
  width: calc(100% / 3);
}

.cartpage-table__td_main-info {
  padding-bottom: 30px;
}

.cartpage-table__td_extra-info {
  padding-top: 30px;
}
.cartpage-table__img {

}
.cartpage-table__td-counters {
  vertical-align: middle; // ToDO
}
.cartpage-table__control {
  @include button-reset;
}
.cartpage-table__control {
  display: inline-block;
  @include font(36px, 400, 1.2);
  @include for-size(tablet) {
    @include font(20px, 900, 1.2);
  }
}

.cartpage-table__control:hover {
  background-color: rgba(128, 128, 128, 0.15); //ToDo
}
.cartpage-table__control_decrease::before {
  content: '-';
}
.cartpage-table__control_increase::before {
  content: '+';
}
.cartpage-table__product-count {
  @include font(36px, 400, 1.2);
  margin: 0 10px;
  @include for-size(tablet) {
    @include font(20px, 900, 1.2);
  }
}
.cartpage-table__product-price {
  @include font(49px, 400, 1.2);
  @include for-size(tablet) {
    @include font(20px, 900, 1.2);
  }
}
.cartpage-table__delivery-info {
  @include font(32px, 400, 1.2);
  padding: 30px 0;
  border-top: 1px solid $blue;
  border-bottom: 1px solid $blue;
  @include for-size(tablet) {
    @include font(16px, 900, 1.2);
  }
}
.cartpage-table__total-price {
  @include font(32px, 400, 1.2);
  padding: 15px;
  @include for-size(tablet) {
    @include font(16px, 900, 1.2);
  }
}
.cartpage-table__btn {
  @include font(32px, 400, 1.2);
  display: inline-block;
  background-color: $blue;
  color: $white;
  text-decoration: none;
  padding: 10px 25px;
  @include for-size(tablet) {
    @include font(16px, 900, 1.2);
    padding: 8px 16px;
  }
}
.cartpage-table__btn::after {
  content: '>>';
  margin-left: 5px;
}
</style>