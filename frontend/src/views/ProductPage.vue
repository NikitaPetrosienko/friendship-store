<script setup lang="ts">
import CreateCommentForm from '@/components/product-page/CreateCommentForm.vue';
import AppComment from '@/components/product-page/AppComment.vue';

</script>

<template>
  <div class="product-page">
    <div class="container">
      <div class="product-page__row">
        <div class="product-page__column product-page__column_picture">
          <img src="../assets/img/skateboards/img1.png" alt="skateboard">
        </div>
        <div class="product-page__column product-page__column_info">
          <h1 class="product-page__title">Дека Footwork Progress Universe fwsb-prguniverse (multi)</h1>
          <div class="product-page__price">2630.00р</div>
          <div class="product-page__status">В наличии</div>
          <div class="product-page__size">Размер: 8x31.5</div>
          
          <div class="product-page__buttons">
            <div class="product-page__btn-cart">
              <button class="product-page__btn" type="button">В корзину </button><span class="product-page__btn-count">0</span>
            </div>
            <button class="product-page__btn" type="button">В избранное</button>
            <button class="product-page__btn" type="button">Купить в один клик</button>
          </div>

          <div class="product-page__desc">
            <p class="product-page__text product-page__text_title">Описание</p>
            <p class="product-page__text">
              Поставка 2021 года.<br>
              - Бренд: Footwork.<br>
              - Конструкция: Progress.<br>
              - Размеры: 8 x 31.5 / 8.25 x 31.75<br>
              - Конкейв: Глубокий.<br>
              - Стикерпак из 15 наклеек в подарок.
            </p>
          </div>

        </div>
      </div>

      <div class="product-page__row">
        <div class="product-page__column">
          <CreateCommentForm />
        </div>
      </div>

      <div class="product-page__row">
        <div class="product-page__column">
          <div class="product-page__comments" v-if="true">
            <h3 class="product-page__text">Комментарии</h3>
            <AppComment
              v-for="comment in 4"
              :key="comment"
            />
          </div>
          <div class="product-page__comments-placeholder" v-else>Комментариев на данный момент нет</div>
        </div>
      </div>
    </div>
  </div>
</template>

<style lang="scss" scoped>
@import '@/assets/scss/_variables.scss';
@import '@/assets/scss/_mixins.scss';
.product-page {
  padding: 40px 0;
}
.product-page__row {
  display: flex;
  margin: 0 -18px;
  @include for-size(tablet) {
    flex-wrap: wrap;
  }
}
.product-page__column {
  width: 100%;
  padding: 0 18px;
}
.product-page__column_picture {
  flex: 0 0 auto;
  width: calc(100% / 12) * 5;
  @include for-size(tablet) {
    text-align: center;
    width: 100%;
  }
}
.product-page__column_info {
  width: calc(100% / 12) * 7;
  @include for-size(tablet) {
    width: 100%;
  }
}
.product-page__title {
  @include font(48px, 400, 60px);
  margin: 0 0 18px;
  @include for-size(tablet) {
    @include font(25px, 400, 1.2);
  }
}
.product-page__price {
  @include font(48px, 400, 60px);
  margin: 0 0 18px;
  @include for-size(tablet) {
    @include font(25px, 400, 1.2);
  }
}
.product-page__status {
  @include font(36px, 400, 45px);
  margin: 0 0 18px;
  @include for-size(tablet) {
    @include font(20px, 400, 1.2);
  }
}
.product-page__size {
  @include font(36px, 400, 45px);
  margin: 0 0 24px;
  @include for-size(tablet) {
    @include font(20px, 400, 1.2);
  }
}
.product-page__buttons {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
  margin-bottom: 40px;
}
.product-page__btn {
  @include button-reset;
}
.product-page__btn {
  flex: 0 0 auto;
  @include font(24px, 900, 28px);
  background-color: $blue;
  color: $white;
  padding: 8px 20px;
  @include for-size(tablet) {
    @include font(20px, 400, 1.2);
    padding: 6px 15px;
  }
}
.product-page__btn-cart {
  display: flex;
}
.product-page__btn-count {
  display: block;
  @include font(24px, 900, 28px);
  background-color: $blue;
  color: $white;
  padding: 8px;
  border-left: 1px solid #FFFFFF;
  @include for-size(tablet) {
    @include font(20px, 400, 1.2);
    padding: 6px 15px;
  }
}

.product-page__text {
  @include font(24px, 900, 28px);
  margin: 0 0 45px;
  @include for-size(tablet) {
    @include font(20px, 400, 1.2);
  }
}
.product-page__text_title {
  display: inline-block;
  padding-bottom: 10px;
  border-bottom: 2px solid $blue;
}

.product-page__comments-placeholder {
  text-align: center;
}
</style>