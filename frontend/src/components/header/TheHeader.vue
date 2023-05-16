<script setup lang="ts">
import AppHeaderLinks from '@/components/header/AppHeaderLinks.vue'
import AppHeaderPanel from '@/components/header/AppHeaderPanel.vue'
import AppHeaderBurger from '@/components/header/AppHeaderBurger.vue'

</script>

<template>
  <header class="header">
    <div class="container header__container header__container_desktop">

      <router-link class="header__logo-link" to="/">
        <img class="header__logo-img" src="../../assets/img/logo.png" alt="Дружба Store" />
      </router-link>

      <AppHeaderLinks />

      <AppHeaderPanel />

    </div>

    <div class="container header__container header__container_mobile">

      <AppHeaderPanel />

        <router-link class="header__logo-link" to="/">
          <img class="header__logo-img" src="../../assets/img/logo.png" alt="Дружба Store" />
        </router-link>

      <AppHeaderBurger />

    </div>
  </header>
</template>

<style lang="scss" scoped>
@import '@/assets/scss/_variables.scss';
@import '@/assets/scss/_mixins.scss';

.header {
  background-color: $blue;
  padding: 27px 0 37px;
}

.header__container {
  display: flex;
}

.header__container_desktop {
  @include for-size(laptop-s) {
    display: none;
  }
}

.header__container_mobile {
  display: none;

  @include for-size(laptop-s) {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 5px;
  }
}
.header__logo-link {
  display: block;
  flex: 0 1 auto;
}
.header__logo-img {
  display: block;
  margin-right: 20px;
  @include for-size(tablet) { //ToDo
    width: 170px;
    height: 60px;
  }
}</style>