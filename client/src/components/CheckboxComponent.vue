<template>
  <div class="checkbox-wrapper">
    <span class="checkbox" :class="{ checked: isChecked }" @click="toggleCheck">
      <font-awesome-icon icon="fas fa-check" class="checkbox-icon"
    /></span>
    <p class="checkbox-text">
      {{ checkboxText }}
    </p>
  </div>
</template>

<script>
export default {
  name: "CheckboxComponent",
  props: {
    isChecked: {
      type: Boolean,
      default: false,
    },
    checkboxText: {
      type: String,
      default: "",
    },
  },
  methods: {
    toggleCheck() {
      this.$emit("update:checked", !this.isChecked);
    },
  },
};
</script>

<style>
.checkbox-wrapper {
  display: flex;
  align-items: center;
  gap: 10px;
}

.checkbox {
  flex: 0 0 15px;
  height: 15px;
  width: 15px;
  border: 1px solid var(--primary-color);
  border-radius: var(--border-radius-sm);
}

.checkbox.checked {
  background-color: var(--primary-color);
}

.checkbox-icon {
  display: none;
  color: var(--white);
}

.checkbox.checked > .checkbox-icon {
  max-width: 75%;
  margin: 0 auto;
  display: block;
}

.checkbox-text {
  font-size: calc(var(--font-size) * 0.7);
  color: var(--secondary-text-color);
}
</style>
