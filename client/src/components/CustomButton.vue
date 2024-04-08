<template>
  <button class="btn" :class="{ 'btn--primary': isPrimary }">
    <slot></slot>
  </button>
</template>

<script>
export default {
  name: "CustomButton",
  props: {
    isPrimary: {
      type: Boolean,
      default: false,
    },
  },
};
</script>

<style>
.btn {
  border: none;
  background-color: var(--background-color);
  color: var(--primary-text-color);
  font-size: calc(var(--font-size) * 1);
  font-weight: var(--font-bold);
  height: auto;
  margin: 0;
  padding: 0.5rem 2rem;
  border: 2px solid var(--primary-color);
  border-radius: var(--border-radius-md);
  box-shadow: 4px 4px 4px 0 var(--box-shadow-color);
  cursor: pointer;
  transition: all ease-out 0.2s;
}

.btn--primary {
  background-color: var(--primary-color);
  color: var(--background-color);
  width: 100%;
  padding: 0.5rem 4rem;
}

.btn:hover {
  transform: translateY(-1px);
  box-shadow: 4px 4px 4px 2px var(--box-shadow-color);
}

@media only screen and (min-width: 768px) {
  .btn {
    width: fit-content;
  }
}
</style>
