<template>
  <div class="scroll-tracking">
    <div id="landing" class="section"></div>
    <div id="services" class="section"></div>
    <div id="philosophy" class="section"></div>
    <div id="clients" class="section"></div>
    <div id="contact" class="section"></div>
  </div>
</template>

<script>
export default {
  name: "ScrollTracking",
};
</script>

<style>
.scroll-tracking {
  position: fixed;
  top: 150px;
  left: 50px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 1rem;
  width: 20px;
  padding: 1rem;
  margin: 0;
  border-radius: 16px;
  z-index: 150;
}

.scroll-tracking > .section {
  position: relative;
  width: 10px;
  height: 10px;
  background-color: var(--white);
  border: 1px solid var(--gray);
  border-radius: 50%;
}

.scroll-tracking > .section:not(:last-child)::after {
  content: "";
  position: absolute;
  top: 110%;
  right: 0;
  left: 0;
  margin: 0 auto;
  padding: 0;
  height: 1rem;
  width: 1px;
  background-color: var(--gray);
}

.scroll-tracking > .section#landing {
  background-color: var(--red);
}
</style>
