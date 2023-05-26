<template>
  <div class="component">
    <slot></slot>
  </div>
</template>

<script>
export default {
  name: "Component",
};
</script>

<style>
.component {
  border-top: 1px solid var(--gray);
  max-width: 800px;
  margin: 0 auto;
  padding: 2rem;
}
</style>
