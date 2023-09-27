

import Home from "@/views/Home.vue";
import About from "@/views/About.vue";
import Todos from "@/views/Todos.vue";
import ThreePanelContainer from "@/views/3PanelContainer.vue";
import SettingsView from "@/views/SettingsView.vue";

import { createRouter, createWebHistory } from "vue-router";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    { path: "/", component: Home },
    { path: "/about", component: About },
    { path: "/todos", component: Todos },
    { path: "/zasshi", component: ThreePanelContainer },
    { path: "/settings", component: SettingsView },
  ],
});

export default router;
