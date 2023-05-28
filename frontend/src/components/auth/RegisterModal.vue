<script setup lang="ts">
import vInput from '@/components/input/v-input.vue';

import { computed, ref } from 'vue';

import useVuelidate from '@vuelidate/core';
import { helpers, minLength, email, sameAs } from '@vuelidate/validators';

import { useAuthStore } from '@/store/auth/auth';

const authStore = useAuthStore();

const userEmail = ref('');
const userPassword = ref('');
const confirmUserPassword = ref('');

const rules = computed(() => ({
  userEmail: {
    email: helpers.withMessage('Вы ввели неверный email', email),
  },
  userPassword: {
    minLength: helpers.withMessage('Минимальная длина: 8 сиволов', minLength(8))
  },
  confirmUserPassword: {
    sameAsPassword: helpers.withMessage('Пароли не совпадают', sameAs(userPassword.value))
  },
}));

const v = useVuelidate(rules, { userEmail, userPassword, confirmUserPassword });

const submitForm = () => {
  v.value.$touch()
  if (!v.value.$error) {
    authStore.registerUser({ email: userEmail.value, password: userPassword.value });
  }
}


</script>

<template>
  <div class="register-modal">
    <div class="register-modal__container">
      <router-link class="register-modal__link" to="/">
        <img class="register-modal__img" src="../../assets/img/logo.png" alt="Дружба Store" />
      </router-link>
      <form class="register-modal__form" action="#" @submit.prevent="submitForm">
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
        <v-input
          label="* Подтвердите пароль"
          name="password"
          type="password"
          placeholder="Подтвердите пароль"
          width="100%"
          v-model:value="v.confirmUserPassword.$model"
          :error="v.confirmUserPassword.$errors"
        />
        <router-link class="register-modal__link" to="/login">Уже зарегистрированы?</router-link>
        <button class="register-modal__button" type="submit">Зарегистрироваться</button>
      </form>
    </div>
  </div>
</template>

<style lang="scss" scoped>
@import '@/assets/scss/_variables.scss';
@import '@/assets/scss/_mixins.scss';
.register-modal {
  display: flex;
  align-items: center;
  justify-content: center;
  height: 100vh;
  background-color: $blue;
}

.register-modal__container {
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
.register-modal__link {
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

.register-modal__form {
  display: flex;
  flex-direction: column;
  justify-content: center;
}
.register-modal__img {
}

.register-modal__button {
  @include button-reset;
}
.register-modal__button {
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
.register-modal__button:hover {
  background-color: $blue;
  color: $white;
}

</style>