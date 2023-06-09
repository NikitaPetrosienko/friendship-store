<script setup lang="ts">
import vInput from '@/components/input/v-input.vue';

import { computed, ref, watch } from 'vue';
// import { useRoute } from 'vue-router';

// const route = useRoute();

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
// if (route.query.code) {
//   authStore.loginUserByVk({ code: route.query.code });
// }

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
        <router-link class="login-modal__link" to="/register">Еще не регистрировались?</router-link>

        <!-- <a class="login-modal__vk" href="https://oauth.vk.com/authorize?client_id=51651546&display=page&redirect_uri=http://127.0.0.1:5173/&scope=friends&response_type=code&v=5.131">
          <svg width="30" height="30" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M15.0729 2H8.9375C3.33331 2 2 3.33331 2 8.92706V15.0625C2 20.6666 3.32294 22 8.92706 22H15.0625C20.6667 22 22 20.6771 22 15.0729V8.9375C22 3.33331 20.6771 2 15.0729 2ZM18.1458 16.2708H16.6875C16.1354 16.2708 15.9688 15.8229 14.9792 14.8333C14.1146 14 13.75 13.8958 13.5312 13.8958C13.2292 13.8958 13.1458 13.9791 13.1458 14.3958V15.7083C13.1458 16.0625 13.0312 16.2708 12.1042 16.2708C11.2046 16.2104 10.3322 15.9371 9.55888 15.4735C8.78557 15.0098 8.13346 14.3691 7.65625 13.6041C6.52336 12.194 5.73511 10.5391 5.35419 8.77081C5.35419 8.55206 5.4375 8.35413 5.85419 8.35413H7.3125C7.6875 8.35413 7.82294 8.52081 7.96875 8.90625C8.67706 10.9896 9.88544 12.8021 10.375 12.8021C10.5625 12.8021 10.6458 12.7188 10.6458 12.25V10.1041C10.5833 9.125 10.0625 9.04163 10.0625 8.6875C10.0694 8.59407 10.1124 8.50699 10.1824 8.44475C10.2524 8.3825 10.3439 8.35 10.4375 8.35413H12.7292C13.0417 8.35413 13.1458 8.51038 13.1458 8.88538V11.7812C13.1458 12.0938 13.2812 12.1979 13.375 12.1979C13.5625 12.1979 13.7083 12.0938 14.0521 11.75C14.7907 10.8492 15.3943 9.84559 15.8438 8.77081C15.8896 8.64149 15.9766 8.53074 16.0913 8.4555C16.2061 8.38025 16.3423 8.34465 16.4792 8.35413H17.9375C18.375 8.35413 18.4688 8.57288 18.375 8.88538C17.8444 10.0737 17.1878 11.2017 16.4167 12.25C16.2604 12.4896 16.1979 12.6146 16.4167 12.8958C16.5625 13.1146 17.0729 13.5416 17.4167 13.9479C17.9167 14.4466 18.3318 15.0237 18.6458 15.6562C18.7708 16.0625 18.5625 16.2708 18.1458 16.2708Z" fill="blue"/>
          </svg>
        </a> -->
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

.login-modal__vk {
  text-align: center;
  margin: 20px 0;
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