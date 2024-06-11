<template>
  <div class="profile-wrapper">
    <div
      class="profile"
      :class="{ collapsed: isDropdownCollapsed }"
      v-if="isLoggedIn && userData"
      @click="collapseDropdown"
    >
      <UserPicture
        :profilePicSrc="userData.profilePicture"
        :userDisplayName="userData.displayName"
      />
      <div class="profile__info">
        <p class="profile__name">
          {{ userData.displayName }}
        </p>
        <font-awesome-icon
          icon="fas fa-chevron-down"
          class="profile__dropdown-button"
        />
      </div>
    </div>
    <GoogleLogin v-else :callback="callback" />
    <div
      v-show="isDropdownCollapsed"
      class="profile-dropdown"
      @click="collapseDropdown"
    >
      <router-link
        v-show="userData && userData.role === 'admin'"
        class="profile-dropdown__item"
        to="/publicar"
      >
        Publicar
        <font-awesome-icon
          icon="fas fa-pen-to-square"
          class="profile-dropdown__icon"
        />
      </router-link>
      <p class="profile-dropdown__item" @click="logout">
        Cerrar sesión
        <font-awesome-icon
          icon="fas fa-sign-out"
          class="profile-dropdown__icon"
        />
      </p>
    </div>
  </div>
</template>

<script>
import UserPicture from "./UserPicture.vue";
import { mapState } from "vuex";
import { GoogleLogin, decodeCredential, googleLogout } from "vue3-google-login";
import Cookies from "js-cookie";
import store from "@/store";

export default {
  name: "LoginComponent",
  components: {
    UserPicture,
    GoogleLogin,
  },
  data() {
    return {
      isDropdownCollapsed: false,
      isLoggedIn: false,
    };
  },
  methods: {
    collapseDropdown() {
      this.isDropdownCollapsed = !this.isDropdownCollapsed;
    },
    checkLoggedIn() {
      const userId = Cookies.get("user_id");
      if (userId) {
        this.isLoggedIn = true;
      } else {
        this.isLoggedIn = false;
      }
    },
    async logout() {
      googleLogout();
      Cookies.remove("user_id");

      await store.dispatch("logoutUser");

      this.isLoggedIn = false;
    },
    async callback(response) {
      if (response.credential) {
        // gets google credential to access Google data
        const decoded = decodeCredential(response.credential);

        // sets cookie to recognize user for next 7 days
        Cookies.set("user_id", decoded.sub, { expires: 7 });

        // creates or updates a new user
        await store.dispatch("createAndLoginUser", {
          userId: Cookies.get("user_id"),
          googleData: decoded,
        });

        this.isLoggedIn = true;
      } else {
        console.log("Couldn't access callback credential");
      }
    },
  },
  computed: {
    ...mapState({
      userData: (state) => state.userData,
    }),
  },
  mounted() {
    this.checkLoggedIn();
  },
};
</script>

<style>
.profile-wrapper {
  position: relative;
}

.profile {
  display: flex;
  align-items: center;
  gap: 10px;
}

.profile__info {
  display: flex;
  align-items: center;
  gap: 10px;
}

.profile__name {
  font-weight: var(--font-bold);
  border-bottom: 2px solid var(--primary-color);
}

.profile__dropdown-button {
  width: 20px;
  transition: all 0.1s ease-out;
}

.profile.collapsed > .profile__info > .profile__dropdown-button {
  transform: rotate(180deg);
}

.profile-dropdown {
  position: absolute;
  top: 120%;
  right: 0;
  left: 0;
  width: 100%;
  border-radius: var(--border-radius-sm);
  background-color: var(--background-color);
  box-shadow: 1px 1px 4px 0 var(--box-shadow-color);
  padding: 0.5rem 1rem;
  z-index: 500;
  user-select: none;
}

.profile-dropdown__item {
  display: flex;
  align-items: center;
  gap: 5px;
  font-size: calc(var(--font-size) * 0.8);
  font-weight: var(--font-bold);
  text-decoration: none;
  color: var(--primary-text-color);
  padding: 0.5rem;
  cursor: default;
}

.profile-dropdown__item:hover {
  opacity: 0.8;
  border-radius: var(--border-radius-sm);
}

.profile-dropdown__item:not(:last-child) {
  border-bottom: 1px solid var(--foreground-color);
}

.profile-dropdown__icon {
  width: 15px;
}
</style>
