<template>
  <HomePage />
</template>

<script>
import HomePage from "./HomePage.vue";

export default {
  name: "App",
  components: {
    HomePage,
  },
};
</script>

<style>
:root {
  --font-size: 1em;
  --font-regular: 400;
  --font-bold: 700;
  --font-family: "Poppins", sans-serif;
  --black: rgba(33, 33, 33);
  --gray: rgba(158, 152, 170);
  --dark-gray: rgb(129, 129, 129);
  --white: rgba(242, 242, 242);
  --red: rgba(237, 57, 56);
}

html {
  box-sizing: border-box;
}

*,
*::before,
*::after {
  box-sizing: inherit;
}

body {
  font-family: var(--font-family);
  font-size: var(--font-size);
  margin: 0;
  padding: 0;
}

h1,
h2,
h3,
h4,
h5 {
  font-weight: var(--font-bold);
  line-height: calc(var(--font-size) * 1);
  margin: 0;
  padding: 0;
}

p {
  font-weight: var(--font-regular);
  line-height: calc(var(--font-size) * 1.6);
  margin: 0;
  padding: 0;
}

ol,
ul {
  list-style: none;
}

input,
textarea,
button,
select {
  font: inherit;
}

img,
picture,
svg,
video,
object {
  display: block;
  max-width: 100%;
  height: auto;
}

.sr-only {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip: rect(0, 0, 0, 0);
  border: 0;
}
</style>
