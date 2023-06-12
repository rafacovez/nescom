<template>
  <header class="header">
    <img class="logo" :src="logoPath" alt="Nescom RD" />
    <button
      v-if="screenWidth < 768"
      @click="toggleNav"
      class="open-nav-button"
      :class="{ x: navOpen }"
    >
      <span></span>
    </button>
    <nav class="nav" :class="{ show: navOpen }">
      <ul>
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
        <li @click="toggleNav()">
          <a
            href="https://www.porlalinea.com.do/secciones/en-conexion/con-nestor-estevez/"
          >
            Blog | Néstor Estévez <ArrowUpRightIcon class="icon" />
          </a>
        </li>
      </ul>
      <div v-if="screenWidth < 768" class="nav__social-media">
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
      screenWidth: window.innerWidth,
    };
  },
  components: {
    InstagramLogo,
    FacebookLogo,
    TwitterLogo,
    YoutubeLogo,
    ArrowUpRightIcon,
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
    toggleNav() {
      if (this.screenWidth < 768) {
        this.navOpen = !this.navOpen;
        if (this.navOpen) {
          document.body.classList.add("no-scroll");
        } else {
          document.body.classList.remove("no-scroll");
        }
      }
    },
    scrollTo(selector) {
      const element = document.querySelector(selector);
      element.scrollIntoView({ behavior: "smooth" });
    },
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
  z-index: 100;
}

.nav.show {
  visibility: visible;
  opacity: 1;
  transform: translateY(0px);
}

.nav > ul {
  margin: 0;
  padding: 0;
}

.nav > ul > li {
  color: var(--black);
  font-size: calc(var(--font-size) * 0.9);
  font-weight: var(--font-regular);
  border-bottom: 1px solid var(--gray);
  padding: 1rem 0;
  list-style: none;
  cursor: pointer;
}

.nav > ul > li > a {
  display: flex;
  gap: 0.2rem;
  color: var(--black);
  text-decoration: none;
  width: 100%;
}

.nav > ul > li > a > .icon {
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

.open-nav-button {
  background: none;
  border: none;
  padding: 0;
  margin: 0;
  cursor: pointer;
}

.open-nav-button > span {
  width: 20px;
  height: 2px;
  background-color: var(--black);
  display: block;
  position: relative;
  transition: all ease-out 0.2s;
}

.open-nav-button > span::before {
  content: "";
  width: 100%;
  height: 100%;
  background-color: var(--black);
  display: inherit;
  position: absolute;
  top: -8px;
  transition: inherit;
}

.open-nav-button > span::after {
  content: "";
  width: 100%;
  height: 100%;
  background-color: var(--black);
  display: inherit;
  position: absolute;
  top: 8px;
  transition: inherit;
}

.open-nav-button.x > span {
  transform: translateX(10px);
  background-color: rgba(255, 0, 0, 0);
}

.open-nav-button.x > span::before {
  transform: translate(-10px, 8px) rotate(45deg);
}

.open-nav-button.x > span::after {
  transform: translate(-10px, -8px) rotate(-45deg);
}

@media only screen and (min-width: 768px) {
  .header {
    justify-content: space-between;
    align-items: center;
    padding: 1rem 4rem;
  }

  .logo {
    max-width: 50px;
  }

  .nav {
    position: static;
    width: fit-content;
    padding: 0;
    margin: 0;
    z-index: 0;
  }

  .nav > ul {
    display: flex;
    gap: 2rem;
  }

  .nav > ul > li {
    padding: 0.5rem 0;
    transition: all ease-out 0.2s;
  }

  .nav > ul > li:hover {
    border-bottom-color: var(--red);
  }
}
</style>
