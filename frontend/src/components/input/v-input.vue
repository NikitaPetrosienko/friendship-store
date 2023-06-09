<script setup lang="ts">
const emit = defineEmits(['update:value']);

const props = defineProps({
  error: {
    type: Array,
    required: false,
  },
  value: {
    type: String,
    default: '',
  },
  name: {
    type: String,
    required: true,
  },
  type: {
    type: String,
    default: 'text',
  },
  placeholder: {
    type: String,
    required: false,
  },
  label: {
    type: String,
    required: false,
  },
  width: {
    type: String,
    default: '300px',
  }
});

const updateValue = (e: any) => {
  emit('update:value', e.target.value)
}
</script>

<template>
  <div class="form-input" :style="{width: width}">
    <input
      class="input-text"
      :type="type"
      :name="name"
      :id="name"
      :placeholder="placeholder"
      :value="value"
      @input="updateValue($event)"
      >
    <label :for="name" class="input-label">{{ label }}</label>

    <TransitionGroup v-if="error">
      <div
        class="form-error"
        v-for="element of error"
        :key="element.$uid">
        <div class="form-error__message">{{ element.$message }}</div>
      </div>
    </TransitionGroup>

  </div>
</template>

<style lang="scss" scoped>
@import '@/assets/scss/_variables.scss';
@import '@/assets/scss/_mixins.scss';

.form-input {
  position: relative;
}

.form-error {
  @include font(16px, 600, 1.2);
  position: absolute;
  margin-top: 4px;
  border-radius: 7px;
  font-size: 13px;
  color: $danger;
  padding: 5px;
}

.input-text {
  border: 1px solid $blue;
  padding: 0 10px;
  height: 40px;
  border-radius: 7px;
  font-size: 15px;
  width: 100%;
  position: relative;
  z-index: 1;
}

.input-text:focus+.input-label {
  z-index: 1;
  opacity: 1;
  top: -20px;
}

.input-text:not(:placeholder-shown)+.input-label {
  z-index: 1;
  opacity: 1;
  top: -20px;
}

.input-label {
  font-weight: bold;
  display: block;
  position: absolute;
  top: 20px;
  opacity: 0;
  z-index: -1;
  transition: .3s;
  font-size: 13px;
  color: $blue;
}
.v-enter-active,
.v-leave-active {
  transition: opacity 0.5s ease;
}
.v-enter-from,
.v-leave-to {
  opacity: 0;
}
</style>
