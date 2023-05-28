<script setup lang="ts">
import vInput from '@/components/input/v-input.vue';

import { computed, ref } from 'vue';

import useVuelidate from '@vuelidate/core';
import { helpers, minLength, maxLength, email, numeric } from '@vuelidate/validators';

const userEmail = ref('');
const userPassword = ref('');

const rules = computed(() => ({
  userEmail: {
    email: helpers.withMessage('Выввели неверный email', email),
  },
  userPassword: {
    minLength: helpers.withMessage('Минимальная длина: 3 символа', minLength(3))
  },
}));

const v = useVuelidate(rules, { userEmail, userPassword });

const submitForm = () => {
  console.log('submitForm: ', submitForm);
}

</script>

<template>
  <div class="login-modal">
    <div class="login-modal__container">
      <router-link class="login-modal__link" to="/">
        <img class="login-modal__img" src="../../assets/img/logo.png" alt="Дружба Store" />
      </router-link>
      <form class="login-modal__form" action="#" @submit.prevent="submitForm">
        <v-input
          label="* Ваше email"
          name="email"
          type="email"
          placeholder="Введите email"
          width="100%"
          v-model:value="v.userEmail.$model"
          :error="v.userEmail.$errors"
        />
        <v-input
          label="* Ваш пароль"
          name="password"
          type="password"
          placeholder="Введите пароль"
          width="100%"
          v-model:value="v.userPassword.$model"
          :error="v.userPassword.$errors"
        />
        <router-link class="login-modal__link" to="/register">Еще не регистрироваилсь?</router-link>
        <button class="login-modal__button" type="submit">Войти</button>
      </form>
    </div>
  </div>
</template>

<style lang="scss" scoped>
@import '@/assets/scss/_variables.scss';
@import '@/assets/scss/_mixins.scss';
.login-modal {
  display: flex;
  align-items: center;
  justify-content: center;
  height: 100vh;
  background-color: $blue;
}

.login-modal__container {
  background-color: $white;
  max-width: 600px;
  width: 100%;
  margin: 0 auto;
  box-shadow: 0px 4px 10px rgba(18, 118, 185, 0.25);
  border-radius: 15px;
  padding: 40px;
  @include for-size(tablet) {
    max-width: 600px;
  }
  @include for-size(mobile) {
      max-width: 300px;
  }
}
.login-modal__link {
  display: block;
  text-align: center;
  @include font(20px, 400, 1.2);
  color: $blue;
  text-decoration: none;
  padding: 10px 25px;
  @include for-size(tablet) {
    @include font(16px, 900, 1.2);
    padding: 8px 16px;
  }
}

.login-modal__form {
  display: flex;
  flex-direction: column;
  justify-content: center;
}
.login-modal__img {
}

.login-modal__button {
  @include button-reset;
}
.login-modal__button {
  @include font(32px, 400, 1.2);
  color: $blue;
  padding: 10px 25px;
  border: 2px solid $blue;
  border-radius: 8px;
  transition: all 0.2s ease;
  margin-top: 10px;
  @include for-size(tablet) {
    @include font(16px, 400, 1.2);
    padding: 8px 16px;
  }
}
.login-modal__button:hover {
  background-color: $blue;
  color: $white;
}

</style>