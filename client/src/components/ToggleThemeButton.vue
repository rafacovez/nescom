<template>
  <div
    @click="toggleTheme"
    role="button"
    class="toggle-theme-switch"
    :class="{ dark: theme }"
  >
    <font-awesome-icon class="toggle-icon" icon="fas fa-sun" />
    <font-awesome-icon class="toggle-icon" icon="fas fa-moon" />
  </div>
</template>

<script>
export default {
  name: "ToggleThemeButton",
  data() {
    return {
      theme: localStorage.getItem("theme") || "",
    };
  },
  methods: {
    toggleTheme() {
      this.theme = this.theme === "dark" ? "" : "dark";
      document.documentElement.setAttribute("data-theme", this.theme);
      localStorage.setItem("theme", this.theme);
    },
  },
  mounted() {
    // get theme value
    let localTheme = localStorage.getItem("theme");
    document.documentElement.setAttribute("data-theme", localTheme);
  },
};
</script>

<style>
.toggle-theme-switch {
  display: none;
}

@media only screen and (min-width: 768px) {
  .toggle-theme-switch {
    position: relative;
    display: flex;
    align-items: center;
    justify-content: space-around;
    height: 20px;
    width: 40px;
    border-radius: 10px;
    background-color: var(--foreground-color);
    cursor: pointer;
  }

  .toggle-theme-switch::after {
    content: "";
    display: block;
    height: 20px;
    width: 20px;
    border-radius: 100%;
    position: absolute;
    top: 0;
    right: 0;
    bottom: 0;
    transform: scale(1.1);
    border: 1px solid var(--primary-color);
    background-color: var(--white);
  }

  .toggle-theme-switch.dark::after {
    left: 0;
  }

  .toggle-icon {
    width: 10px;
    color: var(--white);
  }
}
</style>
