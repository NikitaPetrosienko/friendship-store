<script setup lang="ts">
import vPicture from '@/components/picture/v-picture.vue';

import { PropType } from 'vue';

import { INews } from '@/store/news/news.interfaces';

const props = defineProps({
  item: {
    type: Object as PropType<INews>,
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
  <div class="news">
    <div class="news__body">
      <v-picture :class-container="'news__picture'" :class-image="'news__img'" :image-url="item.main_image"
        :alt-text="item.title" />
    </div>

    <div class="news__footer">
      <router-link :to="`/news/${1}`" class="news__link">
        <div class="news__title">{{ formatDate(item.date) }}</div>
        <div class="news__title">{{ item.title }}</div>
      </router-link>
    </div>
  </div>
</template>

<style lang="scss" scoped>
@import '@/assets/scss/_variables.scss';
@import '@/assets/scss/_mixins.scss';

.news {
  position: relative;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  height: 100%;
  background-color: $blue;
}
.news__body {
  flex: 1 1 auto;
}
.news__link {
  display: inline-block;
  vertical-align: top;
  max-width: 100%;
  @include font(24px, 400, 30px);
  text-decoration: none;
  width: 100%;
  color: $white;
  overflow-wrap: break-word;
  text-decoration: none;
  padding: 15px;
  
  @include for-size(tablet) {
    @include font(16px, 400, 1.2);
  }
}

.news__link::after {
  content: '';
  position: absolute;
  width: 100%;
  height: 100%;
  top: 0;
  left: 0;
}
</style>