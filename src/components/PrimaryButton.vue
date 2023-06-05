<template>
  <button class="primary-btn">
    <slot></slot>
  </button>
</template>

<script>
export default {
  name: "PrimaryButton",
};
</script>

<style>
.primary-btn {
  border: none;
  background-color: var(--red);
  color: var(--white);
  font-size: calc(var(--font-size) * 1);
  font-weight: var(--font-bold);
  height: auto;
  width: 100%;
  margin: 0;
  padding: 0.5rem 2rem;
  border-radius: 4px;
  box-shadow: 4px 4px 4px 0 rgba(0, 0, 0, 0.2);
  cursor: pointer;
  transition: all ease-out 0.2s;
}

.primary-btn:hover {
  transform: translateY(-1px);
  box-shadow: 4px 4px 4px 2px rgba(0, 0, 0, 0.2);
}

@media only screen and (min-width: 768px) {
  .primary-btn {
    width: fit-content;
  }
}
</style>
