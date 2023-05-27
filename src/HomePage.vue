<template>
  <PrimaryLayout>
    <LandingSection />
    <ClientsSection />
    <PhilosophySection />
  </PrimaryLayout>
</template>

<script>
import PrimaryLayout from "./layouts/PrimaryLayout.vue";
import LandingSection from "./components/LandingSection.vue";
import ClientsSection from "./components/ClientsSection.vue";
import PhilosophySection from "./components/PhilosophySection.vue";

export default {
  name: "HomePage",
  components: {
    PrimaryLayout,
    LandingSection,
    ClientsSection,
    PhilosophySection,
  },
};
</script>
