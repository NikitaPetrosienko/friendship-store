<script setup lang="ts">
import CartPageTable from '@/components/cart-page/CartPageTable.vue';

</script>

<template>
  <div class="cart-page">
    <div class="container">
      <div class="cart-page__row">
        <div class="cart-page__column">
          <CartPageTable />
        </div>
      </div>
    </div>
  </div>
</template>

<style lang="scss" scoped>
.cart-page {
  padding-top: 40px;
}
.cart-page__row {
  
}
.cart-page__column {
}
</style>