<template>
  <nav class="nav">
    <ul class="nav__list">
      <router-link
        class="nav__item"
        v-for="item in nav"
        :key="item.id"
        :to="item.ref"
      >
        {{ item.name }}
      </router-link>
    </ul>
    <div class="nav__social-media">
      <button
        v-for="social in socials"
        :key="social.id"
        role="link"
        tabindex="0"
        class="nav__social-media--link"
        :aria-label="`Navigate to Nescom ${social.name}`"
        @click="navigateTo(social.url)"
      >
        <font-awesome-icon
          :icon="social.icon"
          type="image/svg+xml"
          class="nav__social-media--icon"
        />
      </button>
    </div>
  </nav>
</template>

<script>
import nav from "@/data/nav";
import socials from "@/data/socials";
import { navigateTo } from "@/utils/navigateTo";
import { scrollTo } from "@/utils/scrollTo";

export default {
  name: "NavSection",
  data() {
    return {
      nav: nav.items,
      socials: socials.socials,
    };
  },
  methods: {
    navigateTo(url) {
      navigateTo(url);
    },
    scrollTo(selector) {
      scrollTo(selector);
    },
  },
};
</script>

<style>
.nav > .nav__list > .nav__item {
  cursor: pointer;
}

.main-header > .header-utilities {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 2rem;
}

.main-header > .header-utilities > .nav {
  background-color: var(--background-color);
  color: var(--primary-text-color);
  position: fixed;
  flex-direction: column;
  inset: 0;
  height: 100vh;
  width: 100%;
  padding: 8rem 3rem 0 3rem;
  margin: 0;
  visibility: hidden;
  opacity: 0;
  transform: translateY(-25px);
  transition: all ease-out 0.2s;
  z-index: 1000;
}

.main-header > .header-utilities > .nav.show {
  visibility: visible;
  opacity: 1;
  transform: translateY(0px);
}

.main-header > .header-utilities > .nav > .nav__list > .nav__item {
  display: flex;
  width: 100%;
  color: var(--primary-text-color);
  font-size: calc(var(--font-size) * 0.9);
  font-weight: var(--font-regular);
  border-bottom: 1px solid var(--foreground-color);
  padding: 1rem 0;
  text-decoration: none;
}

.footer > .nav > .nav__list {
  display: flex;
  gap: 20px;
  flex-direction: column;
  padding: 2rem;
  margin: 0;
}

.footer > .nav > .nav__list > .nav__item {
  display: flex;
  width: fit-content;
  color: var(--background-color);
  font-size: calc(var(--font-size) * 0.8);
  text-decoration: underline;
}

.footer > .nav > .nav__list > .nav__item:hover {
  text-decoration: none;
}

.nav__social-media {
  display: flex;
  align-items: center;
  justify-content: center;
  margin: 3rem 0 0 0;
  gap: 1rem;
}

.nav__social-media--link {
  color: var(--primary-text-color);
  background: none;
  border: none;
  width: fit-content;
  cursor: pointer;
  opacity: 0.8;
  z-index: 2;
}

.nav__social-media--link:hover {
  opacity: 1;
}

.nav__social-media--icon {
  height: 25px;
  width: 25px;
  object-fit: cover;
  border-radius: 50%;
  pointer-events: none;
}

.footer > .nav {
  padding: 2rem;
}

.footer > .nav > .nav__list {
  padding: 0;
}

.footer > * > .nav__social-media {
  margin-top: 2rem;
}

@media only screen and (min-width: 768px) {
  .main-header > .header-utilities {
    flex-direction: row-reverse;
  }

  .main-header > .header-utilities > .nav {
    position: static;
    padding: 0;
    margin: 0;
    height: fit-content;
    width: fit-content;
    transition: none;
  }

  .main-header > .header-utilities > .nav > .nav__list {
    display: flex;
    gap: 30px;
  }

  .main-header > .header-utilities > .nav > .nav__list > .nav__item {
    font-size: calc(var(--font-size) * 0.8);
    font-weight: var(--font-bold);
    border-bottom-width: 2px;
    padding: 0.2rem 0;
    transition: all ease-out 0.2s;
    width: fit-content;
  }

  .main-header > .header-utilities > .nav > .nav__list > .nav__item:hover {
    border-bottom-color: var(--primary-color);
  }

  .footer > .nav > .nav__list {
    align-items: center;
  }

  .nav__social-media {
    display: none;
  }
}
</style>
