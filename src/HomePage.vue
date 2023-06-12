<template>
  <PrimaryLayout>
    <LandingSection id="landingSection" />
    <ServicesSection id="servicesSection" />
    <PhilosophySection id="philosophySection" />
    <ClientsSection id="clientsSection" />
    <ContactSection id="contactSection" />
  </PrimaryLayout>
</template>

<script>
import PrimaryLayout from "./layouts/PrimaryLayout.vue";
import LandingSection from "./components/LandingSection.vue";
import ServicesSection from "./components/ServicesSection.vue";
import PhilosophySection from "./components/PhilosophySection.vue";
import ClientsSection from "./components/ClientsSection.vue";
import ContactSection from "./components/ContactSection.vue";

export default {
  name: "HomePage",
  components: {
    PrimaryLayout,
    LandingSection,
    ServicesSection,
    PhilosophySection,
    ClientsSection,
    ContactSection,
  },
};
</script>
