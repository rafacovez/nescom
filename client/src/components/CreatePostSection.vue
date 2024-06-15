<template>
  <form id="createPostForm" action="#" v-on:submit.prevent>
    <InputComponent
      :inputName="'Título'"
      :isRequired="true"
      :inputValue="inputValueTitle"
      @update:inputValue="(value) => (inputValueTitle = value)"
      :isFocused="isFocusedTitle"
      @update:isFocused="(value) => (isFocusedTitle = value)"
    />
    <p class="post-url">
      https://nescomrd.com/blog/post/{{ this.formattedUrl }}
    </p>
    <InputComponent
      :inputName="'Contenido'"
      :isTextarea="true"
      :isRequired="true"
      :inputValue="inputValueContent"
      @update:inputValue="(value) => (inputValueContent = value)"
      :isFocused="isFocusedContent"
      @update:isFocused="(value) => (isFocusedContent = value)"
    />
    <ThumbnailComponent
      :onInputChange="getImage"
      :thumbnailSrc="this.postThumbnailPreviewSrc"
      :thumbnailAlt="this.postThumbnailAlt"
      :isInput="true"
      :labelText="'Click aquí para añadir una portada'"
    />
    <div class="form-actions">
      <CustomButton @click="publishPost" :isPrimary="true">
        <input class="publish-button" type="submit" value="Publicar" />
      </CustomButton>
      <CustomButton @click="draftPost">
        <input class="draft-button" type="submit" value="Guardar" />
      </CustomButton>
    </div>
  </form>
</template>

<script>
import InputComponent from "@/components/InputComponent.vue";
import CustomButton from "@/components/CustomButton.vue";
import ThumbnailComponent from "./ThumbnailComponent.vue";
import { mapState } from "vuex";
import axiosInstance from "@/axios-instance";

