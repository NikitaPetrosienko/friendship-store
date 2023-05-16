<script lang="ts">
import { defineComponent } from 'vue';

// Import Swiper Vue.js components
import { Swiper, SwiperSlide } from 'swiper/vue';
import { Autoplay, Navigation, Pagination } from 'swiper';

// Import Swiper styles
import 'swiper/css';
import 'swiper/css/navigation';
import 'swiper/css/pagination';

export default defineComponent({
  components: {
    Swiper, SwiperSlide
  },
  setup() {

    return {
      modules: [Autoplay, Navigation, Pagination],
    };
  },
});
</script>


<template>
  <swiper class="home-page-swiper" :modules="modules" :pagination="{ clickable: true }" :slides-per-view="1" :autoplay="{
    delay: 3000,
    disableOnInteraction: false,
    pauseOnMouseEnter: true,
  }">
    <swiper-slide v-for="(elem, idx) in 5" :key="idx">
      <img class="home-page__img" src="../../assets/img/banner.png" alt="banner">
    </swiper-slide>
  </swiper>
</template>

<style lang="scss">

.swiper {
  width: 100%;
  height: 100%;
}

.swiper-slide {
  text-align: center;
  font-size: 18px;
  background: #fff;
  display: flex;
  justify-content: center;
  align-items: center;
}

.swiper-slide img {
  display: block;
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.swiper-pagination-bullet {
  width: 10px;
  height: 10px;
  background-color: #A9B0B4;
  opacity: 0.5;
  border-radius: 10px;
  margin: 0 8px;
  cursor: pointer;
}

.swiper-pagination-bullet-active {
  opacity: 1;
}
</style>