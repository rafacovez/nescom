<template>
  <ComponentLayout class="blog-section">
    <div class="blog-section__header">
      <h3>Blog</h3>
      <span v-if="$route.path === '/'">&mdash;</span>
      <router-link class="link" to="/blog" v-if="$route.path === '/'"
        >Ver todas las publicaciones</router-link
      >
    </div>
    <div class="blog-section__posts-wrapper">
      <div class="blog-section__post blog-section__post--primary"></div>
      <div class="blog-section__post blog-section__post--a"></div>
      <div class="blog-section__post blog-section__post--b"></div>
      <div class="blog-section__post blog-section__post--c"></div>
    </div>
  </ComponentLayout>
</template>

<script>
import ComponentLayout from "@/layouts/ComponentLayout.vue";

export default {
  name: "BlogSection",
  components: {
    ComponentLayout,
  },
};
</script>

<style>
.blog-section__header {
  display: flex;
  align-items: flex-start;
  gap: 0.5rem;
}

.blog-section__posts-wrapper {
  display: grid;
  grid-template-areas:
    "primary"
    "a"
    "b"
    "c";
  gap: 1rem;
}

.blog-section__post {
  min-height: 200px;
}

.blog-section__post--primary {
  grid-area: primary;
  background-color: var(--red);
}

.blog-section__post--a {
  grid-area: a;
  background-color: var(--red);
}

.blog-section__post--b {
  grid-area: b;
  background-color: var(--red);
}

.blog-section__post--c {
  grid-area: c;
  background-color: var(--red);
}

@media only screen and (min-width: 768px) {
  .blog-section__posts-wrapper {
    grid-template-areas:
      "primary primary primary a"
      "primary primary primary b"
      "primary primary primary c";
    height: 400px;
  }

  .blog-section__post {
    min-height: 0;
  }
}
</style>
