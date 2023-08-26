import { createApp } from "vue";
import App from "./App.vue";
import VueLazyload from "vue-lazyload";
import { createRouter, createWebHistory } from "vue-router";

const routes = [
  {
    path: "/contacto",
    name: "ContactPage",
    component: () => import("@/views/ContactPage.vue"),
  },
  {
    path: "/blog",
    name: "BlogPage",
    component: () => import("@/views/BlogPage.vue"),
  },
  {
    path: "/",
    name: "HomePage",
    component: () => import("@/views/HomePage.vue"),
  },
  {
    path: "/:catchAll(.*)", // Matches any route that hasn't been matched by other routes
    name: "NotFoundPage",
    component: () => import("@/views/NotFoundPage.vue"),
  },
];

const routers = createRouter({
  history: createWebHistory(),
  routes,
});

const app = createApp(App);

app.use(routers);
app.use(VueLazyload);

app.mount("#app");
