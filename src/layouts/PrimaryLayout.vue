<template>
  <SocialMediaModal />
  <ScrollTrackingModal />
  <HeaderSection />
  <main>
    <slot></slot>
  </main>
  <FooterSection />
</template>

<script>
import HeaderSection from "../components/HeaderSection.vue";
import FooterSection from "../components/FooterSection.vue";
import SocialMediaModal from "../components/SocialMediaModal.vue";
import ScrollTrackingModal from "../components/ScrollTrackingModal.vue";

export default {
  name: "PrimaryLayout",
  components: {
    HeaderSection,
    FooterSection,
    SocialMediaModal,
    ScrollTrackingModal,
  },
};
</script>
