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
    <div class="landing-section__illustration">
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
  methods: {
    scrollTo(selector) {
      const element = document.querySelector(selector);
      element.scrollIntoView({ behavior: "smooth" });
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

.landing-section__illustration {
  display: none;
}

@media only screen and (min-width: 1080px) {
  .landing-section {
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: space-between;
  }

  .landing-section > div {
    flex-basis: 50%;
  }

  .landing-section__text > h1 {
    font-size: calc(var(--font-size) * 3);
  }

  .landing-section__illustration {
    display: block;
    max-width: 250px;
  }
}
</style>
