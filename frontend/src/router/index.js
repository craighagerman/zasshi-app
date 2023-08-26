// import App from "./App";

import Home from "@/views/Home.vue";

import About from "@/views/About.vue";
import Todos from "@/views/Todos.vue";
import App_v1 from "@/views/App_v1.vue";
import App_v2 from "@/views/App_v2.vue";

import { createRouter, createWebHistory } from "vue-router";

// import HomeView from "../views/HomeView.vue";

// const router = createRouter({
//   history: createWebHistory(import.meta.env.BASE_URL),
//   routes: [
//     {
//       path: "/",
//       name: "home",
//       component: HomeView,
//     },
//     {
//       path: "/about",
//       name: "about",
//       // route level code-splitting
//       // this generates a separate chunk (About.[hash].js) for this route
//       // which is lazy-loaded when the route is visited.
//       component: () => import("../views/AboutView.vue"),
//     },
//   ],
// });

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    { path: "/", component: Home },
    { path: "/about", component: About },
    { path: "/todos", component: Todos },
    { path: "/v1", component: App_v1 },
    { path: "/v2", component: App_v2 },
  ],
});

export default router;
