<template>
  <div>
    <HeaderSection />
    <main>
      <slot>
        <router-view></router-view>
      </slot>
    </main>
    <FooterSection />
  </div>
</template>

<script>
import HeaderSection from "@/components/HeaderSection.vue";
import FooterSection from "@/components/FooterSection.vue";

export default {
  name: "App",
  components: {
    HeaderSection,
    FooterSection,
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
  --white: rgba(242, 242, 242);
  --primary-text-color: rgba(33, 33, 33);
  --secondary-text-color: rgb(50, 50, 50);
  --background-color: rgba(242, 242, 242);
  --foreground-color: rgba(158, 152, 170);
  --primary-color: rgba(237, 57, 56);
  --box-shadow-color: rgba(0, 0, 0, 0.2);
  --green: rgb(0, 165, 0);
  --red: rgb(211, 6, 6);
  --border-radius-sm: 4px;
  --border-radius-md: 32px;
  --z-index-back-sm: -100;
  --z-index-back-md: -50;
  --z-index-back-xl: -25;
  --z-index-neutral: 0;
  --z-index-front-sm: 25;
  --z-index-front-md: 50;
  --z-index-front-xl: 100;
  --z-index-front-xxl: 250;
}

[data-theme="dark"] {
  --primary-text-color: rgba(242, 242, 242);
  --secondary-text-color: rgba(158, 152, 170);
  --background-color: rgba(33, 33, 33);
  --foreground-color: rgb(50, 50, 50);
  --box-shadow-color: rgba(255, 255, 255, 0.1);
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
  background-color: var(--background-color);
  color: var(--primary-text-color);
  font-family: var(--font-family);
  font-size: var(--font-size);
  margin: 0;
  padding: 0;
}

body.no-scroll {
  overflow: hidden;
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
  margin: 0;
  padding: 0;
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

.link {
  font-size: var(--font-size);
  font-weight: var(--font-bold);
  color: var(--primary-color);
  text-decoration-color: var(--primary-color);
}

.link:hover {
  text-decoration: none;
}
</style>
