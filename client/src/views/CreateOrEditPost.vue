<template>
  <ComponentLayout>
    <h1>Crea o edita tu publicación</h1>
    <CreatePostSection />
  </ComponentLayout>
</template>

<script>
import ComponentLayout from "@/layouts/ComponentLayout.vue";
import CreatePostSection from "@/components/CreatePostSection.vue";

export default {
  name: "CreatePost",
  components: {
    ComponentLayout,
    CreatePostSection,
  },
};
</script>