export default {
  name: "CreateOrEditPostSection",
  components: {
    InputComponent,
    CustomButton,
    ThumbnailComponent,
  },
  data() {
    return {
      existentPostId: "",
      inputValueTitle: "",
      inputValueContent: "",
      isFocusedTitle: false,
      isFocusedContent: false,
      postThumbnail: null,
      postThumbnailPreviewSrc: "",
      postThumbnailKey: "",
      postThumbnailAlt: "",
      postThumbnailSrc: "",
    };
  },
  computed: {
    ...mapState({
      userData: (state) => state.userData,
    }),
    formattedUrl() {
      return this.inputValueTitle
        .trim()
        .normalize("NFD")
        .replace(/[\u0300-\u036f]/g, "")
        .toLowerCase()
        .replace(/[^\w\s]/g, "")
        .replace(/\s+/g, "-");
    },
  },
  mounted() {
    this.existentPostId = this.$route.query.id;

    if (this.existentPostId) {
      this.getPost(this.existentPostId);
    }
  },
  methods: {
    // getPost() {
    //   fetch(
    //     `${process.env.VUE_APP_URL}/api/posts/getPostById/${this.existentPostId}`,
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
    //     .then((data) => {
    //       this.inputValueTitle = data.title;
    //       this.inputValueContent = data.content;
    //       this.postThumbnailPreviewSrc = data.thumbnailImage;
    //     })
    //     .catch((error) => {
    //       console.error(error);
    //     });
    // },
    async getPost() {
      try {
        const response = await axiosInstance.get(
          `/api/posts/getPostById/${this.existentPostId}`
        );

        // Handle 404 error by redirecting to a 404 page
        if (response.status === 404) {
          this.$router.push("/404");
          return;
        }

        // Check if response is not OK (other than 404)
        if (!response.status === 200) {
          throw new Error("Error fetching post data");
        }

        // Extract data from the response
        const data = response.data;
        this.inputValueTitle = data.title;
        this.inputValueContent = data.content;
        this.postThumbnailPreviewSrc = data.thumbnailImage;
      } catch (error) {
        console.error("Error fetching post data:", error);
      }
    },
    getImage() {
      this.postThumbnail = document.getElementById("imageInput").files[0];
      this.postThumbnailPreviewSrc = URL.createObjectURL(this.postThumbnail);
      this.postThumbnailKey = this.postThumbnail.name;
      this.postThumbnailAlt = this.inputValueTitle;
    },
    // async publishThumbnail() {
    //   if (document.getElementById("createPostForm").checkValidity()) {
    //     const formData = new FormData();

    //     formData.append("title", this.inputValueTitle);
    //     formData.append("content", this.inputValueContent);
    //     formData.append("thumbnailImage", this.postThumbnail);
    //     formData.append("thumbnailImageKey", this.postThumbnailKey);
    //     formData.append("url", this.formattedUrl);

    //     await fetch(`${process.env.VUE_APP_URL}/api/media/upload`, {
    //       method: "POST",
    //       body: formData,
    //     })
    //       .then((response) => {
    //         if (!response.ok) {
    //           throw new Error("Failed to upload post thumbnail");
    //         }
    //         return response.json();
    //       })
    //       .then((data) => {
    //         this.postThumbnailSrc = data.url;
    //       })
    //       .catch((error) => {
    //         console.error("Error uploading post data:", error);
    //       });
    //   }
    // },
    async publishThumbnail() {
      if (document.getElementById("createPostForm").checkValidity()) {
        const formData = new FormData();

        formData.append("title", this.inputValueTitle);
        formData.append("content", this.inputValueContent);
        formData.append("thumbnailImage", this.postThumbnail);
        formData.append("thumbnailImageKey", this.postThumbnailKey);
        formData.append("url", this.formattedUrl);

        try {
          const response = await axiosInstance.post(
            "/api/media/upload",
            formData
          );

          if (response.status !== 200) {
            throw new Error("Failed to upload post thumbnail");
          }

          this.postThumbnailSrc = response.data.url;
        } catch (error) {
          console.error("Error uploading post data:", error);
        }
      }
    },
    // eslint-disable-next-line
    // async publishPost() { // TODO: Check for duplicated titles
    //   if (this.existentPostId) {
    //     const updatePost = {
    //       title: this.inputValueTitle,
    //       content: this.inputValueContent,
    //       categoryTags: ["one", "two"],
    //       thumbnailImage: this.postThumbnailSrc,
    //       url: this.formattedUrl,
    //       featured: true,
    //       status: "published",
    //     };

    //     fetch(
    //       `${process.env.VUE_APP_URL}/api/posts/updatePostById/${this.existentPostId}`,
    //       {
    //         method: "POST",
    //         headers: {
    //           "Content-Type": "application/json",
    //         },
    //         body: JSON.stringify(updatePost),
    //       }
    //     )
    //       .then((response) => {
    //         if (!response.ok) {
    //           throw new Error("Failed to update post");
    //         } else {
    //           this.$router.push("/blog");
    //         }
    //       })
    //       .catch((error) => {
    //         console.error(error);
    //       });
    //   } else {
    //     await this.publishThumbnail();

    //     const newPost = {
    //       title: this.inputValueTitle,
    //       author: this.userData._id,
    //       content: this.inputValueContent,
    //       categoryTags: ["one", "two"],
    //       thumbnailImage: this.postThumbnailSrc,
    //       url: this.formattedUrl,
    //       viewsReadCount: 12,
    //       likesReactions: 5,
    //       comments: ["Hello guys", "Looks great!"],
    //       featured: true,
    //       status: "published",
    //     };

    //     await fetch(`${process.env.VUE_APP_URL}/api/posts/createPost`, {
    //       method: "POST",
    //       headers: {
    //         "Content-Type": "application/json",
    //       },
    //       body: JSON.stringify(newPost),
    //     })
    //       .then((response) => {
    //         if (!response.ok) {
    //           throw new Error("Failed to create post");
    //         } else {
    //           this.$router.push("/blog");
    //         }
    //       })
    //       .catch((error) => {
    //         console.error(error);
    //       });
    //   }
    // },
    async publishPost() {
      // Check if the form is valid before proceeding
      if (document.getElementById("createPostForm").checkValidity()) {
        if (this.existentPostId) {
          const updatePost = {
            title: this.inputValueTitle,
            content: this.inputValueContent,
            categoryTags: ["one", "two"],
            thumbnailImage: this.postThumbnailSrc,
            url: this.formattedUrl,
            featured: true,
            status: "published",
          };

          try {
            const response = await axiosInstance.post(
              `/api/posts/updatePostById/${this.existentPostId}`,
              updatePost
            );

            if (response.status !== 200) {
              throw new Error("Failed to update post");
            } else {
              this.$router.push("/blog");
            }
          } catch (error) {
            console.error("Error updating post:", error);
          }
        } else {
          await this.publishThumbnail();

          const newPost = {
            title: this.inputValueTitle,
            author: this.userData._id,
            content: this.inputValueContent,
            categoryTags: ["one", "two"],
            thumbnailImage: this.postThumbnailSrc,
            url: this.formattedUrl,
            viewsReadCount: 12,
            likesReactions: 5,
            comments: ["Hello guys", "Looks great!"],
            featured: true,
            status: "published",
          };

          try {
            const response = await axiosInstance.post(
              "/api/posts/createPost",
              newPost
            );

            if (response.status !== 200) {
              throw new Error("Failed to create post");
            } else {
              this.$router.push("/blog");
            }
          } catch (error) {
            console.error("Error creating post:", error);
          }
        }
      }
    },
    draftPost() {
      console.log("Guardar");
    },
  },
};
</script>

<style>
.post-url {
  background-color: var(--foreground-color);
  color: var(--white);
  font-size: calc(var(--font-size) * 0.8);
  width: fit-content;
  padding: 2px 8px;
  margin: 1rem 0;
  border-radius: var(--border-radius-md);
}

.form-actions {
  display: flex;
  gap: 1rem;
  margin: 2rem 0;
}

.publish-button {
  color: var(--white);
}
</style>
