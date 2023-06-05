<template>
  <ComponentLayout class="landing-section">
    <div class="landing-section__text">
      <h1>
        Hacemos más efectivas las relaciones entre nuestros clientes y sus
        asociados.
      </h1>
      <PrimaryButton @click="scrollTo('#contactSection')"
        >Contáctanos</PrimaryButton
      >
    </div>
  </ComponentLayout>
</template>

<script>
import PrimaryButton from "./PrimaryButton.vue";
import ComponentLayout from "@/layouts/ComponentLayout.vue";

export default {
  name: "LandingSection",
  components: {
    PrimaryButton,
    ComponentLayout,
  },
  methods: {
    scrollTo(selector) {
      const element = document.querySelector(selector);
      element.scrollIntoView({ behavior: "smooth" });
    },
  },
};
</script>

<style>
.landing-section__text {
  display: flex;
  flex-direction: column;
  gap: 2rem;
}

@media only screen and (min-width: 768px) {
  .landing-section {
    display: grid;
    grid-template-columns: 1fr 1fr;
  }
}
</style>
