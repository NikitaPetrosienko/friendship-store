<script setup lang="ts">
import AppBreadcrumb from '@/components/breadcrumb/AppBreadcrumb.vue'

</script>

<template>
  <div class="aboutus-page">
    <div class="container">
      <AppBreadcrumb />
      <h1 class="aboutus-page__title">О магазине</h1>
    </div>

    <div class="aboutus-page__body">
      <div class="container">
        <p>Команда скейтшопа ДРУЖБА приветствует тебя и предлагает окунуться в мир скейтбординга и всего, что его окружает.</p>
        <p>Открыв свои двери в 2005 году, мы по сей день продолжаем бороться за распространение скейтбординга по всей планете, да что там — по всей России! За это время нашими клиентами были представители всех регионов России, а также многих стран ближнего и дальнего зарубежья, соседних планет и галактик. Но при этом мы всегда оставались небольшим локальным скейтшопом и уверены, что именно это позволяет нам наладить доверительные дружеские отношения с нашими клиентами.
        </p>
        <p>Ведь скейтбординг — не про большие деньги, крупные сети, гигантские моллы и модные бутики. Для нас скейтбординг — это фан, прикол и хорошее расслабленное настроение, а не серьезный олимпийский вид спорта с судьями и баллами. Это катание на парковках со своими друзьями, самодельные скейтпарки, локальные контесты, теплые солнечные дни на доске и долгие зимние вечера в ожидании нового сезона, и, конечно же, удовольствие от самого процесса, которое может принести эта самая досточка со шкурочкой и колесиками.
        </p>
      </div>
    </div>

  </div>
</template>

<style lang="scss" scoped>
@import '@/assets/scss/_variables.scss';
@import '@/assets/scss/_mixins.scss';
.aboutus-page__title {
  @include font(48px, 400, 60px);
  color: $purple;
  margin: 8px 0 5px;
  @include for-size(tablet) {
    @include font(30px, 400, 1.2);
  }
}
.aboutus-page__body {
  background-image: url(../assets/img/aboutus-bg1.png);
  background-position: center;
  background-repeat: no-repeat;
  background-size: cover;
  padding: 10px 0 10px;
}
.aboutus-page__body p {
  @include font(36px, 500, 43px);
  color: $black;
  @include for-size(tablet) {
    @include font(16px, 400, 1.2);
  }
}
</style>