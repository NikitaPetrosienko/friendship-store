<script setup lang="ts">
import AppNews from '@/components/home-page/news/AppNews.vue';

import { ref } from 'vue';

import { useNewsStore } from '@/store/news/news';

const newsStore = useNewsStore();
newsStore.fetchNews();

// const newsMock = ref([
//   { id: 1, imagePath: "/src/assets/img/news/img1.png", title: "NIKE SB Dunk Low Pro Laser Blue" },
//   { id: 2, imagePath: "/src/assets/img/news/img2.png", title: "Вселенские скидки" },
//   { id: 3, imagePath: "/src/assets/img/news/img3.png", title: "Работа в нерабочие дни" },
//   { id: 4, imagePath: "/src/assets/img/news/img4.png", title: "NIKE SB Dunk Low Pro Laser Blue" },
//   { id: 5, imagePath: "/src/assets/img/news/img5.png", title: "Вселенские скидки" },
//   { id: 6, imagePath: "/src/assets/img/news/img6.png", title: "Работа в нерабочие дни" },
// ]);

</script>

<template>
  <div class="homepage-news">
    <div class="homepage-news__title">Архив новостей</div>
    <div class="homepage-news__row">
      <div class="homepage-news__column" v-for="newsItem in newsStore.news" :key="newsItem.id">
        <AppNews :item="newsItem"/>
      </div>
    </div>
  </div>
</template>

<style lang="scss" scoped>
@import '@/assets/scss/_variables.scss';
@import '@/assets/scss/_mixins.scss';
.homepage-news {
  padding-top: 40px;
}
.homepage-news__title {
  @include font(48px, 400, 60px);
  margin: 8px 0 5px;
  @include for-size(tablet) {
    @include font(30px, 400, 1.2);
  }
}
.homepage-news__row {
  display: flex;
  flex-wrap: wrap;
  margin: 0 -16px;
}
.homepage-news__column {
  width: calc(100% / 3);
  padding: 16px;
  @include for-size(tablet) {
    width: calc(100% / 2);
  }
  @include for-size(mobile) {
    width: 100%;
  }
}
</style>