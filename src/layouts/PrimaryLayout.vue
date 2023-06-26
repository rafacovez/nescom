<template>
  <HeaderSection />
  <main>
    <slot></slot>
  </main>
  <FooterSection />
</template>

<script>
import HeaderSection from "../components/HeaderSection.vue";
import FooterSection from "../components/FooterSection.vue";

export default {
  name: "PrimaryLayout",
  components: {
    HeaderSection,
    FooterSection,
  },
};
</script>
