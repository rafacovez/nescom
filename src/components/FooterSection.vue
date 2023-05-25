<template>
  <footer class="footer">
    <ul>
      <li>item</li>
      <li>item</li>
      <li>item</li>
    </ul>
    <div class="sub-footer">
      <p>Copyright blah blah</p>
    </div>
  </footer>
</template>

<script>
export default {
  name: "FooterSection",
};
</script>

<style>
.footer {
  background-color: var(--dark-gray);
  color: var(--white);
}

.footer > ul {
  font-size: calc(var(--font-size) * 0.9);
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
  padding: 2rem;
  margin: 0;
}

.sub-footer {
  font-size: calc(var(--font-size) * 0.8);
  background-color: var(--black);
  color: var(--gray);
  padding: 2rem;
  text-align: center;
}
</style>
