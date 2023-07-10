import { createApp } from "vue";
import { createRouter, createWebHistory } from "vue-router";
import App from "./App.vue";
import VueLazyload from "vue-lazyload";
import NotFoundPage from "@/views/NotFoundPage.vue";
import HomePage from "@/views/HomePage.vue";
import ContactPage from "@/views/ContactPage.vue";

const NotFound = { template: NotFoundPage };
const Home = { template: HomePage };
const Contact = { template: ContactPage };

const routes = [
  { path: "/", name: "Home", component: Home },
  { path: "/contact", name: "Contact", component: Contact },
  { path: "/:pathMatch(.*)*", name: "NotFound", component: NotFound },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

const app = createApp(App);

app.use(router);
app.use(VueLazyload);

app.mount("#app");
