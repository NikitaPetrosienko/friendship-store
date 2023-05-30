<script setup lang="ts">
import vPicture from '@/components/picture/v-picture.vue';
import AppBreadcrumb from '@/components/breadcrumb/AppBreadcrumb.vue';

import { ref } from 'vue';

import { useAlbumsStore } from '@/store/albums/albums';

const albumsStore = useAlbumsStore();

albumsStore.fetchAlbums();

// const mockAlbums = ref([
//   { id: 1, image: "/src/assets/img/albums/img1.png"},
//   { id: 2, image: "/src/assets/img/albums/img2.png" },
//   { id: 3, image: "/src/assets/img/albums/img3.png"},
//   { id: 4, image: "/src/assets/img/albums/img4.png"},
// ]);

const breadcrumbs = ref([
  {
    id: 1,
    title: 'Главная',
    url: '/'
  },
  {
    id: 2,
    title: 'Фотоальбом',
    url: '/albums'
  },
]);

</script>

<template>
  <div class="albums-page">
    <div class="container">

      <AppBreadcrumb :breadcrumbs="breadcrumbs"/>
      
      <h1 class="albums-page__title">Фотоальбом</h1>
      <div class="albums-page__row">
        <div class="albums-page__column" v-for="album in albumsStore.albums" :key="album.id">
          <v-picture
            :class-container="'albums-page__picture'"
            :class-image="'albums-page__img'"
            :image-url="album.image"
            alt-text="album" 
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