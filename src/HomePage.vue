<template>
  <PrimaryLayout>
    <LandingSection />
  </PrimaryLayout>
</template>

<script>
import PrimaryLayout from "./layouts/PrimaryLayout.vue";
import LandingSection from "./components/LandingSection.vue";

export default {
  name: "HomePage",
  components: {
    PrimaryLayout,
    LandingSection,
  },
};
</script>
