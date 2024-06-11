<template>
  <ComponentLayout class="blog-section">
    <div class="blog-section__header">
      <h3>Blog</h3>
      <span v-if="$route.path === '/'">&ndash;</span>
      <router-link class="link" to="/blog" v-if="$route.path === '/'"
        >Ver todas las publicaciones</router-link
      >
    </div>
    <div class="blog-section__posts-wrapper">
      <router-link
        v-for="(post, index) in latestPosts"
        :key="index"
        class="blog-section__post"
        :class="['blog-section__post--' + index]"
        :to="'/blog/post/' + post.url"
      >
        <img
          v-show="post.thumbnailImage !== ''"
          v-lazy="post.thumbnailImage"
          :alt="post.title"
          class="blog-section__post-thumbnail"
        />
        <h4 class="blog-section__post-title">{{ post.title }}</h4>
        <p
          class="blog-section__post-content"
          v-show="index < 1 && this.screenWidth > 768"
        >
          {{ post.content }}
        </p>
      </router-link>
    </div>
  </ComponentLayout>
</template>

<script>
import ComponentLayout from "@/layouts/ComponentLayout.vue";
import axiosInstance from "@/axios-instance";

export default {
  name: "BlogSection",
  components: {
    ComponentLayout,
  },
  data() {
    return {
      latestPosts: [],
      screenWidth: window.innerWidth,
    };
  },
  mounted() {
    this.fetchLatestPosts();
    // get screen width
    this.setScreenWidth();
    window.addEventListener("resize", this.setScreenWidth);
  },
  beforeUnmount() {
    window.removeEventListener("resize", this.setScreenWidth);
  },
  methods: {
    setScreenWidth() {
      this.screenWidth = window.innerWidth;
    },
    // fetchLatestPosts() {
    // fetch(`${process.env.VUE_APP_URL}/api/posts/getLatest`, {
    //   method: "GET",
    // })
    //   .then((response) => {
    //     if (!response.ok) {
    //       throw new Error("Failed to get posts");
    //     }
    //     return response.json();
    //   })
    //   .then((data) => {
    //     this.latestPosts = data;
    //   })
    //   .catch((error) => {
    //     console.error("Error getting posts:", error);
    //   });
    // },
    async fetchLatestPosts() {
      try {
        const response = await axiosInstance.get("/api/posts/getLatest");
        this.latestPosts = response.data;
      } catch (error) {
        console.error("Error getting posts:", error);
      }
    },
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
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.blog-section__post {
  min-height: 200px;
  background-color: var(--primary-color);
  border-radius: var(--border-radius-sm);
  text-decoration: none;
  display: flex;
  flex-direction: column;
  justify-content: flex-end;
  padding: 1rem;
  position: relative;
  z-index: 50;
  overflow: hidden;
}

.blog-section__post-thumbnail {
  position: absolute;
  inset: 0;
  height: 100%;
  width: 100%;
  z-index: -1;
}

/* .blog-section__post::after {
  content: "";
  display: block;
  height: 100%;
  width: 100%;
  position: absolute;
  inset: 0;
  background-color: var(--black);
  opacity: 0.5;
  z-index: -25;
  transition: all ease-out 0.2s;
} */

.blog-section__post-title {
  color: var(--white);
}

.blog-section__post-content {
  color: var(--white);
  margin: 1rem 0;
}

.blog-section__post--0 {
  grid-area: primary;
}

.blog-section__post--1 {
  grid-area: a;
}

.blog-section__post--2 {
  grid-area: b;
}

.blog-section__post--3 {
  grid-area: c;
}

@media only screen and (min-width: 768px) {
  .blog-section__posts-wrapper {
    display: grid;
    grid-template-areas:
      "primary primary primary a"
      "primary primary primary b"
      "primary primary primary c";
    height: 400px;
  }

  .blog-section__post {
    min-height: 0;
  }

  .blog-section__post:not(.blog-section__post--0) {
    max-width: 200px;
  }

  .blog-section__post--0 > .blog-section__post-title {
    font-size: calc(var(--font-size) * 1.5);
  }
}
</style>
