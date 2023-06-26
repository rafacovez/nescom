<template>
  <div class="social-media">
    <button
      v-for="social in socials"
      :key="social.id"
      role="link"
      tabindex="0"
      class="social-media__icon"
      :aria-label="`Navigate to Nescom ${social.name}`"
      @click="navigateTo(social.url)"
    >
      <object :data="getSocialLogo(social.name)" type="image/svg+xml"></object>
    </button>
  </div>
</template>

<script>
import socials from "@/data/socials";
import { navigateTo } from "@/utils/navigateTo";

export default {
  name: "SocialMediaModal",
  data() {
    return {
      socials: socials.socials,
    };
  },
  methods: {
    navigateTo(url) {
      navigateTo(url);
    },
    getSocialLogo(social) {
      return require(`../assets/${social}Logo.svg`);
    },
  },
};
</script>

<style>
.social-media {
  display: none;
}

@media only screen and (min-width: 1080px) {
  .social-media {
    display: block;
    position: fixed;
    top: 30%;
    transform: translateY(-30%);
    left: 20px;
    display: flex;
    flex-direction: column;
    gap: 1rem;
    border: 1px solid var(--gray);
    width: fit-content;
    margin: 0;
    padding: 1rem 0.5rem;
    border-radius: var(--border-radius-md);
  }

  .social-media__icon {
    display: grid;
    place-items: center;
    background: none;
    border: none;
    opacity: 0.5;
    max-width: 30px;
    cursor: pointer;
  }

  .social-media__icon:hover {
    opacity: 1;
  }
}
</style>
