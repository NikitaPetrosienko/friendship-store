<script setup lang="ts">
import vInput from '@/components/input/v-input.vue';
import vTextarea from '@/components/input/v-textarea.vue';

import useVuelidate from '@vuelidate/core';
import { helpers, minLength, maxLength } from '@vuelidate/validators';

import { computed, ref } from 'vue';

const commentAuthor = ref('');
const commentText = ref('');

const submitForm = () => {
  const formData = {
    commentAuthor: commentAuthor.value,
    commentText: commentText.value,
  }
  console.log('submitForm: ', formData);
}

const rules = computed(() => ({
  commentAuthor: {
    minLength: helpers.withMessage('Минимальная длина: 3 символа', minLength(3))
  },
  commentText: {
    minLength: helpers.withMessage('Минимальная длина: 10 символов', minLength(10)),
    maxLength: helpers.withMessage('Максимальная длина: 100 символов', maxLength(100))
  },
}));

const v = useVuelidate(rules, { commentAuthor, commentText });

const handleClick = () => {
  console.log('Press Button');
}

</script>

<template>
  <form class="createcomment-form" action="#" method="POST" @submit.prevent="submitForm">
    <h3 class="createcomment-form__title">Добавить комментарий</h3>

    <v-input
      label="* Ваше имя"
      name="name"
      placeholder="Введите имя"
      width="100%"
      v-model:value="v.commentAuthor.$model"
      :error="v.commentAuthor.$errors" 
    />

    <v-textarea
      label="* Текст сообщения"
      name="text"
      placeholder="Введите текст комментария"
      v-model:value="v.commentText.$model"
      :error="v.commentText.$errors" 
    />

    <!-- <v-button label="Добавить комментарий" color="primary" size="medium" rounded type="submit" icon="pen-to-square"
      @click="handleClick" /> -->
      <button class="createcomment-form__btn" type="button" @click="handleClick">Добавить комментарий</button>

    <!-- <v-checkbox
      label="Согласен на обработку"
      id="isAgree"
      name="isAgree"
      v-model="isAgree"
    />

    <v-checkbox-group v-model="selectedHeroes" name="'heroes'" :options="listOfHeroes" /> -->

  </form>
</template>

<style lang="scss" scoped>
@import '@/assets/scss/_mixins.scss';
@import '@/assets/scss/_variables.scss';

.createcomment-form {
  margin-bottom: 30px; //ToDO
}

.createcomment-form__title {
  @include font(25px, 700, 24px);
  margin: 0 0 50px;
}

.createcomment-form__btn {
  @include button-reset;
}
.createcomment-form__btn {
  @include font(32px, 400, 1.2);
  display: inline-block;
  background-color: $blue;
  color: $white;
  text-decoration: none;
  padding: 10px 25px;
  @include for-size(tablet) {
    @include font(16px, 900, 1.2);
    padding: 8px 16px;
  }
}
</style>
