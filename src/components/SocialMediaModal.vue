<template>
  <div v-if="screenWidth >= 1080" class="social-media">
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
  data() {
    return {
      screenWidth: window.innerWidth,
    };
  },
  components: {
    InstagramLogo,
    FacebookLogo,
    TwitterLogo,
    YoutubeLogo,
  },
  mounted() {
    this.setScreenWidth();
    window.addEventListener("resize", this.setScreenWidth);
    if (this.screenWidth >= 768) {
      this.navOpen = true;
    } else {
      this.navOpen = false;
    }
  },
  beforeUnmount() {
    window.removeEventListener("resize", this.setScreenWidth);
  },
  methods: {
    setScreenWidth() {
      this.screenWidth = window.innerWidth;
    },
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
</style>
