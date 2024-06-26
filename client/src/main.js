import { createApp } from "vue";
import App from "./App.vue";
import { createRouter, createWebHistory } from "vue-router";
import HomePage from "@/views/HomePage.vue";
import CreateOrEditPost from "@/views/CreateOrEditPost.vue";
import ContactPage from "@/views/ContactPage.vue";
import BlogPage from "@/views/BlogPage.vue";
import BlogPost from "./views/BlogPost.vue";
import NotFoundPage from "@/views/NotFoundPage.vue";
import store from "./store";
import vue3GoogleLogin from "vue3-google-login";
import VueLazyload from "vue-lazyload";

// icons set up
import { FontAwesomeIcon } from "@fortawesome/vue-fontawesome";
import { library } from "@fortawesome/fontawesome-svg-core";
import {
  faInstagram,
  faFacebookF,
  faXTwitter,
  faYoutube,
} from "@fortawesome/free-brands-svg-icons";
import {
  faSun,
  faMoon,
  faChevronDown,
  faSignOut,
  faPenToSquare,
  faCheck,
  faTrashCan,
  faBoxArchive,
  faArrowUpRightFromSquare,
  faExclamation,
  faXmark,
} from "@fortawesome/free-solid-svg-icons";

library.add(
  faInstagram,
  faFacebookF,
  faXTwitter,
  faYoutube,
  faSun,
  faMoon,
  faChevronDown,
  faSignOut,
  faPenToSquare,
  faCheck,
  faTrashCan,
  faBoxArchive,
  faArrowUpRightFromSquare,
  faExclamation,
  faXmark
);

const routes = [
  {
    path: "/publicar",
    name: "CreateOrEditPost",
    component: CreateOrEditPost,
    meta: { requiresAdmin: true },
  },
  {
    path: "/contacto",
    name: "ContactPage",
    component: ContactPage,
  },
  {
    path: "/blog",
    children: [
      {
        path: "",
        name: "BlogPage",
        component: BlogPage,
      },
      {
        path: "post/:postURL",
        component: BlogPost,
      },
    ],
  },
  {
    path: "/",
    name: "HomePage",
    component: HomePage,
  },
  {
    path: "/404",
    name: "NotFoundPage",
    component: NotFoundPage,
  },
  {
    path: "/:catchAll(.*)",
    redirect: { name: "NotFoundPage" },
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

router.beforeEach(async (to, from, next) => {
  console.log(process.env.SERVER_API_KEY);

  // fetches user data, if any
  await store.dispatch("fetchUserData");

  let isAdmin = false;

  // check if userData is available before asking for values
  if (store.state.userData) {
    // handle admin role permissions
    isAdmin = store.state.userData.role === "admin";
  }

  const requiresAdmin = to.matched.some((record) => record.meta.requiresAdmin);

  // redirects to 404 if not admin user tries to access restricted page
  if (requiresAdmin && !isAdmin) {
    next({ name: "NotFoundPage" });
  } else {
    next();
  }
});

const app = createApp(App);

// Font Awesome component set up
app.component("font-awesome-icon", FontAwesomeIcon);

app.use(router);
app.use(store);
app.use(VueLazyload);
app.use(vue3GoogleLogin, {
  clientId: process.env.VUE_APP_GOOGLE_CLIENT,
});

app.mount("#app");
