<template>
  <div>
    <SocialMediaModal />
    <PostsListSection />
  </div>
</template>

<script>
import PostsListSection from "@/components/PostsListSection.vue";
import SocialMediaModal from "@/components/SocialMediaModal.vue";

export default {
  name: "BlogPage",
  components: {
    PostsListSection,
    SocialMediaModal,
  },
};
</script>
