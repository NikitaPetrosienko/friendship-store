<script setup lang="ts">
import { useAuthStore } from '@/store/auth/auth';

const authStore = useAuthStore();

const logoutUser = () => {
  authStore.logoutUser();
}

</script>

<template>
  <div class="header-panel">
    <a
      class="header-panel__phone"
      href="tel: 8 (926) 473-47-68"
    >8 (926) 473-47-68</a>
    <div class="header-panel__links">
      <router-link
        class="header-panel__link header-panel__link_basket"
        to="/cart"
        >Корзина
      </router-link>

      <router-link
        class="header-panel__link header-panel__link_favourites"
        to="/favourites"
        >Избранное
      </router-link>

      <router-link
        v-if="!authStore.isUserLoggedIn"
        class="header-panel__link header-panel__link_login"
        to="/login"
        >Войти
      </router-link>

      <router-link
        v-else
        class="header-panel__link header-panel__link_login"
        to="/"
        @click="logoutUser"
        >Выйти
      </router-link>
    </div>
  </div>
</template>

<style lang="scss" scoped>
@import '@/assets/scss/_variables.scss';
@import '@/assets/scss/_mixins.scss';
.header-panel {
  display: flex;
  flex-direction: column;
  align-items: space-between;
  padding-left: 20px;
  @include for-size(tablet) { // ToDo
    padding-left: 0;
  }
}
.header-panel__phone {
  display: block;
  flex: 1 1 auto;
  @include font(18px, 400, 22px);
  text-decoration: none;
  color: $white;
  @include for-size(laptop-s) { // ToDo
    display: none;
  }
}
.header-panel__phone::before {
  content: url('../../assets/img/svg/phone.svg');
  margin-right: 16px;
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
  background-image: url('../../assets/img/svg/basket.svg');
  @include for-size(tablet) {
    width: 17px;
    height: 15px;
  }
}
.header-panel__link_favourites {
  width: 52px;
  height: 44px;
  background-image: url('../../assets/img/svg/favourites.svg');
  @include for-size(tablet) {
    width: 17px;
    height: 16px;
  }
}
.header-panel__link_login {
  width: 54px;
  height: 46px;
  background-image: url('../../assets/img/svg/login.svg');  
  @include for-size(tablet) {
    width: 19px;
    height: 18px;
  }
}
</style>