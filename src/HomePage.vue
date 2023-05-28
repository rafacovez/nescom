<template>
  <PrimaryLayout>
    <LandingSection />
    <ServicesSection />
    <PhilosophySection />
    <ClientsSection />
  </PrimaryLayout>
</template>

<script>
import PrimaryLayout from "./layouts/PrimaryLayout.vue";
import LandingSection from "./components/LandingSection.vue";
import ServicesSection from "./components/ServicesSection.vue";
import PhilosophySection from "./components/PhilosophySection.vue";
import ClientsSection from "./components/ClientsSection.vue";

export default {
  name: "HomePage",
  components: {
    PrimaryLayout,
    LandingSection,
    ServicesSection,
    PhilosophySection,
    ClientsSection,
  },
};
</script>
