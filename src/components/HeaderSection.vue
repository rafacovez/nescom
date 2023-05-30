<template>
  <header class="header">
    <img class="logo" :src="logoPath" alt="Nescom RD" />
    <button @click="toggleNav" class="nav__button" :class="{ x: navOpen }">
      <span></span>
    </button>
    <nav class="nav" :class="{ show: navOpen }">
      <li
        @click="
          scrollTo('#philosophySection');
          toggleNav();
        "
      >
        ¿Quiénes somos?
      </li>
      <li
        @click="
          scrollTo('#servicesSection');
          toggleNav();
        "
      >
        Servicios
      </li>
      <li
        @click="
          scrollTo('#clientsSection');
          toggleNav();
        "
      >
        Clientes
      </li>
      <li
        @click="
          scrollTo('#contactSection');
          toggleNav();
        "
      >
        Contacto
      </li>
      <a
        href="https://www.porlalinea.com.do/secciones/en-conexion/con-nestor-estevez/"
      >
        <li @click="toggleNav()">
          Blog | Néstor Estévez <ArrowUpRightIcon class="icon" />
        </li>
      </a>
      <div class="nav__social-media">
        <button
          @click="
            navigateToInstagram();
            toggleNav();
          "
          role="link"
          tabindex="0"
          class="social-media-icon"
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
          class="social-media-icon"
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
          class="social-media-icon"
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
          class="social-media-icon"
          aria-label="Navigate to Nescom RD Youtube"
        >
          <YoutubeLogo />
        </button>
      </div>
    </nav>
  </header>
</template>

<script>
import logo from "../assets/logo.png";
import InstagramLogo from "@/assets/icons/InstagramLogo.vue";
import FacebookLogo from "@/assets/icons/FacebookLogo.vue";
import TwitterLogo from "@/assets/icons/TwitterLogo.vue";
import YoutubeLogo from "@/assets/icons/YoutubeLogo.vue";
import { ArrowUpRightIcon } from "@heroicons/vue/20/solid";

export default {
  name: "HeaderSection",
  data() {
    return {
      logoPath: logo,
      navOpen: false,
    };
  },
  components: {
    InstagramLogo,
    FacebookLogo,
    TwitterLogo,
    YoutubeLogo,
    ArrowUpRightIcon,
  },
  methods: {
    toggleNav() {
      this.navOpen = !this.navOpen;
      if (this.navOpen) {
        document.body.classList.add("no-scroll");
      } else {
        document.body.classList.remove("no-scroll");
      }
    },
    scrollTo(selector) {
      const element = document.querySelector(selector);
      element.scrollIntoView({ behavior: "smooth" });
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
.header {
  display: flex;
  justify-content: space-between;
  padding: 1rem 2rem;
}

.logo {
  max-width: 30px;
}

.nav {
  background-color: var(--white);
  color: var(--black);
  position: fixed;
  flex-direction: column;
  top: 62px;
  left: 0;
  min-height: 100%;
  width: 100%;
  padding: 2rem 3rem;
  margin: 0;
  visibility: hidden;
  opacity: 0;
  transform: translateY(-25px);
  transition: all ease-out 0.2s;
  z-index: 50;
}

.nav.show {
  visibility: visible;
  opacity: 1;
  transform: translateY(0px);
}

.nav > li,
a > li {
  display: flex;
  gap: 0.2rem;
  font-size: calc(var(--font-size) * 0.9);
  font-weight: var(--font-regular);
  list-style: none;
  border-bottom: 1px solid var(--gray);
  padding: 1rem 0;
  cursor: pointer;
}

.nav > a {
  color: var(--black);
  text-decoration: none;
  width: 100%;
}

.nav > a > li > .icon {
  width: 15px;
  color: var(--black);
}

.nav__social-media {
  display: flex;
  align-items: center;
  justify-content: center;
  margin: 3rem 0 0 0;
  gap: 1rem;
}

.nav__social-media > .social-media-icon {
  background: none;
  border: none;
  cursor: pointer;
  opacity: 0.5;
}

.nav__social-media > .social-media-icon:hover {
  opacity: 1;
}

.nav__button {
  background: none;
  border: none;
  padding: 0;
  margin: 0;
  cursor: pointer;
}

.nav__button > span {
  width: 20px;
  height: 2px;
  background-color: var(--black);
  display: block;
  position: relative;
  transition: all ease-out 0.2s;
}

.nav__button > span::before {
  content: "";
  width: 100%;
  height: 100%;
  background-color: var(--black);
  display: inherit;
  position: absolute;
  top: -8px;
  transition: inherit;
}

.nav__button > span::after {
  content: "";
  width: 100%;
  height: 100%;
  background-color: var(--black);
  display: inherit;
  position: absolute;
  top: 8px;
  transition: inherit;
}

.nav__button.x > span {
  transform: translateX(10px);
  background-color: rgba(255, 0, 0, 0);
}

.nav__button.x > span::before {
  transform: translate(-10px, 8px) rotate(45deg);
}

.nav__button.x > span::after {
  transform: translate(-10px, -8px) rotate(-45deg);
}
</style>
