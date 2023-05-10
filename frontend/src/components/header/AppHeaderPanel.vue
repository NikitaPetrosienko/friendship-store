<script setup lang="ts">

</script>

<template>
  <div class="header-panel">
    <a
      class="header-panel__phone"
      href="tel: 8 (926) 473-47-68"
    >8 (926) 473-47-68</a>
    <div class="header-panel__links">
      <a href="#" class="header-panel__link header-panel__link_basket">Корзина</a>
      <a href="#" class="header-panel__link header-panel__link_favourites">Избранное</a>
      <a href="#" class="header-panel__link header-panel__link_login">Войти</a>
    </div>
  </div>
</template>

<style lang="scss" scoped>
@import '@/assets/scss/_variables.scss';
@import '@/assets/scss/_mixins.scss';
.header-panel {
  padding-left: 20px;
}
.header-panel__phone {
  display: block;
  @include font(18px, 400, 22px);
  color: $white;
}
.header-panel__links {
  display: flex;
  gap: 10px ;
}
.header-panel__link {
  font-size: 0;
  overflow: hidden;
  text-decoration: none;
  background-size: 100%;
  background-repeat: no-repeat;
  background-position: center;
}
.header-panel__link_basket {
  width: 39px;
  height: 40px;
  background-image: url('../../assets/img/basket.svg');
}
.header-panel__link_favourites {
  width: 52px;
  height: 44px;
  background-image: url('../../assets/img/favourites.svg');
}
.header-panel__link_login {
  width: 54px;
  height: 46px;
  background-image: url('../../assets/img/login.svg');
}
</style>