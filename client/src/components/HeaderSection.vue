<template>
  <header class="header">
    <div class="pre-header">
      <a href="https://porlalinea.com.do">
        Por La Línea: Un medio para defender el derecho a la información.
        <ArrowUpRight class="icon" />
      </a>
    </div>
    <div class="main-header">
      <a href="https://nescomrd.com"
        ><img class="logo" :src="logoPath" alt="Nescom RD"
      /></a>
      <div class="header-utilities">
        <LoginButton />
        <ToggleThemeButton />
        <button
          @click="toggleNav"
          class="open-nav-button"
          :class="{ opened: navOpen }"
        >
          <span></span>
        </button>
        <NavSection @click="toggleNav" :class="{ show: navOpen }"></NavSection>
      </div>
    </div>
  </header>
</template>

<script>
import NavSection from "./NavSection.vue";
import logo from "@/assets/logo.png";
import { toggleNav } from "@/utils/toggleNav";
import LoginButton from "./LoginButton.vue";
import ArrowUpRight from "@/assets/icons/ArrowUpRight.vue";
import ToggleThemeButton from "./ToggleThemeButton.vue";

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
    NavSection,
    LoginButton,
    ArrowUpRight,
    ToggleThemeButton,
  },
  methods: {
    toggleNav() {
      toggleNav(this);
    },
    setScreenWidth() {
      this.screenWidth = window.innerWidth;
      this.navOpen = this.screenWidth < 768 ? false : true;
    },
  },
  mounted() {
    // get screen width
    this.setScreenWidth();
    window.addEventListener("resize", this.setScreenWidth);
  },
  beforeUnmount() {
    window.removeEventListener("resize", this.setScreenWidth);
  },
};
</script>

<style>
.pre-header > a {
  background-color: var(--primary-color);
  margin: 0;
  padding: 0.5rem;
  display: flex;
  align-items: center;
  justify-content: center;
  color: var(--background-color);
  font-size: calc(var(--font-size) * 0.7);
  font-weight: var(--font-bold);
  text-align: center;
  text-decoration: none;
}

.main-header {
  background-color: var(--background-color);
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1rem 2rem;
}

.logo {
  max-width: 30px;
}

.open-nav-button {
  background: none;
  border: none;
  padding: 0;
  margin: 0;
  cursor: pointer;
  z-index: 200;
}

.open-nav-button > span {
  width: 20px;
  height: 2px;
  background-color: var(--primary-text-color);
  display: block;
  position: relative;
  transition: all ease-out 0.2s;
}

.open-nav-button > span::before {
  content: "";
  width: 100%;
  height: 100%;
  background-color: var(--primary-text-color);
  display: inherit;
  position: absolute;
  top: -8px;
  transition: inherit;
}

.open-nav-button > span::after {
  content: "";
  width: 100%;
  height: 100%;
  background-color: var(--primary-text-color);
  display: inherit;
  position: absolute;
  top: 8px;
  transition: inherit;
}

.open-nav-button.opened {
  position: fixed;
  top: 50px;
  right: 25px;
}

.open-nav-button.opened > span {
  transform: translateX(10px);
  background-color: rgba(255, 0, 0, 0);
}

.open-nav-button.opened > span::before {
  transform: translate(-10px, 8px) rotate(45deg);
}

.open-nav-button.opened > span::after {
  transform: translate(-10px, -8px) rotate(-45deg);
}

@media only screen and (min-width: 768px) {
  .main-header {
    position: sticky;
    top: 0;
    justify-content: space-between;
    align-items: center;
    padding: 1rem 4rem;
    z-index: 500;
    border-bottom: 1px solid var(--foreground-color);
  }

  .open-nav-button {
    display: none;
  }
}
</style>
