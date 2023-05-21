<script setup lang="ts">

import {
  defineProps, PropType,
} from 'vue';

import { useRouter } from '@nuxtjs/composition-api'

// interface IPropsComment {
//   id: number,
//   title: string,
//   publish_date: string,
//   tag: string,
//   text: string,
// }

// const props = defineProps({
//   item: {
//     type: Object as PropType<IPropsComment>,
//     required: true,
//   },
// });


</script>

<template>
  <div class="comment">
    <div class="comment__header">
      <span class="comment__author">Person name</span>
      <span class="comment__date">
        <fa class="comment__icon" icon="clock" /> {{ new Date().toLocaleString() }}
      </span>
    </div>
    <hr>
    <div class="comment__text">
      <p class="comment__info">
        Lorem ipsum dolor sit amet.
      </p>
    </div>

  </div>
</template>

<style lang="scss" scoped>
@import '@/assets/scss/_mixins.scss';
@import '@/assets/scss/_variables.scss';

.comment {
  box-shadow: 0 2px 12px 0 rgb(0 0 0 / 10%);
  border-radius: 16px;
  padding: 15px;
}

.comment+.comment {
  margin-top: 15px;
}

.comment__header {
  display: flex;
  justify-content: space-between;
}

.comment__author {
  @include font(16px, 400, 24px);
}

.comment__date {
  @include font(14px, 400, 24px);
}

.comment__info {
  @include font(16px, 400, 24px);
  white-space: pre-line;
}

.comment__icon {
  width: 18px;
  height: 18px;
}
</style>
