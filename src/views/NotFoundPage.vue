<template>
  <ComponentLayout class="container">
    <div class="illustration-wrapper">
      <img
        class="page-not-found-illustration"
        v-lazy="pageNotFoundPath"
        alt="Page Not Found"
      />
    </div>
    <div class="text-wrapper">
      <h1 class="msg">Oops! Parece que la página que buscas no existe...</h1>
      <router-link to="/">
        <PrimaryButtonVue>Volver al inicio</PrimaryButtonVue>
      </router-link>
    </div>
  </ComponentLayout>
</template>

<script>
import ComponentLayout from "@/layouts/ComponentLayout.vue";
import PrimaryButtonVue from "@/components/PrimaryButton.vue";
import pageNotFound from "@/assets/page-not-found.webp";

export default {
  name: "NotFoundPage",
  data() {
    return {
      pageNotFoundPath: pageNotFound,
    };
  },
  components: {
    ComponentLayout,
    PrimaryButtonVue,
  },
};
</script>

<style>
.msg {
  height: 100%;
  display: grid;
  place-items: center;
  gap: 2rem;
  text-align: center;
  margin-bottom: 2rem;
}

@media only screen and (min-width: 768px) {
  .container {
    display: flex;
    justify-content: center;
    align-items: center;
    padding: 0;
  }

  .msg {
    text-align: left;
    font-size: calc(var(--font-size) * 4);
  }
}
</style>
