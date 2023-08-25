<template>
  <ComponentLayout class="landing-section">
    <div class="landing-section__text">
      <h1>
        Hacemos más efectivas las relaciones entre nuestros clientes y sus
        asociados.
      </h1>
      <router-link to="/contact">
        <PrimaryButton class="landing-section__text--btn">
          Contáctanos
          <ArrowUpRight />
        </PrimaryButton>
      </router-link>
    </div>
    <div class="landing-section__illustration">
      <img v-lazy="conferenceSpeakerPath" alt="Conference Speaker" />
    </div>
  </ComponentLayout>
</template>

<script>
import PrimaryButton from "./PrimaryButton.vue";
import ComponentLayout from "@/layouts/ComponentLayout.vue";
import ArrowUpRight from "@/assets/icons/ArrowUpRight.vue";
import conferenceSpeaker from "@/assets/conference-speaker.webp";

export default {
  name: "LandingSection",
  data() {
    return {
      conferenceSpeakerPath: conferenceSpeaker,
    };
  },
  components: {
    PrimaryButton,
    ComponentLayout,
    ArrowUpRight,
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

.landing-section__text--btn {
  display: flex;
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
    max-width: 350px;
  }
}
</style>
