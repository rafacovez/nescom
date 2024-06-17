<template>
  <div v-show="modalIsVisible" class="pop-up">
    <div class="pop-up__modal">
      <slot> </slot>
      <CustomButton :isPrimary="true" @click="hidePopUp" class="pop-up__button"
        ><font-awesome-icon
          icon="fas fa-xmark"
          class="x-icon"
        />Cerrar</CustomButton
      >
    </div>
  </div>
</template>

<script>
import CustomButton from "./CustomButton.vue";

export default {
  name: "PopUpModal",
  components: {
    CustomButton,
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
  z-index: var(--z-index-front-xl);
}

.pop-up__modal {
  position: relative;
  display: block;
  background-color: var(--background-color);
  border: 2px solid var(--foreground-color);
  border-radius: var(--border-radius-sm);
  padding: 2rem;
  max-width: 300px;
  z-index: var(--z-index-front-xxl);
}

.pop-up__button {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 5px;
  margin: 0 auto;
}

.pop-up__button > .x-icon {
  width: 20px;
}
</style>
