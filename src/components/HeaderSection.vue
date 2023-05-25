<template>
  <header class="header">
    <img class="logo" :src="logoPath" alt="Nescom RD" />
    <button @click="toggleNav" class="nav__button" :class="{ x: navOpen }">
      <span></span>
    </button>
    <nav class="nav" :class="{ show: navOpen }">
      <li>¿Quiénes somos?</li>
      <li>Servicios</li>
      <li>Clientes</li>
      <li>Néstor Estévez</li>
      <li>Publicaciones</li>
    </nav>
  </header>
</template>

<script>
import logo from "../assets/logo.png";

export default {
  name: "HeaderSection",
  data() {
    return {
      logoPath: logo,
      navOpen: false,
    };
  },
  methods: {
    toggleNav() {
      this.navOpen = !this.navOpen;
    },
  },
};
</script>

<style>
.header {
  display: flex;
  justify-content: space-between;
  padding: 1rem;
  background-color: var(--red);
}

.logo {
  max-width: 30px;
}

.nav {
  position: fixed;
  flex-direction: column;
  background-color: var(--red);
  color: var(--white);
  top: 62px;
  left: 0;
  width: 100%;
  padding: 2rem;
  margin: 0;
  visibility: hidden;
  opacity: 0;
  transform: translateY(-25px);
  transition: all ease-out 0.2s;
}

.nav.show {
  visibility: visible;
  opacity: 1;
  transform: translateY(0px);
}

.nav > li {
  font-size: calc(var(--font-size) * 0.9);
  font-weight: var(--font-bold);
  list-style: none;
  border-bottom: 1px solid var(--gray);
  padding: 1rem 0;
}

.nav__button {
  background: none;
  border: none;
  padding: 0;
  margin: 0;
  cursor: pointer;
}

.nav__button > span {
  width: 20px;
  height: 2px;
  background-color: var(--white);
  display: block;
  position: relative;
  transition: all ease-out 0.2s;
}

.nav__button > span::before {
  content: "";
  width: 100%;
  height: 100%;
  background-color: var(--white);
  display: inherit;
  position: absolute;
  top: -8px;
  transition: inherit;
}

.nav__button > span::after {
  content: "";
  width: 100%;
  height: 100%;
  background-color: var(--white);
  display: inherit;
  position: absolute;
  top: 8px;
  transition: inherit;
}

.nav__button.x > span {
  transform: translateX(10px);
  background-color: rgba(255, 0, 0, 0);
}

.nav__button.x > span::before {
  transform: translate(-10px, 8px) rotate(45deg);
}

.nav__button.x > span::after {
  transform: translate(-10px, -8px) rotate(-45deg);
}
</style>
