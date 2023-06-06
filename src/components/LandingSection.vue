<template>
  <ComponentLayout class="landing-section">
    <div class="landing-section__text">
      <h1>
        Hacemos más efectivas las relaciones entre nuestros clientes y sus
        asociados.
      </h1>
      <PrimaryButton @click="scrollTo('#contactSection')"
        >Contáctanos</PrimaryButton
      >
    </div>
    <div v-if="screenWidth >= 768" class="landing-section__illustration">
      <CommunicationIllustration />
    </div>
  </ComponentLayout>
</template>

<script>
import PrimaryButton from "./PrimaryButton.vue";
import ComponentLayout from "@/layouts/ComponentLayout.vue";
import CommunicationIllustration from "../assets/illustrations/CommunicationIllustration.vue";

export default {
  name: "LandingSection",
  components: {
    PrimaryButton,
    ComponentLayout,
    CommunicationIllustration,
  },
  data() {
    return {
      screenWidth: window.innerWidth,
    };
  },
  mounted() {
    this.setScreenWidth();
    window.addEventListener("resize", this.setScreenWidth);
  },
  beforeUnmount() {
    window.removeEventListener("resize", this.setScreenWidth);
  },
  methods: {
    scrollTo(selector) {
      const element = document.querySelector(selector);
      element.scrollIntoView({ behavior: "smooth" });
    },
    setScreenWidth() {
      this.screenWidth = window.innerWidth;
    },
  },
};
</script>

<style>
.landing-section__text {
  display: flex;
  flex-direction: column;
  gap: 2rem;
}

@media only screen and (min-width: 768px) {
  .landing-section {
    display: grid;
    grid-template-columns: 1fr 1fr;
    place-items: center;
  }

  .landing-section__text > h1 {
    font-size: calc(var(--font-size) * 2.5);
  }

  .landing-section__illustration {
    max-width: 250px;
  }
}
</style>
