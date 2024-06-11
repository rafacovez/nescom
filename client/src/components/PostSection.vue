<template>
  <ComponentLayout>
    <div v-if="post && author" class="post">
      <div class="post__header">
        <h1 class="post__heading">{{ post.title }}</h1>
        <div
          v-show="userData && userData.role === 'admin'"
          class="post__actions"
        >
          <CustomButton
            @click="deletePost"
            class="post__actions-button post__delete"
            :isPrimary="true"
          >
            <font-awesome-icon
              icon="fas fa-trash-can"
              class="post__actions-icon post__delete-icon"
            />
          </CustomButton>
          <router-link :to="'/publicar?id=' + post._id">
            <CustomButton class="post__actions-button post__edit">
              <font-awesome-icon
                icon="fas fa-pen-to-square"
                class="post__actions-icon post__edit-icon"
              />
            </CustomButton>
          </router-link>
          <CustomButton
            v-if="post.status === 'published'"
            @click="archivePost"
            class="post__actions-button post__archive"
          >
            <font-awesome-icon
              icon="fas fa-box-archive"
              class="post__actions-icon post__archive-icon"
            />
          </CustomButton>
          <CustomButton
            v-else
            @click="publishPost"
            class="post__actions-button post__publish"
            :isPrimary="true"
          >
            Publicar
          </CustomButton>
        </div>
      </div>
      <div class="post__author">
        <UserPicture
          :profilePicSrc="author.profilePicture"
          :userDisplayName="author.displayName"
        />
        <p class="post__info">
          Publicado por
          <strong>{{ author.displayName }}</strong>
          en
          {{ formatCreatedAt(post.createdAt) }}
        </p>
      </div>
      <span class="post__divider"></span>
      <p class="post__content">{{ post.content }}</p>
    </div>
    <div v-else></div>
  </ComponentLayout>
</template>

<script>
import ComponentLayout from "@/layouts/ComponentLayout.vue";
import UserPicture from "./UserPicture.vue";
import CustomButton from "./CustomButton.vue";
import { mapState } from "vuex";
import axiosInstance from "@/axios-instance";

