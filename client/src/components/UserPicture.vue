<template>
  <img
    v-if="profilePicSrc !== ''"
    v-lazy="profilePicSrc"
    :alt="userDisplayName"
    class="user-profile-pic"
  />
  <div v-else class="user-profile-pic">
    {{ userDisplayName.charAt(0).toUpperCase() }}
  </div>
</template>

<script>
export default {
  name: "UserPicture",
  props: {
    profilePicSrc: {
      type: String,
      default: "",
    },
    userDisplayName: {
      type: String,
      default: "",
    },
  },
};
</script>

<style>
.user-profile-pic {
  display: grid;
  place-items: center;
  height: 50px;
  width: 50px;
  border: 2px solid var(--primary-color);
  border-radius: 100%;
  background-color: var(--primary-color);
  color: var(--white);
}
</style>
