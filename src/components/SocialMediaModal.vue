<template>
  <div class="social-media">
    <button
      @click="
        navigateToInstagram();
        toggleNav();
      "
      role="link"
      tabindex="0"
      class="social-media__icon"
      aria-label="Navigate to Nescom RD Instagram profile"
    >
      <InstagramLogo />
    </button>
    <button
      @click="
        navigateToFacebook();
        toggleNav();
      "
      role="link"
      tabindex="0"
      class="social-media__icon"
      aria-label="Navigate to Nescom RD Facebook page"
    >
      <FacebookLogo />
    </button>
    <button
      @click="
        navigateToTwitter();
        toggleNav();
      "
      role="link"
      tabindex="0"
      class="social-media__icon"
      aria-label="Navigate to Nescom RD Twitter profile"
    >
      <TwitterLogo />
    </button>
    <button
      @click="
        navigateToYoutube();
        toggleNav();
      "
      role="link"
      tabindex="0"
      class="social-media__icon"
      aria-label="Navigate to Nescom RD Youtube"
    >
      <YoutubeLogo />
    </button>
  </div>
</template>

<script>
import InstagramLogo from "@/assets/icons/InstagramLogo.vue";
import FacebookLogo from "@/assets/icons/FacebookLogo.vue";
import TwitterLogo from "@/assets/icons/TwitterLogo.vue";
import YoutubeLogo from "@/assets/icons/YoutubeLogo.vue";

export default {
  name: "SocialMediaModal",
  components: {
    InstagramLogo,
    FacebookLogo,
    TwitterLogo,
    YoutubeLogo,
  },
  methods: {
    navigateToInstagram() {
      window.location.href = "https://www.instagram.com/nescomrd";
    },
    navigateToFacebook() {
      window.location.href = "https://www.facebook.com/nescomrd";
    },
    navigateToTwitter() {
      window.location.href = "https://twitter.com/nescomrd";
    },
    navigateToYoutube() {
      window.location.href =
        "https://www.youtube.com/channel/UCK6yeR3uawJDFfUKMehdD1A";
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
