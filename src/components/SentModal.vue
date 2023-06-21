<template>
  <div v-show="modalIsVisible" class="sent">
    <div class="sent__modal">
      <XMarkIcon class="x-icon" @click="hideModal" />
      <slot> </slot>
    </div>
  </div>
</template>

<script>
import { XMarkIcon } from "@heroicons/vue/20/solid";

export default {
  name: "SentModal",
  components: {
    XMarkIcon,
  },
  props: {
    modalIsVisible: {
      type: Boolean,
      default: false,
    },
  },
  methods: {
    showModal() {
      this.$emit("update:modal-is-visible", true);
    },
    hideModal() {
      this.$emit("update:modal-is-visible", false);
    },
  },
};
</script>

<style>
.sent {
  display: grid;
  place-items: center;
  position: fixed;
  inset: 0;
  background-color: rgba(0, 0, 0, 0.2);
  z-index: 600;
}

.sent__modal {
  position: relative;
  background-color: var(--white);
  border: 2px solid var(--gray);
  border-radius: var(--border-radius-sm);
  margin: 3rem;
  padding: 2rem;
  max-width: 300px;
  z-index: 700;
}

.sent__modal > .x-icon {
  position: absolute;
  top: 5px;
  right: 5px;
  width: 20px;
  cursor: pointer;
}

.sent__modal > p {
  text-align: center;
  font-size: calc(var(--font-size) * 0.9);
  color: var(--black);
}
</style>
