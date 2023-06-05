<script setup lang="ts">
import AppBreadcrumb from '@/components/breadcrumb/AppBreadcrumb.vue'

import { ref } from 'vue';

const breadcrumbs = ref([
  {
    id: 1,
    title: 'Главная',
    url: '/'
  },
  {
    id: 2,
    title: 'Архив новостей',
    url: '/news/1'
  },
  {
    id: 3,
    title: 'NIKE SB Dunk Low Pro Laser Blue',
    url: '/news/1'
  },
]);

</script>

<template>
  <div class="news-page">
    <div class="container">
      <AppBreadcrumb :breadcrumbs="breadcrumbs"/>

      <div class="news-page__grid">
        <div>
          <h1>NIKE SB Dunk Low Pro Laser Blue</h1>
          <img src="../assets/img/news/img1.png" alt="news">
          <p>
            В 2020 году Nike SB провели довольно очевидную связь между своими любимыми Dunk и Air Max 90. Воспользовавшись растущей шумихой вокруг Данков, команда Nike SB привлекла дополнительное внимание к беговой обуви Air Max 90, которая в прошлом году праздновала свое 30-летие. Для тех, кто является поклонником Air Max, 2020 год стал невероятным годом для переизданий оригинальных цветов, но кто мог предположить, что они появятся на SB Dunk?
          </p>
        </div>
        <div>
          <p>Nike SB Dunk Low Pro “Laser Blue” — очередной релиз, вдохновленный моделью Nike Air Max 90.
            После того, как в прошлом году была выпущена расцветка SB Данков, вдохновленная классической моделью Nike Air Max 90 “Infrared”, еще одна классическая расцветка Air Max 90 “Laser Blue” была использована в качестве вдохновения для очередного релиза Nike SB Dunk Low.
          </p>
          <img src="../assets/img/news/img1.png" alt="news">
        </div>
      </div>

    </div>
  </div>
</template>

<style lang="scss" scoped>
@import '@/assets/scss/_variables.scss';
@import '@/assets/scss/_mixins.scss';

.news-page__grid {
  display: grid;
  grid-template-columns: 6fr 6fr;
  grid-gap: 20px;
  @include for-size(tablet) {
    grid-template-columns: 12fr;
  }
}

.news-page__grid h1 {
  @include font(48px, 400, 60px);
  color: $purple;
  margin: 8px 0 5px;

  @include for-size(tablet) {
    @include font(30px, 400, 1.2);
  }
}

.news-page__grid div:last-child{
  padding-top: 50px;
}

.news-page__grid img {
  width: 100%;
}

// .news-page__body p {
//   @include font(36px, 500, 43px);
//   color: $black;

//   @include for-size(tablet) {
//     @include font(16px, 400, 1.2);
//   }
// }
</style>