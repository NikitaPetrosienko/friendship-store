<script setup lang="ts">

import { computed } from 'vue';

import { useCommonStore } from '@/store/common/common';

const commonStore = useCommonStore();
const btnColor = computed(() => {
  if (commonStore.alert.status === 'danger') {
    return 'alert__btn_danger'
  }
  else if (commonStore.alert.status === 'warning') {
    return 'alert__btn_warning'
  }
  return 'alert__btn_success';
});

const alertColor = computed(() => {
  if (commonStore.alert.status === 'danger') {
    return 'alert_danger'
  }
  else if (commonStore.alert.status === 'warning') {
    return 'alert_warning'
  }
  return 'alert_success';
});

const alertText = computed(() => {
  if (commonStore.alert.status === 'danger') {
    return 'Ошибка'
  }
  else if (commonStore.alert.status === 'warning') {
    return 'Предупреждение'
  }
  return 'Успешно';
});

const closeAlert = () => {
  commonStore.clearAlert();
}

</script>

<template>
  <div
    v-if="commonStore.alert.info !== null"
    class="alert"
    :class="alertColor"
  >
    <h3 class="alert__title">{{ alertText }}</h3>
    <p class="alert__text">{{ commonStore.alert.info }}</p>
    <button class="alert__btn" :class="btnColor" @click="closeAlert">Закрыть</button>
  </div>
</template>

<style lang="scss" scoped>
@import '@/assets/scss/_variables.scss';
@import '@/assets/scss/_mixins.scss';
.alert {
  padding: 16px 24px;
  border-left-width: 10px;
  border-left-style: solid;
  border-bottom-right-radius: 2px;
  border-top-right-radius: 2px;
}

.alert_success {
  border-color: $success;
  background-color: $bg-loader;
}

.alert_danger {
  border-color: $danger;
  background-color: $bg-loader;
}

.alert_warning {
  border-color: $warning;
  background-color: $bg-loader;
}

.alert__text {
  @include font(18px, 400, 1.7);
  color: $black;
}

.alert__title {
  @include font(20px, 600, 1.7);
  text-transform: uppercase;
  margin: 0 0 30px;
}
.alert__btn {
  @include button-reset;
}
.alert__btn {
  @include font(18px, 700, 1);
  padding: 8px 24px;
  border-radius: 99px;
  text-transform: uppercase;
  white-space: nowrap;
  transition: all 0.3s;
}

.alert__btn:hover {
  opacity: 0.8;
}

// .alert__btn:disabled {
//   cursor: not-allowed;
//   opacity: 1!important;
//   background: #eee!important;
//   border-color: #ddd!important;
//   color: #999!important;
// }

.alert__btn:active {
  box-shadow: inset 1px 1px 1px rgba(0, 0, 0, 0.3);
}

.alert__btn_success {
  background: $success;
  color: $white;
  border-color: $success;
}

.alert__btn_danger {
  background: $danger;
  color: $white;
  border-color: $danger;
}

.alert__btn_warning {
  background: $warning;
  color: $white;
  border-color: $warning;
}
</style>