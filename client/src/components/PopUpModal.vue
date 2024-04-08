<template>
  <div v-show="modalIsVisible" class="pop-up">
    <div class="pop-up__modal">
      <slot> </slot>
      <CustomButton :isPrimary="true" @click="hidePopUp" class="pop-up__button"
        ><XMarkIcon class="x-icon" />Cerrar</CustomButton
      >
    </div>
  </div>
</template>

<script>
import CustomButton from "./CustomButton.vue";
import { XMarkIcon } from "@heroicons/vue/20/solid";

export default {
  name: "PopUpModal",
  components: {
    CustomButton,
    XMarkIcon,
  },
  props: {
    modalIsVisible: {
      type: Boolean,
      default: false,
    },
  },
  methods: {
    showPopUp() {
      this.$emit("update:modal-is-visible", true);
      document.body.classList.add("no-scroll");
    },
    hidePopUp() {
      this.$emit("update:modal-is-visible", false);
      document.body.classList.remove("no-scroll");
    },
  },
};
</script>

<style>
.pop-up {
  position: fixed;
  inset: 0;
  display: grid;
  place-items: center;
  background-color: rgba(0, 0, 0, 0.5);
  z-index: 1000;
}

.pop-up__modal {
  position: relative;
  background-color: var(--background-color);
  border: 2px solid var(--foreground-color);
  border-radius: var(--border-radius-sm);
  padding: 2rem;
  max-width: 300px;
  z-index: 1001;
}

.pop-up__button {
  display: flex;
  gap: 5px;
  margin: 0 auto;
}

.pop-up__button > .x-icon {
  width: 20px;
}
</style>
