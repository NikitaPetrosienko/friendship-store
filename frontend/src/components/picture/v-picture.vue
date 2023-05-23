<script setup lang="ts">
import {
  defineProps, toRefs
} from 'vue';

interface IPropsPicture {
  imageUrl?: string,
  classContainer: string,
  classImage?: string,
}

const props = defineProps<IPropsPicture>();

const { imageUrl, classContainer, classImage } = toRefs(props);

</script>

<template>
  <div class="picture">
    <picture class="picture__container" :class="classContainer">
      <img class="picture__img" :class="classImage" :src="`${imageUrl}`" alt="img">
    </picture>
  </div>
</template>

<style lang="scss" scoped>
@import '@/assets/scss/_variables.scss';
@import '@/assets/scss/_mixins.scss';

.picture__container {
  position: relative;
  display: block;
}

.picture__img {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.home-page-brands__picture {
  padding-top: calc(357 / 345 * 100%);
}
.home-page-brands__img {

}
</style>
