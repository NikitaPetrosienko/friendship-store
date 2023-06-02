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
    required: true,
  },
  label: {
    type: String,
    required: true,
  },
});

const updateValue = (e: any) => {
  emit('update:value', e.target.value);
}

</script>

<template>
  <div class="textarea-input">
    <textarea
      class="textarea-text"
      :type="type"
      :name="name"
      :id="name"
      :placeholder="placeholder"
      @input="updateValue($event)"
    ></textarea>

    <label class="textarea-label" :for="name" >{{ label }}</label>

    <TransitionGroup>
    <div
      class="textarea-error"
      v-for="element of error"
      :key="element.$uid">
      <div class="textarea-error__message">{{ element.$message }}</div>
    </div>
  </TransitionGroup>
  </div>
</template>

<style lang="scss" scoped>
@import '@/assets/scss/_mixins.scss';
@import '@/assets/scss/_variables.scss';

.textarea-input {
  position: relative;
  margin-bottom: 20px;
}

.textarea-error {
  @include font(16px, 600, 1.2);
  position: absolute;
  margin-top: 4px;
  border-radius: 7px;
  font-size: 13px;
  color: $danger;
  padding: 5px;
}

.textarea-label {
  display: block;
  @include font(13px, 700, 24px);
  position: absolute;
  top: 25px;
  opacity: 0;
  z-index: -1;
  transition: .3s;
  color: $blue;
}

.textarea-text {
  position: relative;
  z-index: 1;
  @include font(16px, 400, 24px);
  width: 100%;
  height: 200px;
  border: 1px solid $blue;
  border-radius: 7px;
  padding: 15px 10px;
  resize: none;
}

.textarea-text:focus+.textarea-label {
  z-index: 1;
  opacity: 1;
  top: -25px;
}

.textarea-text:focus:not(:placeholder-shown)+.textarea-label {
  z-index: 1;
  opacity: 1;
  top: -25px;
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
