<script setup lang="ts">

</script>

<template>
  <div class="cartpage-makeorder">
    <div class="cartpage-makeorder__row">
      <div class="cartpage-makeorder__column">
        <div class="cartpage-makeorder__title">Адрес доставки</div>
        <p>г. Мухосранск, Ул. Пушкина, дом Колотушкина</p>
      </div>
      <div class="cartpage-makeorder__column">
        <div class="cartpage-makeorder__title">Получатель</div>
        <p>Аркадий Паровозов 8(999)-228-13-12</p>
      </div>
    </div>
    <div class="cartpage-makeorder__row">
      <div class="cartpage-makeorder__column cartpage-makeorder__column_button">
        <router-link class="cartpage-makeorder__btn" to="/make-order">Далее</router-link>
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