export default {
  name: "PostSection",
  data() {
    return {
      post: null,
      author: null,
    };
  },
  computed: {
    ...mapState({
      userData: (state) => state.userData,
    }),
  },
  components: {
    ComponentLayout,
    CustomButton,
    UserPicture,
  },
  mounted() {
    this.getPost();
  },
  methods: {
    // getPost() {
    //   fetch(
    //     `${process.env.VUE_APP_URL}/api/posts/getPostByURL/${this.$route.params.postURL}`,
    //     {
    //       method: "GET",
    //     }
    //   )
    //     .then((response) => {
    //       if (response.status === 404) {
    //         this.$router.push("/404");
    //       } else if (!response.ok) {
    //         throw new Error("Error fetching post data");
    //       }
    //       return response.json();
    //     })
    //     .then(async (data) => {
    //       const authorData = await this.getAuthor(data.author);
    //       return [data, authorData];
    //     })
    //     .then((data) => {
    //       this.post = data[0];
    //       this.author = data[1];
    //     })
    //     .catch((error) => {
    //       console.error(error);
    //     });
    // },
    async getPost() {
      try {
        const response = await axiosInstance.get(
          `/api/posts/getPostByURL/${this.$route.params.postURL}`
        );

        const data = response.data;
        const authorData = await this.getAuthor(data.author);

        this.post = data;
        this.author = authorData;
      } catch (error) {
        if (error.response && error.response.status === 404) {
          this.$router.push("/404");
        } else {
          console.error("Error fetching post data", error);
        }
      }
    },
    // getAuthor(authorId) {
    //   return fetch(`${process.env.VUE_APP_URL}/api/users?id=${authorId}`, {
    //     method: "GET",
    //   })
    //     .then((response) => {
    //       if (!response.ok) {
    //         throw new Error("Error fetching author user data");
    //       }
    //       return response.json();
    //     })
    //     .then((data) => {
    //       return data[0];
    //     })
    //     .catch((error) => {
    //       console.error(error);
    //     });
    // },
    async getAuthor(authorId) {
      try {
        const response = await axiosInstance.get(`/api/users?id=${authorId}`);

        const data = response.data;
        return data[0];
      } catch (error) {
        console.error("Error fetching author user data", error);
      }
    },
    formatCreatedAt(dateString) {
      const date = new Date(dateString);
      const day = date.getDate();
      const month = date.getMonth() + 1;
      const year = date.getFullYear();

      return `${day}/${month}/${year}`;
    },
    // archivePost() {
    //   const post = {
    //     status: "archived",
    //   };

    //   fetch(
    //     `${process.env.VUE_APP_URL}/api/posts/updatePostById/${this.post._id}`,
    //     {
    //       method: "POST",
    //       headers: {
    //         "Content-Type": "application/json",
    //       },
    //       body: JSON.stringify(post),
    //     }
    //   )
    //     .then((response) => {
    //       if (!response.ok) {
    //         throw new Error("Failed update post");
    //       } else {
    //         this.$router.push("/blog");
    //       }
    //     })
    //     .catch((error) => {
    //       console.error(error);
    //     });
    // },
    async archivePost() {
      const post = {
        status: "archived",
      };

      try {
        const response = await axiosInstance.post(
          `/api/posts/updatePostById/${this.post._id}`,
          post,
          {
            headers: {
              "Content-Type": "application/json",
            },
          }
        );

        if (response.status !== 200) {
          throw new Error("Failed update post");
        } else {
          this.$router.push("/blog");
        }
      } catch (error) {
        console.error(error);
      }
    },
    // deletePost() {
    //   fetch(
    //     `${process.env.VUE_APP_URL}/api/posts/deletePostById/${this.post._id}`,
    //     {
    //       method: "DELETE",
    //     }
    //   )
    //     .then((response) => {
    //       if (!response.ok) {
    //         throw new Error("Failed update post");
    //       } else {
    //         this.$router.push("/blog");
    //       }
    //     })
    //     .catch((error) => {
    //       console.error(error);
    //     });
    // },
    async deletePost() {
      try {
        const response = await axiosInstance.delete(
          `/api/posts/deletePostById/${this.post._id}`
        );

        // Axios does not have a property called "ok". It throws an error for non-2xx responses.
        if (response.status !== 200) {
          throw new Error("Failed to delete post");
        } else {
          this.$router.push("/blog");
        }
      } catch (error) {
        console.error(error);
      }
    },
    // publishPost() {
    //   const post = {
    //     status: "published",
    //   };

    //   fetch(
    //     `${process.env.VUE_APP_URL}/api/posts/updatePostById/${this.post._id}`,
    //     {
    //       method: "POST",
    //       headers: {
    //         "Content-Type": "application/json",
    //       },
    //       body: JSON.stringify(post),
    //     }
    //   )
    //     .then((response) => {
    //       if (!response.ok) {
    //         throw new Error("Failed update post");
    //       } else {
    //         this.$router.push("/blog");
    //       }
    //     })
    //     .catch((error) => {
    //       console.error(error);
    //     });
    // },
    async publishPost() {
      const post = {
        status: "published",
      };

      try {
        const response = await axiosInstance.post(
          `/api/posts/updatePostById/${this.post._id}`,
          post,
          {
            headers: {
              "Content-Type": "application/json",
            },
          }
        );

        if (response.status !== 200) {
          throw new Error("Failed update post");
        } else {
          this.$router.push("/blog");
        }
      } catch (error) {
        console.error(error);
      }
    },
  },
};
</script>

<style>
.post__header {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  margin-bottom: 1rem;
  gap: 1rem;
}

.post__heading {
  font-size: calc(var(--font-size) * 2.2);
  color: var(--primary-text-color);
}

.post__actions {
  display: flex;
  gap: 1rem;
}

.post__actions-button {
  padding: 0.5rem 1rem;
  max-width: fit-content;
}

.post__actions-icon {
  width: 20px;
}

.post__edit > a {
  text-decoration: none;
  color: var(--primary-text-color);
}

.post__author {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.post__info {
  font-size: calc(var(--font-size) * 0.8);
  color: var(--secondary-text-color);
}

.post__content {
  color: var(--primary-text-color);
}

.post__divider {
  display: block;
  height: 1px;
  width: 100%;
  background-color: var(--foreground-color);
  margin: 1rem 0;
}

@media only screen and (min-width: 768px) {
  .post__header {
    flex-direction: row;
    align-items: center;
  }
}
</style>
