<template>
  <div>
    <SocialMediaModal />
    <ContactSection />
  </div>
</template>

<script>
import ContactSection from "@/components/ContactSection.vue";
import SocialMediaModal from "@/components/SocialMediaModal.vue";

export default {
  name: "ContactPage",
  components: {
    ContactSection,
    SocialMediaModal,
  },
};
</script>
