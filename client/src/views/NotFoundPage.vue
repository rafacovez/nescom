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
      <h1 class="msg">Parece que la página que buscas no existe...</h1>
      <router-link to="/">
        <CustomButton :isPrimary="true">Volver al inicio</CustomButton>
      </router-link>
    </div>
  </ComponentLayout>
</template>

<script>
import ComponentLayout from "@/layouts/ComponentLayout.vue";
import CustomButton from "@/components/CustomButton.vue";
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
    CustomButton,
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
