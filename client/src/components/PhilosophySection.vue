<template>
  <article class="philosophy-section">
    <section class="mission">
      <h3>Misión</h3>
      <p>
        Somos una empresa dedicada a hacer más efectivas las
        <strong>relaciones</strong> entre nuestros clientes y sus asociados,
        agregando valor a sus procesos <strong>comunicacionales</strong>.
      </p>
    </section>
    <section class="vision">
      <h3>Visión</h3>
      <p>
        Ser una empresa referida por nuestros clientes como fuente de
        <strong>satisfacción</strong> y en crecimiento sostenido de cara a
        seguir agregando valor a la <strong>comunicación</strong>.
      </p>
    </section>
    <section class="values">
      <h3>Valores</h3>
      <p>
        servicio, <strong>eficiencia</strong>, calidad, proacción y entusiasmo
        inspiran a cada colaborador de nuestro equipo de
        <strong>profesionales</strong> y asociados.
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
  background-color: var(--primary-color);
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

@media only screen and (min-width: 768px) {
  .philosophy-section {
    flex-direction: row;
    gap: 4rem;
    justify-content: center;
  }

  .philosophy-section > section {
    text-align: center;
    max-width: 300px;
  }
}
</style>
