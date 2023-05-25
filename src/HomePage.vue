<template>
  <HeaderSection />
  <FooterSection />
</template>

<script>
import HeaderSection from "./components/HeaderSection.vue";
import FooterSection from "./components/FooterSection.vue";

export default {
  name: "HomePage",
  components: {
    HeaderSection,
    FooterSection,
  },
};
</script>
