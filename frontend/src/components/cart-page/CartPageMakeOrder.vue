<script setup lang="ts">

import { useOrdersStore } from '@/store/orders/orders';
const ordersStore = useOrdersStore();

const createOrder = () => {
  ordersStore.createOrder();
}

</script>

<template>
  <div class="cartpage-makeorder">
    <div class="cartpage-makeorder__row">
      <div class="cartpage-makeorder__column">
        <div class="cartpage-makeorder__title">Адрес доставки</div>
        <p>{{ ordersStore.order.district }}, {{ ordersStore.order.street }}, {{ ordersStore.order.house }}</p>
      </div>
      <div class="cartpage-makeorder__column">
        <div class="cartpage-makeorder__title">Получатель</div>
        <p>{{ ordersStore.order.first_name }} {{ ordersStore.order.last_name }} {{ ordersStore.order.phoneNumber }}</p>
      </div>
    </div>
    <div class="cartpage-makeorder__row">
      <div class="cartpage-makeorder__column cartpage-makeorder__column_button">
        <button 
          class="cartpage-makeorder__btn"
          @click="createOrder"
          >Оформить заказ
        </button>
      </div>
    </div>
  </div>
</template>

<style lang="scss" scoped>
@import '@/assets/scss/_variables.scss';
@import '@/assets/scss/_mixins.scss';
.cartpage-makeorder {
  padding-top: 60px;
}
.cartpage-makeorder__row {
  display: flex;
  margin: 0 -20px;
  @include for-size(tablet) {
    flex-wrap: wrap;
  }
}
.cartpage-makeorder__column {
  width: 50%;
  padding: 0 20px;
  @include for-size(tablet) {
    width: 100%;
  }
}

.cartpage-makeorder__column_button {
  width: 100%;
  padding: 0 20px;
  text-align: center;
  @include for-size(tablet) {
    text-align: left;
  }
}
.cartpage-makeorder__title {
  @include font(36px, 400, 1.2);
  margin-bottom: 10px;
  @include for-size(tablet) {
    @include font(20px, 800, 1.2);
  }
}

.cartpage-makeorder__btn {
  @include button-reset;
}
.cartpage-makeorder__btn {
  @include font(32px, 400, 1.2);
  display: inline-block;
  background-color: $blue;
  color: $white;
  text-decoration: none;
  padding: 10px 25px;
  margin-top: 50px;
  @include for-size(tablet) {
    @include font(16px, 900, 1.2);
    padding: 8px 16px;
  }
}
.cartpage-makeorder__btn::after {
  content: '>>';
  margin-left: 5px;
}
</style>