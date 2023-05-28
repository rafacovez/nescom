<template>
  <ComponentLayout class="services-section">
    <article class="services-wrapper">
      <h3>Nuestros servicios</h3>
      <section class="service">
        <h4>Lorem, ipsum dolor.</h4>
        <p>
          Lorem ipsum dolor sit amet consectetur, adipisicing elit. Nihil fugit,
          labore id in laudantium vel.
        </p>
      </section>
      <section class="service">
        <h4>Lorem, ipsum dolor.</h4>
        <p>
          Lorem ipsum dolor sit amet consectetur, adipisicing elit. Nihil fugit,
          labore id in laudantium vel.
        </p>
      </section>
      <section class="service">
        <h4>Lorem, ipsum dolor.</h4>
        <p>
          Lorem ipsum dolor sit amet consectetur, adipisicing elit. Nihil fugit,
          labore id in laudantium vel.
        </p>
      </section>
      <section class="service">
        <h4>Lorem, ipsum dolor.</h4>
        <p>
          Lorem ipsum dolor sit amet consectetur, adipisicing elit. Nihil fugit,
          labore id in laudantium vel.
        </p>
      </section>
      <section class="service">
        <h4>Lorem, ipsum dolor.</h4>
        <p>
          Lorem ipsum dolor sit amet consectetur, adipisicing elit. Nihil fugit,
          labore id in laudantium vel.
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
.services-wrapper {
  display: grid;
  gap: 2rem;
}

.service {
  position: relative;
  background-image: url("../assets/services1.jpg");
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
  border: 2px solid var(--red);
  border-radius: 4px;
  color: var(--white);
  padding: 1rem;
  cursor: pointer;
  z-index: -50;
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
  z-index: -25;
}

.service > p {
  margin: 1rem 0;
  z-index: 50;
}
</style>
