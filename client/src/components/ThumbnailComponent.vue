<template>
  <div class="thumbnail">
    <input
      v-show="isInput"
      @change="onInputChange"
      class="sr-only"
      type="file"
      id="imageInput"
      accept="image/*"
    />
    <label class="thumbnail__label" v-show="isInput" for="imageInput">
      {{ labelText }}
    </label>
    <img
      class="thumbnail__img"
      :class="{ post: !isInput }"
      v-lazy="thumbnailSrc"
      :alt="thumbnailAlt"
    />
  </div>
</template>

<script>
export default {
  name: "ThumbnailComponent",
  props: {
    thumbnailSrc: {
      type: String,
      default: "",
    },
    thumbnailAlt: {
      type: String,
      default: "Post thumbnail",
    },
    isInput: {
      type: Boolean,
      default: false,
    },
    labelText: {
      type: String,
      default: "Click aquí",
    },
    onInputChange: {
      type: Function,
      default: null,
    },
  },
};
</script>

<style>
.thumbnail {
  position: relative;
  border: 1px solid var(--foreground-color);
  width: 100%;
  padding-top: 66.67%;
  border-radius: var(--border-radius-sm);
  overflow: hidden;
}

.thumbnail__label {
  position: absolute;
  inset: 0;
  display: grid;
  place-items: center;
  font-size: calc(var(--font-size) * 0.8);
  color: var(--white);
  background-color: var(--black);
  cursor: pointer;
  opacity: 0.6;
}

.thumbnail__label.error {
  border: 1px solid var(--red);
}

.thumbnail__img {
  position: absolute;
  top: 0;
  left: 0;
  height: 100%;
  width: 100%;
  object-fit: cover;
  z-index: var(--z-index-back-xl);
}
</style>
