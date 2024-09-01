import { createRouter, createWebHistory } from "vue-router";

import ClientInfo from "../components/ClientInfo.vue";
import SelectingBirthDate from "../components/SelectingBirthDate.vue";

const routes = [
  {
    path: "/client-info/:username",
    name: "ClientInfo",
    component: ClientInfo,
    props: true,
  },
  {
    path: "/selecting-birth-date",
    name: "SelectingBirthDate",
    component: SelectingBirthDate,
  },
  {
    path: "/:username",
    redirect: "/client-info/:username",
    props: true,
  },
  {
    path: "/",
    redirect: "/selecting-birth-date",
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
