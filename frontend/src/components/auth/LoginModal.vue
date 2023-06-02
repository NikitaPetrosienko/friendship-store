<script setup lang="ts">
import vInput from '@/components/input/v-input.vue';

import { computed, ref } from 'vue';

import useVuelidate from '@vuelidate/core';
import { helpers, minLength, email } from '@vuelidate/validators';

import { useAuthStore } from '@/store/auth/auth';
import { useCommonStore } from '@/store/common/common';

const authStore = useAuthStore();
const commonStore = useCommonStore();

const userEmail = ref('');
const userPassword = ref('');

const rules = computed(() => ({
  userEmail: {
    email: helpers.withMessage('Вы ввели неверный email', email),
  },
  userPassword: {
    minLength: helpers.withMessage('Минимальная длина: 8 символов', minLength(8))
  },
}));

const v = useVuelidate(rules, { userEmail, userPassword });

const submitForm = () => {
  v.value.$touch()
  if (!v.value.$error) {
    authStore.loginUser({ email: userEmail.value, password: userPassword.value });
  }
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
          class="login-modal__input"
          label="* Ваше email"
          name="email"
          type="email"
          placeholder="Введите email"
          width="100%"
          v-model:value="v.userEmail.$model"
          :error="v.userEmail.$errors"
        />
        <v-input
          class="login-modal__input"
          label="* Ваш пароль"
          name="password"
          type="password"
          placeholder="Введите пароль"
          width="100%"
          v-model:value="v.userPassword.$model"
          :error="v.userPassword.$errors"
        />
        <router-link class="login-modal__link" to="/register">Еще не регистрироваилсь?</router-link>
        <button class="login-modal__button" :disabled="commonStore.loading" type="submit">Войти</button>
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
      max-width: 330px;
  }
}
.login-modal__link {
  display: block;
  text-align: center;
  @include font(20px, 400, 1.2);
  color: $blue;
  text-decoration: none;
  padding: 10px 25px;
  margin: 20px 0;
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

.login-modal__input + .login-modal__input {
  margin-top: 50px;
}
.login-modal__img {
}

.login-modal__button {
  @include button-reset;
}
.login-modal__button {
  @include font(32px, 400, 1.2);
  color: $white;
  background-color: $blue;
  padding: 10px 25px;
  border-radius: 8px;
  transition: all 0.3s ease;
  @include for-size(tablet) {
    @include font(16px, 400, 1.2);
    padding: 8px 16px;
  }
}
.login-modal__button:hover {
  opacity: 0.8;
}

.login-modal__button:disabled {
  cursor: not-allowed;
  opacity: 1;
  background: #eee;
  border-color: #ddd;
  color: #999;
}

</style>