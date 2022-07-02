import Vue from "vue";
import VueRouter from "vue-router";
import HomeView from "@/views/HomeView.vue";
import authService from "@/api/auth";
import storageService from "@/helpers/storage";
const callback = () => import("@/views/CallbackView.vue");
const login = () => import("@/views/LoginView.vue");

Vue.use(VueRouter);

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes: [
    {
      path: "/",
      name: "home",
      component: HomeView,
      meta: {
        requireAuth: true,
      },
    },
    {
      path: "/login",
      name: "login",
      component: login,
    },
    {
      path: "/callback",
      name: "callback",
      component: callback,
    },
  ],
});

router.beforeEach((to, from, next) => {
  console.log(
    "Router:",
    to.name,
    authService.isAuthenticated(),
    storageService.getValue("token")
  );
  if (to.meta.requireAuth && !authService.isAuthenticated()) {
    return next({ name: "login" });
  }
  if (to.name === "login" && authService.isAuthenticated()) {
    return next({ name: "home" });
  }
  return next();
});

export default router;
