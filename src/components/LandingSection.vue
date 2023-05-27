<template>
  <ComponentLayout class="landing-section">
    <h1>
      Hacemos más efectivas las relaciones entre nuestros clientes y sus
      asociados.
    </h1>
    <PrimaryButton>Contáctanos</PrimaryButton>
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
};
</script>

<style>
.landing-section {
  display: flex;
  flex-direction: column;
  gap: 2rem;
}
</style>
