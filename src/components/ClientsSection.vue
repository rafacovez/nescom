<template>
  <ComponentLayout class="clients-section">
    <h3 class="clients-section__heading">Nuestros clientes</h3>
    <div class="clients-wrapper">
      <button
        class="clients-wrapper__client"
        role="link"
        tabindex="0"
        v-for="client in clients"
        :key="client.id"
        :aria-label="`Visit ${client.name} website`"
        @click="navigateTo(client.url)"
      >
        <img v-lazy="getLogoSrc(client)" :alt="`${client.name} logo`" />
      </button>
      <router-link
        to="/contacto"
        aria-label="Go to contact page"
        class="clients-wrapper__client"
      >
        <p>Tu entidad aquí</p>
      </router-link>
    </div>
  </ComponentLayout>
</template>

<script>
import clients from "@/data/clients.json";
import ComponentLayout from "@/layouts/ComponentLayout.vue";

export default {
  name: "ClientsSection",
  data() {
    return {
      clients: clients.clients,
    };
  },
  components: {
    ComponentLayout,
  },
  methods: {
    scrollTo(selector) {
      const element = document.querySelector(selector);
      element.scrollIntoView({ behavior: "smooth" });
    },
    navigateTo(url) {
      window.open(url, "_blank");
    },
    getLogoSrc(client) {
      const logo = client.name.toLowerCase().replace(/\s+/g, "-");
      return require(`../assets/${logo}.webp`);
    },
  },
};
</script>

<style>
.clients-wrapper {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 0.5rem;
}

.clients-wrapper__client {
  display: grid;
  place-items: center;
  background-color: var(--gray);
  color: var(--black);
  border: 1px solid var(--gray);
  height: 100px;
  padding: 1rem;
  margin: 0;
  border-radius: var(--border-radius-sm);
  cursor: pointer;
  filter: grayscale(100%);
  text-decoration: none;
  transition: all ease-out 0.2s;
  overflow: hidden;
}

.clients-wrapper__client:hover {
  background-color: var(--white);
  filter: grayscale(0%);
}

.clients-wrapper__client > img {
  max-width: 100px;
  width: 100%;
  margin: 0 auto;
}
</style>
