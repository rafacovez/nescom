<template>
  <header class="header">
    <img class="logo" :src="logoPath" alt="Nescom RD" />
    <button class="nav__button">
      <span></span>
    </button>
  </header>
</template>

<script>
import logo from "../assets/logo.png";

export default {
  name: "HeaderSection",
  data() {
    return {
      logoPath: logo,
    };
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
  max-width: 50px;
}

.nav__button > span {
  width: 25px;
  height: 4px;
  background-color: var(--black);
  display: block;
  position: relative;
}

.nav__button > span::before {
  content: "";
  width: 100%;
  height: 100%;
  background-color: inherit;
  display: inherit;
  position: absolute;
  top: -8px;
}

.nav__button > span::after {
  content: "";
  width: 100%;
  height: 100%;
  background-color: inherit;
  display: inherit;
  position: absolute;
  top: 8px;
}
</style>
