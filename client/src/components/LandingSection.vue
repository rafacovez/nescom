<template>
  <ComponentLayout class="landing-section">
    <div class="landing-section__text">
      <h1>
        Hacemos más efectivas las relaciones entre nuestros clientes y sus
        asociados.
      </h1>
      <router-link class="landing-section__text--link" to="/contacto">
        <CustomButton class="landing-section__text--btn" :isPrimary="true">
          Contáctanos
        </CustomButton>
      </router-link>
    </div>
    <div class="landing-section__illustration">
      <img v-lazy="conferenceSpeakerPath" alt="Conference Speaker" />
    </div>
  </ComponentLayout>
</template>

<script>
import CustomButton from "./CustomButton.vue";
import ComponentLayout from "@/layouts/ComponentLayout.vue";
import conferenceSpeaker from "@/assets/conference-speaker.webp";

export default {
  name: "LandingSection",
  data() {
    return {
      conferenceSpeakerPath: conferenceSpeaker,
    };
  },
  components: {
    CustomButton,
    ComponentLayout,
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

.landing-section__text--link {
  width: fit-content;
  text-decoration: none;
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
