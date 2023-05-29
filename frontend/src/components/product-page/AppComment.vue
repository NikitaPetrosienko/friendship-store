<script setup lang="ts">

import { PropType } from 'vue';

import { IProductComment } from '@/store/products/products.interfaces';

const props = defineProps({
  item: {
    type: Object as PropType<IProductComment>,
    required: true,
  },
});

const formatDate = (dateString) => {
  const date = new Date(dateString);
  const options = { day: 'numeric', month: 'long', year: 'numeric' };
  return date.toLocaleDateString('ru-RU', options);
}

</script>

<template>
  <div class="comment">
    <div class="comment__header">
      <span class="comment__author">{{ item.name_user }}</span>
      <span class="comment__date">
        <fa class="comment__icon" icon="clock" /> {{ formatDate(item.created_at) }}
      </span>
    </div>
    <hr>
    <div class="comment__text">
      <p class="comment__info">
        {{ item.body }}
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
