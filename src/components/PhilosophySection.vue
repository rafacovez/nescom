<template>
  <article id="philosophySection" class="philosophy-section">
    <section class="mission">
      <h3>Lorem.</h3>
      <p>
        Lorem ipsum dolor sit amet consectetur adipisicing elit. Obcaecati
        recusandae nam ex! Recusandae, sed esse.
      </p>
    </section>
    <section class="vision">
      <h3>Lorem.</h3>
      <p>
        Lorem ipsum dolor sit amet consectetur adipisicing elit. Obcaecati
        recusandae nam ex! Recusandae, sed esse.
      </p>
    </section>
    <section class="values">
      <h3>Lorem.</h3>
      <p>
        Lorem ipsum dolor sit amet consectetur adipisicing elit. Obcaecati
        recusandae nam ex! Recusandae, sed esse.
      </p>
    </section>
  </article>
</template>

<script>
export default {
  name: "PhilosophySection",
};
</script>

<style>
.philosophy-section {
  display: flex;
  flex-direction: column;
  gap: 2rem;
  background-color: var(--red);
  color: var(--white);
  padding: 2rem;
  margin: 0;
}

.philosophy-section > section > h3 {
  margin: 0.5rem 0;
}

.philosophy-section > section > p {
  font-size: calc(var(--font-size) * 0.9);
}
</style>
