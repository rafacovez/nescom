<template>
  <ComponentLayout id="servicesSection" class="services-section">
    <h3>Nuestros servicios</h3>
    <article class="services-wrapper">
      <section class="service master-of-ceremony">
        <h4>Maestría de ceremonias</h4>
        <p>
          Cuando organizas una actividad, el papel de quien conduce se vuelve
          determinante para el éxito o el fracaso de la misma.
        </p>
      </section>
      <section class="service communication">
        <h4>Consultoría en comunicación</h4>
        <p>
          Siempre necesitaremos comunicarnos. ¿Cómo te comunicas? ¿Lo quieres
          mejorar? Nosotros podemos ayudarte.
        </p>
      </section>
      <section class="service commercial-voice">
        <h4>Voz comercial</h4>
        <p>
          Cada mensaje ha iniciado como idea que pasa por diversos procesos.
          Nosotros disponemos de la capacidad para hacer más impactante tu
          mensaje.
        </p>
      </section>
      <section class="service public-relations">
        <h4>Relaciones públicas</h4>
        <p>
          En un mundo tan cambiante, el esfuerzo planeado para influenciar la
          opinión es determinante para iniciar, mantener o mejorar fructíferas
          relaciones.
        </p>
      </section>
      <section class="service voiceover">
        <h4>Oratoria y locución</h4>
        <p>
          El adecuado manejo de la palabra marca la diferencia. Para quienes
          tienen sueños o ideas por realizar, la oratoria se vuelve una especie
          de llave maestra.
        </p>
      </section>
    </article>
  </ComponentLayout>
</template>

<script>
import ComponentLayout from "@/layouts/ComponentLayout.vue";

export default {
  name: "ServicesSection",
  components: {
    ComponentLayout,
  },
};
</script>

<style>
.services-section > h3 {
  margin-bottom: 2rem;
}

.services-wrapper {
  display: grid;
  gap: 2rem;
}

.service {
  position: relative;
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
  border: 2px solid var(--red);
  border-radius: 4px;
  color: var(--white);
  padding: 1rem;
  height: 250px;
  z-index: 25;
}

.service::after {
  position: absolute;
  inset: 0;
  content: "";
  height: 100%;
  width: 100%;
  display: block;
  border-radius: inherit;
  background-color: var(--black);
  opacity: 0.8;
  transition: all ease-out 0.2s;
  z-index: -25;
}

.service.master-of-ceremony {
  background-image: url("../assets/services/master-of-ceremony.jpg");
}

.service.communication {
  background-image: url("../assets/services/communication.jpg");
}

.service.commercial-voice {
  background-image: url("../assets/services/commercial-voice.jpg");
}

.service.public-relations {
  background-image: url("../assets/services/public-relations.jpg");
}

.service.voiceover {
  background-image: url("../assets/services/voiceover.jpg");
}

.service > * {
  margin: 0 0 1rem 0;
  transition: all ease-out 0.2s;
  z-index: 50;
}

.service:hover::after {
  opacity: 0;
}

.service:hover > * {
  opacity: 0;
  visibility: hidden;
}
</style>
