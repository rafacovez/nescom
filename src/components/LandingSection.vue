<template>
  <ComponentLayout class="landing-section">
    <h1>
      Hacemos más efectivas las relaciones entre nuestros clientes y sus
      asociados.
    </h1>
    <PrimaryButton>Contáctanos</PrimaryButton>
  </ComponentLayout>
  <ComponentLayout>
    <ClientsSection />
  </ComponentLayout>
</template>

<script>
import PrimaryButton from "./PrimaryButton.vue";
import ComponentLayout from "@/layouts/ComponentLayout.vue";
import ClientsSection from "./ClientsSection.vue";

export default {
  name: "LandingSection",
  components: {
    PrimaryButton,
    ComponentLayout,
    ClientsSection,
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
