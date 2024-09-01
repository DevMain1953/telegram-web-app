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
    path: "/",
    redirect: "/selecting-birth-date",
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

router.beforeEach((to, from, next) => {
  if (to.path === "/selecting-birth-date" && to.query.tgWebAppStartParam) {
    next({
      name: "ClientInfo",
      params: { username: to.query.tgWebAppStartParam },
    });
  } else {
    next();
  }
});

export default router;
