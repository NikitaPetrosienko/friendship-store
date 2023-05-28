<script setup lang="ts">
import vPicture from '@/components/picture/v-picture.vue';
import AppBreadcrumb from '@/components/breadcrumb/AppBreadcrumb.vue'

import { ref } from 'vue';

const albums = ref([
  { id: 1, imagePath: "/src/assets/img/albums/img1.png", title: "Maiami" },
  { id: 2, imagePath: "/src/assets/img/albums/img2.png", title: "San Fracisko" },
  { id: 3, imagePath: "/src/assets/img/albums/img3.png", title: "Virginia" },
  { id: 4, imagePath: "/src/assets/img/albums/img4.png", title: "Albukerke" },
]);

</script>

<template>
  <div class="albums-page">
    <div class="container">
      <AppBreadcrumb />
      <h1 class="albums-page__title">Фотоальбом</h1>
      <div class="albums-page__row">
        <div class="albums-page__column" v-for="item in albums" :key="item.id">
          <v-picture
            :class-container="'albums-page__picture'"
            :class-image="'albums-page__img'"
            :image-url="item.imagePath"
            :alt-text="item.title" 
          />
        </div>
      </div>
    </div>
  </div>
</template>

<style lang="scss" scoped>
@import '@/assets/scss/_variables.scss';
@import '@/assets/scss/_mixins.scss';
.albums-page {
}
.albums-page__title {
  @include font(48px, 400, 60px);
  margin: 8px 0 5px;
  @include for-size(tablet) {
    @include font(30px, 400, 1.2);
  }
}
.albums-page__row {
  display: flex;
  justify-content: space-between;
  flex-wrap: wrap;
  margin: 0 -16px;
}

.albums-page__column {
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