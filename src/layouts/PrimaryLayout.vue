<template>
  <div class="wrapper">
    <HeaderSection />
    <slot></slot>
    <FooterSection />
  </div>
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
