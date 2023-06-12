<template>
  <footer class="footer">
    <ul>
      <li @click="scrollTo('#philosophySection')">¿Quiénes somos?</li>
      <li @click="scrollTo('#servicesSection')">Servicios</li>
      <li @click="scrollTo('#clientsSection')">Clientes</li>
      <li @click="scrollTo('#contactSection')">Contacto</li>
      <li @click="toggleNav()">
        <a
          href="https://www.porlalinea.com.do/secciones/en-conexion/con-nestor-estevez/"
        >
          Blog | Néstor Estévez <ArrowUpRightIcon class="icon" />
        </a>
      </li>
    </ul>

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
import { ArrowUpRightIcon } from "@heroicons/vue/20/solid";

export default {
  name: "FooterSection",
  components: {
    ArrowUpRightIcon,
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
  background-color: var(--gray);
  color: var(--white);
}

.footer > ul {
  display: flex;
  flex-direction: column;
  gap: 1rem;
  padding: 2rem;
  margin: 0;
}

.footer > ul > li {
  font-size: calc(var(--font-size) * 0.8);
  text-decoration: underline;
  width: fit-content;
  padding: 0;
  margin: 0;
  cursor: pointer;
}

.footer > ul > li > a {
  display: flex;
  gap: 0.2rem;
}

.footer > ul > li:hover,
.footer > ul > li > a:hover {
  text-decoration: none;
}

.footer > ul > li > a {
  text-decoration: none;
  width: fit-content;
  color: var(--white);
}

.footer > ul > li > a > .icon {
  width: 15px;
}

.sub-footer {
  display: flex;
  flex-direction: column;
  gap: 0.2rem;
  background-color: var(--white);
  padding: 1rem;
  text-align: center;
}

.sub-footer > p {
  color: var(--gray);
  font-size: calc(var(--font-size) * 0.7);
}

.sub-footer > p > a {
  color: var(--gray);
}

.sub-footer > p > a:hover {
  text-decoration: none;
}

@media only screen and (min-width: 768px) {
  .footer > ul {
    align-items: center;
  }
}
</style>
