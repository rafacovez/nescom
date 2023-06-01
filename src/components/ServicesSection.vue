<template>
  <ComponentLayout id="servicesSection" class="services-section">
    <h3>Nuestros servicios</h3>
    <article class="services-wrapper">
      <section class="service master-of-ceremony">
        <img v-lazy="masterOfCeremonyImg" alt="Maestría de ceremonias" />
        <h4>Maestría de ceremonias</h4>
        <p>
          Cuando organizas una actividad, el papel de quien conduce se vuelve
          determinante para el éxito o el fracaso de la misma.
        </p>
      </section>
      <section class="service communication">
        <img v-lazy="communicationImg" alt="Hand gesturing" />
        <h4>Consultoría en comunicación</h4>
        <p>
          Siempre necesitaremos comunicarnos. ¿Cómo te comunicas? ¿Lo quieres
          mejorar? Nosotros podemos ayudarte.
        </p>
      </section>
      <section class="service commercial-voice">
        <img v-lazy="commercialVoiceImg" alt="Microphone hanging up" />
        <h4>Voz comercial</h4>
        <p>
          Cada mensaje ha iniciado como idea que pasa por diversos procesos.
          Nosotros disponemos de la capacidad para hacer más impactante tu
          mensaje.
        </p>
      </section>
      <section class="service public-relations">
        <img v-lazy="publicRelationsImg" alt="Hands shaking" />
        <h4>Relaciones públicas</h4>
        <p>
          En un mundo tan cambiante, el esfuerzo planeado para influenciar la
          opinión es determinante para iniciar, mantener o mejorar fructíferas
          relaciones.
        </p>
      </section>
      <section class="service voiceover">
        <img v-lazy="voiceoverImg" alt="Microphone on air" />
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
import masterOfCeremony from "../assets/services/master-of-ceremony.webp";
import communication from "../assets/services/communication.webp";
import commercialVoice from "../assets/services/commercial-voice.webp";
import publicRelations from "../assets/services/public-relations.webp";
import voiceover from "../assets/services/voiceover.webp";

export default {
  name: "ServicesSection",
  data() {
    return {
      masterOfCeremonyImg: masterOfCeremony,
      communicationImg: communication,
      commercialVoiceImg: commercialVoice,
      publicRelationsImg: publicRelations,
      voiceoverImg: voiceover,
    };
  },
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
  border: 2px solid var(--red);
  border-radius: 4px;
  color: var(--white);
  margin: 0;
  padding: 1rem;
  height: 250px;
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
  background-color: var(--black);
  opacity: 0.8;
  z-index: -25;
  transition: all ease-out 0.1s;
}

.service > img {
  position: absolute;
  inset: 0;
  object-fit: cover;
  height: 100%;
  width: 100%;
  z-index: -50;
}

.service > h4,
.service > p {
  z-index: 50;
  transition: all ease-out 0.1s;
}

.service:hover::after,
.service:hover > h4,
.service:hover > p {
  opacity: 0;
  visibility: hidden;
}
</style>
