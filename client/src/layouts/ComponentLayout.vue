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
  border-top: 1px solid var(--foreground-color);
  max-width: 1000px;
  margin: 0 auto;
  padding: 2rem;
}

.component > h1,
.component > h2,
.component > h3,
.component > h4,
.component > h5,
.component > [class$="__header"] {
  margin-bottom: 2rem;
}

@media only screen and (min-width: 768px) {
  .component {
    border-top: none;
    padding: 4rem;
  }
}
</style>
