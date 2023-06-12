<template>
  <ComponentLayout class="clients-section">
    <h3 class="clients-section__heading">Nuestros clientes</h3>
    <div class="clients-wrapper">
      <button
        @click="navigateToCoopsano"
        role="link"
        tabindex="0"
        aria-label="Visit Coopsano website"
        class="clients-wrapper__client"
      >
        <img v-lazy="coopsanoLogo" alt="Coopsano logo" />
      </button>
      <button
        @click="navigateToPresidencia"
        role="link"
        tabindex="0"
        aria-label="Visit Presidencia website"
        class="clients-wrapper__client"
      >
        <img v-lazy="presidenciaLogo" alt="Presidencia logo" />
      </button>
      <button
        @click="navigateToIntec"
        role="link"
        tabindex="0"
        aria-label="Visit Intec website"
        class="clients-wrapper__client"
      >
        <img v-lazy="intecLogo" alt="Intec logo" />
      </button>
      <button
        @click="navigateToGermanCooperation"
        role="link"
        tabindex="0"
        aria-label="Visit German Cooperation website"
        class="clients-wrapper__client"
      >
        <img v-lazy="germanCooperationLogo" alt="German Cooperation logo" />
      </button>
      <button
        @click="navigateToAnpa"
        role="link"
        tabindex="0"
        aria-label="Visit Anpa RD website"
        class="clients-wrapper__client"
      >
        <img v-lazy="anpardLogo" alt="Anpa logo" />
      </button>
      <button
        @click="navigateToWorldBank"
        role="link"
        tabindex="0"
        aria-label="Visit Banco Mundial website"
        class="clients-wrapper__client"
      >
        <img v-lazy="bancoMundialLogo" alt="Banco Mundial logo" />
      </button>
      <button
        @click="navigateToInfotep"
        role="link"
        tabindex="0"
        aria-label="Visit Infotep website"
        class="clients-wrapper__client"
      >
        <img v-lazy="infotepLogo" alt="Infotep logo" />
      </button>
      <button
        @click="navigateToInterAmericanBank"
        role="link"
        tabindex="0"
        aria-label="Visit Inter American Bank website"
        class="clients-wrapper__client"
      >
        <img v-lazy="interAmericanBankLogo" alt="Inter American Bank logo" />
      </button>
      <button
        @click="navigateToIsfodosu"
        role="link"
        tabindex="0"
        aria-label="Visit Isfodosu website"
        class="clients-wrapper__client"
      >
        <img v-lazy="isfodosuLogo" alt="Isfodosu logo" />
      </button>
      <button
        @click="navigateToTropical"
        role="link"
        tabindex="0"
        aria-label="Visit Tropical website"
        class="clients-wrapper__client"
      >
        <img v-lazy="tropicalLogo" alt="Tropical logo" />
      </button>
      <button
        @click="navigateToUnicaribe"
        role="link"
        tabindex="0"
        aria-label="Visit Unicaribe website"
        class="clients-wrapper__client"
      >
        <img v-lazy="unicaribeLogo" alt="Unicaribe logo" />
      </button>
      <button
        @click="scrollTo('#contactSection')"
        aria-label="Go to contact page"
        class="clients-wrapper__client"
      >
        <p>Tu entidad aquí</p>
      </button>
    </div>
  </ComponentLayout>
</template>

<script>
import ComponentLayout from "@/layouts/ComponentLayout.vue";
import anpard from "../assets/clients/anpa.webp";
import bancoMundial from "../assets/clients/banco-mundial.webp";
import interAmericanBank from "../assets/clients/inter-american-bank.webp";
import coopsano from "../assets/clients/coopsano.webp";
import germanCooperation from "../assets/clients/german-cooperation.webp";
import infotep from "../assets/clients/infotep.webp";
import intec from "../assets/clients/intec.webp";
import isfodosu from "../assets/clients/isfodosu.webp";
import tropical from "../assets/clients/tropical.webp";
import unicaribe from "../assets/clients/unicaribe.webp";
import presidencia from "../assets/clients/presidencia.webp";

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
  methods: {
    scrollTo(selector) {
      const element = document.querySelector(selector);
      element.scrollIntoView({ behavior: "smooth" });
    },
    navigateToCoopsano() {
      window.open("https://coopsano.com/", "_blank");
    },
    navigateToPresidencia() {
      window.open("https://presidencia.gob.do/", "_blank");
    },
    navigateToIntec() {
      window.open("https://www.intec.edu.do/", "_blank");
    },
    navigateToGermanCooperation() {
      window.open("https://www.giz.de/en/html/index.html", "_blank");
    },
    navigateToAnpa() {
      window.open("http://www.anpard.com/", "_blank");
    },
    navigateToWorldBank() {
      window.open("https://www.worldbank.org/en/home", "_blank");
    },
    navigateToInfotep() {
      window.open("https://www.infotep.gob.do/", "_blank");
    },
    navigateToInterAmericanBank() {
      window.open("https://www.iadb.org/en", "_blank");
    },
    navigateToIsfodosu() {
      window.open("https://isfodosu.edu.do/", "_blank");
    },
    navigateToTropical() {
      window.open("http://www.pinturastropical.com.do/site/", "_blank");
    },
    navigateToUnicaribe() {
      window.open("https://unicaribe.edu.do/", "_blank");
    },
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
  border-radius: var(--border-radius-sm);
  filter: grayscale(100%);
  cursor: pointer;
  transition: all ease-out 0.2s;
  overflow: hidden;
}

.clients-wrapper__client:hover {
  background-color: var(--white);
  filter: grayscale(0%);
}

.clients-wrapper__client:focus {
  color: var(--black);
}

.clients-wrapper__client > img {
  max-width: 100px;
  width: 100%;
  margin: 0 auto;
}

@media only screen and (min-width: 768px) {
  .clients-wrapper {
    grid-template-columns: 1fr 1fr 1fr 1fr;
  }
}
</style>
