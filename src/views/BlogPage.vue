<template>
  <SocialMediaModal />
  <BlogSection />
</template>

<script>
import BlogSection from "@/components/BlogSection.vue";
import SocialMediaModal from "@/components/SocialMediaModal.vue";

export default {
  name: "BlogPage",
  components: {
    BlogSection,
    SocialMediaModal,
  },
};
</script>
