<template>
  <div>
    <SocialMediaModal />
    <PostSection />
  </div>
</template>

<script>
import PostSection from "@/components/PostSection.vue";
import SocialMediaModal from "@/components/SocialMediaModal.vue";

export default {
  name: "BlogPost",
  components: {
    PostSection,
    SocialMediaModal,
  },
};
</script>
