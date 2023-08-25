<template>
  <SocialMediaModal />
  <LandingSection id="landingSection" />
  <ServicesSection id="servicesSection" />
  <PhilosophySection id="philosophySection" />
  <ClientsSection id="clientsSection" />
  <BlogSection id="blogSection" />
  <ContactSection id="contactSection" />
</template>

<script>
import LandingSection from "@/components/LandingSection.vue";
import ServicesSection from "@/components/ServicesSection.vue";
import PhilosophySection from "@/components/PhilosophySection.vue";
import ClientsSection from "@/components/ClientsSection.vue";
import BlogSection from "@/components/BlogSection.vue";
import ContactSection from "@/components/ContactSection.vue";
import SocialMediaModal from "@/components/SocialMediaModal.vue";

export default {
  name: "HomePage",
  components: {
    LandingSection,
    ServicesSection,
    PhilosophySection,
    ClientsSection,
    BlogSection,
    ContactSection,
    SocialMediaModal,
  },
};
</script>
