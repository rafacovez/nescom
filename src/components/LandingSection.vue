<template>
  <div class="landing-section">
    <h1>
      Hacemos más efectivas las relaciones entre nuestros clientes y sus
      asociados.
    </h1>
    <PrimaryButton>Contáctanos</PrimaryButton>
  </div>
</template>

<script>
import PrimaryButton from "./PrimaryButton.vue";

export default {
  name: "LandingSection",
  components: {
    PrimaryButton,
  },
};
</script>

<style>
.landing-section {
  display: flex;
  flex-direction: column;
  gap: 2rem;
  padding: 2rem;
  border: 1px solid var(--gray);
}
</style>
