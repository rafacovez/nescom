<template>
  <div class="form-group">
    <label
      v-show="!inputValue"
      class="label"
      :for="inputName"
      :class="{ focused: isFocused }"
    >
      {{ inputName }}:
      <span v-show="isRequired" class="label__required-indicator"> *</span>
    </label>
    <input
      v-if="!isTextarea"
      class="input"
      type="text"
      :id="inputName"
      :name="inputName"
      :autocomplete="isAutocomplete ? 'on' : 'off'"
      :required="isRequired"
      :value="inputValue"
      @input="$emit('update:inputValue', $event.target.value)"
      @focus="$emit('update:isFocused', true)"
      @blur="$emit('update:isFocused', false)"
    />
    <textarea
      v-else
      class="textarea"
      :id="inputName"
      :name="inputName"
      :autocomplete="isAutocomplete ? 'on' : 'off'"
      :required="isRequired"
      :value="inputValue"
      @input="$emit('update:inputValue', $event.target.value)"
      @focus="$emit('update:isFocused', true)"
      @blur="$emit('update:isFocused', false)"
    ></textarea>
  </div>
</template>

<script>
export default {
  name: "InputComponent",
  props: {
    inputValue: {
      type: String,
      default: "",
    },
    inputName: {
      type: String,
      default: "",
    },
    isTextarea: {
      type: Boolean,
      default: false,
    },
    isRequired: {
      type: Boolean,
      default: false,
    },
    isAutocomplete: {
      type: Boolean,
      default: false,
    },
    isFocused: {
      type: Boolean,
      default: false,
    },
  },
  emits: ["update:inputValue", "update:isFocused"],
};
</script>

<style>
.form-group {
  position: relative;
  background-color: var(--background-color);
}

.form-group > * {
  width: 100%;
  font-size: calc(var(--font-size) * 0.8);
  padding: 1rem;
  margin-top: 1.5rem;
}

.label {
  color: var(--secondary-text-color);
  font-weight: var(--font-bold);
  position: absolute;
  inset: 0;
  pointer-events: none;
  transition: all ease-out 0.2s;
}

.label.focused {
  padding: 0;
  margin: 0;
  color: var(--primary-text-color);
  font-size: calc(var(--font-size) * 0.9);
}

.label > .label__required-indicator {
  color: var(--primary-color);
}

.input,
.textarea {
  outline: none;
  border: 1px solid var(--foreground-color);
  background-color: var(--background-color);
  color: var(--primary-text-color);
  border-radius: var(--border-radius-sm);
  touch-action: manipulation;
}

.input:focus,
.textarea:focus {
  border: 1px solid var(--primary-color);
}
</style>
