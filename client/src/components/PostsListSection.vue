<template>
  <ComponentLayout class="posts-list">
    <h1>Todas las publicaciones</h1>
    <div
      v-show="userData && userData.role === 'admin'"
      class="posts-list__status-wrapper"
    >
      <CustomButton @click="goToPublished">Publicados</CustomButton>
      <CustomButton @click="goToDrafts">Borradores</CustomButton>
      <CustomButton @click="goToArchive">Archivados</CustomButton>
    </div>
    <router-link
      class="posts-list__post"
      v-for="(post, index) in posts"
      :key="index"
      :to="'/blog/post/' + post.url"
    >
      <h3>{{ post.title }}</h3>
    </router-link>
  </ComponentLayout>
</template>

<script>
import ComponentLayout from "@/layouts/ComponentLayout.vue";
import CustomButton from "./CustomButton.vue";
import { mapState } from "vuex";
import axiosInstance from "@/axios-instance";

export default {
  name: "PostsListSection",
  data() {
    return {
      posts: [],
      postsStatus: null,
    };
  },
  components: {
    ComponentLayout,
    CustomButton,
  },
  mounted() {
    this.postStatus = this.$route.query.status;

    if (!this.postsStatus) {
      this.goToPublished();
    } else {
      this.fetchPosts(this.postsStatus);
    }

    // if (!this.postStatus) {
    //   this.goToPublished();
    // } else {
    //   if (
    //     this.$route.query.status === "published" ||
    //     this.userData.role === "admin"
    //   ) {
    //     this.fetchPosts(this.$route.query.status);
    //   } else {
    //     this.$router.push("/404");
    //   }
    // }
  },
  methods: {
    // async fetchPosts(status) {
    //   await fetch(`${process.env.VUE_APP_URL}/api/posts?status=${status}`, {
    //     method: "GET",
    //   })
    //     .then((response) => {
    //       if (!response.ok) {
    //         throw new Error("Failed to fetch posts");
    //       }

    //       return response.json();
    //     })
    //     .then((data) => {
    //       this.posts = data;
    //     })
    //     .catch((error) => {
    //       console.error(error);
    //     });
    // },
    async fetchPosts(status) {
      try {
        const response = await axiosInstance.get(`/api/posts?status=${status}`);

        if (response.status !== 200) {
          throw new Error("Failed to fetch posts");
        }

        const data = response.data;
        this.posts = data;
      } catch (error) {
        console.error(error);
      }
    },
    async goToPublished() {
      await this.$router.push("/blog?status=published");
      this.fetchPosts(this.$route.query.status);
    },
    async goToDrafts() {
      await this.$router.push("/blog?status=draft");
      this.fetchPosts(this.$route.query.status);
    },
    async goToArchive() {
      await this.$router.push("/blog?status=archived");
      this.fetchPosts(this.$route.query.status);
    },
  },
  computed: {
    ...mapState({
      userData: (state) => state.userData,
    }),
  },
};
</script>

<style>
.posts-list__status-wrapper {
  display: flex;
  gap: 1rem;
  scroll-behavior: auto;
}

.posts-list__post {
  display: block;
  padding: 2rem 0;
  color: var(--primary-text-color);
  text-decoration-color: var(--primary-color);
  text-decoration-thickness: 2px;
}

.posts-list__post:not(:last-child) {
  border-bottom: 1px solid var(--foreground-color);
}
</style>
