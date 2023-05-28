<template>
  <ComponentLayout class="clients-section">
    <h3 class="clients-section__heading">Nuestros clientes</h3>
    <div class="clients-wrapper">
      <button
        aria-label="Visit Coopsano website"
        class="clients-wrapper__client"
      >
        <img :src="coopsanoLogo" alt="Coopsano logo" />
      </button>
      <button
        aria-label="Visit Presidencia website"
        class="clients-wrapper__client"
      >
        <img :src="presidenciaLogo" alt="Presidencia logo" />
      </button>
      <button aria-label="Visit Intec website" class="clients-wrapper__client">
        <img :src="intecLogo" alt="Intec logo" />
      </button>
      <button
        aria-label="Visit German Cooperation website"
        class="clients-wrapper__client"
      >
        <img :src="germanCooperationLogo" alt="German Cooperation logo" />
      </button>
      <button
        aria-label="Visit Anpa RD website"
        class="clients-wrapper__client"
      >
        <img :src="anpardLogo" alt="Anpa logo" />
      </button>
      <button
        aria-label="Visit Banco Mundial website"
        class="clients-wrapper__client"
      >
        <img :src="bancoMundialLogo" alt="Banco Mundial logo" />
      </button>
      <button
        aria-label="Visit Infotep website"
        class="clients-wrapper__client"
      >
        <img :src="infotepLogo" alt="Infotep logo" />
      </button>
      <button
        aria-label="Visit Inter American Bank website"
        class="clients-wrapper__client"
      >
        <img :src="interAmericanBankLogo" alt="Inter American Bank logo" />
      </button>
      <button
        aria-label="Visit Isfodosu website"
        class="clients-wrapper__client"
      >
        <img :src="isfodosuLogo" alt="Isfodosu logo" />
      </button>
      <button
        aria-label="Visit Tropical website"
        class="clients-wrapper__client"
      >
        <img :src="tropicalLogo" alt="Tropical logo" />
      </button>
      <button
        aria-label="Visit Unicaribe website"
        class="clients-wrapper__client"
      >
        <img :src="unicaribeLogo" alt="Unicaribe logo" />
      </button>
      <button aria-label="Go to contact page" class="clients-wrapper__client">
        <p>Tu entidad aquí</p>
      </button>
    </div>
  </ComponentLayout>
</template>

<script>
import ComponentLayout from "@/layouts/ComponentLayout.vue";
import anpard from "../assets/anpa.png";
import bancoMundial from "../assets/banco-mundial.png";
import interAmericanBank from "../assets/inter-american-bank.png";
import coopsano from "../assets/coopsano.png";
import germanCooperation from "../assets/german-cooperation.png";
import infotep from "../assets/infotep.png";
import intec from "../assets/intec.png";
import isfodosu from "../assets/isfodosu.png";
import tropical from "../assets/tropical.png";
import unicaribe from "../assets/unicaribe.png";
import presidencia from "../assets/presidencia.png";

export default {
  name: "ClientsSection",
  data() {
    return {
      anpardLogo: anpard,
      bancoMundialLogo: bancoMundial,
      interAmericanBankLogo: interAmericanBank,
      coopsanoLogo: coopsano,
      germanCooperationLogo: germanCooperation,
      infotepLogo: infotep,
      intecLogo: intec,
      isfodosuLogo: isfodosu,
      tropicalLogo: tropical,
      unicaribeLogo: unicaribe,
      presidenciaLogo: presidencia,
    };
  },
  components: {
    ComponentLayout,
  },
};
</script>

<style>
.clients-section__heading {
  margin: 0 0 2rem 0;
}

.clients-wrapper {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 0.5rem;
}

.clients-wrapper__client {
  background-color: var(--gray);
  color: var(--black);
  border: 1px solid var(--gray);
  height: 100px;
  padding: 1rem;
  margin: 0;
  border-radius: 2px;
  filter: grayscale(100%);
  cursor: pointer;
  transition: all ease-out 0.2s;
}

.clients-wrapper__client:hover {
  background-color: var(--white);
  filter: grayscale(0%);
}

.clients-wrapper__client:focus {
  color: var(--black);
}

.clients-wrapper__client > img {
  width: 100%;
  margin: 0 auto;
}
</style>
