

import Home from "@/views/Home.vue";
import About from "@/views/About.vue";
import Todos from "@/views/Todos.vue";
import App_v1 from "@/views/App_v1.vue";
import App_v2 from "@/views/App_v2.vue";
import SettingsView from "@/views/SettingsView.vue";

import { createRouter, createWebHistory } from "vue-router";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    { path: "/", component: Home },
    { path: "/about", component: About },
    { path: "/todos", component: Todos },
    { path: "/v1", component: App_v1 },
    { path: "/v2", component: App_v2 },
    { path: "/settings", component: SettingsView },
  ],
});

export default router;
