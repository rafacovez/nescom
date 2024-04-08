<template>
  <ComponentLayout class="services-section">
    <h2>Nuestros servicios</h2>
    <article class="services-wrapper">
      <section
        v-for="service in services"
        :key="service.id"
        :class="`service ${toKebabCase(service.name)}`"
        :aria-label="`Detalles sobre el servicio de ${service.heading}`"
      >
        <img
          class="service__img"
          v-lazy="getImgSrc(service.name)"
          :alt="service.heading"
        />
        <h3 class="service__heading">{{ service.heading }}</h3>
        <p class="service__paragraph">{{ service.description }}</p>
      </section>
    </article>
  </ComponentLayout>
</template>

<script>
import ComponentLayout from "@/layouts/ComponentLayout.vue";
import services from "../data/services.json";

export default {
  name: "ServicesSection",
  data() {
    return {
      services: services.services,
    };
  },
  components: {
    ComponentLayout,
  },
  methods: {
    toKebabCase(target) {
      const kebab = target.toLowerCase().replace(/\s+/g, "-");
      return kebab;
    },
    getImgSrc(target) {
      const logo = this.toKebabCase(target);
      return require(`../assets/${logo}.webp`);
    },
  },
};
</script>

<style>
.services-wrapper {
  display: grid;
  gap: 2rem;
}

.service {
  position: relative;
  border: 2px solid var(--primary-color);
  border-radius: var(--border-radius-sm);
  color: var(--background-color);
  margin: 0;
  padding: 1rem;
  height: 250px;
  width: 100%;
  overflow: hidden;
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.service::after {
  content: "";
  display: block;
  height: 100%;
  width: 100%;
  position: absolute;
  inset: 0;
  background-color: var(--secondary-text-color);
  opacity: 0.8;
  z-index: -25;
  transition: all ease-out 0.2s;
}

.service__img {
  position: absolute;
  inset: 0;
  object-fit: cover;
  height: 100%;
  width: 100%;
  z-index: -50;
}

.service__paragraph {
  font-size: calc(var(--font-size) * 0.9);
}

.service:hover::after {
  opacity: 0.9;
}

@media only screen and (min-width: 1080px) {
  .services-wrapper {
    grid-template-columns: 1fr 1fr 1fr 1fr 1fr;
    gap: 0;
    place-content: center;
    margin: 4rem 0;
  }

  .service {
    height: 400px;
    width: 250px;
    padding: 2rem;
    margin: -0.75rem;
    transition: all ease-out 0.2s;
  }

  .commercial-voice {
    transform: scale(1);
    z-index: 15;
  }

  .communication,
  .public-relations {
    transform: scale(0.95);
    z-index: 10;
  }

  .master-of-ceremony,
  .voiceover {
    transform: scale(0.9);
    z-index: 5;
  }

  .service:hover {
    transform: scale(1.05);
    z-index: 20;
  }
}
</style>
