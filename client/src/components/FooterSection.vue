<template>
  <footer class="footer">
    <NavSection />
    <div class="sub-footer">
      <p>&copy; {{ copyrightYear }} Nescom, R. D.</p>
      <p>
        Liberado bajo la
        <a
          href="https://github.com/rafacovez/nescom/blob/main/LICENSE"
          target="_blank"
          >Licencia MIT</a
        >. Sitio web diseñado y desarrollado por
        <a href="https://github.com/rafacovez" target="_blank">Adán Estévez</a>
        usando <a href="https://vuejs.org/" target="_blank">Vue.js</a>.
      </p>
    </div>
  </footer>
</template>

<script>
import NavSection from "./NavSection.vue";

export default {
  name: "FooterSection",
  components: {
    NavSection,
  },
  data() {
    return {
      currentYear: 0,
      copyrightYear: "",
    };
  },
  created() {
    this.currentYear = new Date().getFullYear();
    if (this.currentYear > 2023) {
      this.copyrightYear = `2023 - ${this.currentYear}`;
    } else {
      this.copyrightYear = `${this.currentYear}`;
    }
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
.footer {
  background-color: var(--foreground-color);
  color: var(--background-color);
}

.footer > .nav > .nav__list > .nav__item {
  color: var(--primary-text-color);
}

.sub-footer {
  display: flex;
  flex-direction: column;
  gap: 0.2rem;
  background-color: var(--background-color);
  padding: 1rem;
  text-align: center;
}

.sub-footer > p {
  color: var(--secondary-text-color);
  font-size: calc(var(--font-size) * 0.7);
}

.sub-footer > p > a {
  color: inherit;
}

.sub-footer > p > a:hover {
  text-decoration: none;
}
</style>
