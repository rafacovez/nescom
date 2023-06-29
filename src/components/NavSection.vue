<template>
  <nav class="nav">
    <ul>
      <li v-for="item in nav" :key="item.id" @click="scrollTo(item.ref)">
        {{ item.name }}
      </li>
      <li>
        <a
          href="https://www.porlalinea.com.do/secciones/en-conexion/con-nestor-estevez/"
        >
          Blog | Néstor Estévez
          <ArrowUpRight class="icon" />
        </a>
      </li>
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
        <object
          :data="getSocialLogo(social.name)"
          type="image/svg+xml"
          class="nav__social-media--icon"
        ></object>
      </button>
    </div>
  </nav>
</template>

<script>
import ArrowUpRight from "@/assets/icons/ArrowUpRight.vue";
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
  components: {
    ArrowUpRight,
  },
  methods: {
    navigateTo(url) {
      navigateTo(url);
    },
    scrollTo(selector) {
      scrollTo(selector);
    },
    getSocialLogo(social) {
      return require(`../assets/${social}Logo.svg`);
    },
  },
};
</script>

<style>
.header > .nav {
  background-color: var(--white);
  color: var(--black);
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
  z-index: 100;
}

.header > .nav.show {
  visibility: visible;
  opacity: 1;
  transform: translateY(0px);
}

.header > .nav > ul {
  margin: 0;
  padding: 0;
}

.header > .nav > ul > li {
  color: var(--black);
  font-size: calc(var(--font-size) * 0.9);
  font-weight: var(--font-regular);
  border-bottom: 1px solid var(--gray);
  padding: 1rem 0;
  list-style: none;
  cursor: pointer;
}

.header > .nav > ul > li > a {
  display: flex;
  gap: 0.2rem;
  color: var(--black);
  text-decoration: none;
  width: 100%;
}

.footer > .nav > ul {
  display: flex;
  flex-direction: column;
  gap: 1rem;
  padding: 2rem;
  margin: 0;
}

.footer > .nav > ul > li {
  font-size: calc(var(--font-size) * 0.8);
  text-decoration: underline;
  width: fit-content;
  padding: 0;
  margin: 0;
  cursor: pointer;
}

.footer > .nav > ul > li > a {
  display: flex;
  gap: 0.2rem;
}

.footer > .nav > ul > li:hover,
.footer > .nav > ul > li > a:hover {
  text-decoration: none;
}

.footer > .nav > ul > li > a {
  text-decoration: none;
  width: fit-content;
  color: var(--white);
}

.nav__social-media {
  display: flex;
  align-items: center;
  justify-content: center;
  margin: 3rem 0 0 0;
  gap: 1rem;
}

.nav__social-media--link {
  background: none;
  border: none;
  width: fit-content;
  cursor: pointer;
  opacity: 0.5;
  z-index: 2;
}

.nav__social-media--link:hover {
  opacity: 1;
}

.nav__social-media--icon {
  height: 30px;
  width: 30px;
  object-fit: cover;
  border-radius: 50%;
  pointer-events: none;
}

.footer > .nav {
  padding: 2rem;
}

.footer > .nav > ul {
  padding: 0;
}

.footer > * > .nav__social-media {
  margin-top: 2rem;
}

@media only screen and (min-width: 768px) {
  .header > .nav {
    position: static;
    padding: 0;
    margin: 0;
    height: fit-content;
    width: fit-content;
  }

  .header > .nav > ul {
    display: flex;
    gap: 2rem;
  }

  .header > .nav > ul > li {
    font-size: calc(var(--font-size) * 0.8);
    font-weight: var(--font-bold);
    border-bottom-width: 2px;
    padding: 0.2rem 0;
    transition: all ease-out 0.2s;
  }

  .header > .nav > ul > li:hover {
    border-bottom-color: var(--red);
  }

  .footer > .nav > ul {
    align-items: center;
  }

  .nav__social-media {
    display: none;
  }
}
</style>
