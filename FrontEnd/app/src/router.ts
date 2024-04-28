import Vue from "vue";
import Router from "vue-router";
import Viewer from "./views/Viewer.vue";
import Login from "./data/Login.vue";
import "axios";
import pWelcome from "./data_P/pWelcome.vue";
import pAbout from "./data_P/pAbout.vue";
import pContact from "./data_P/pContact.vue";
import Welcome from "./data/Welcome.vue";
import Predict from "./data/Predict.vue";
import View from "./data/EDFList.vue";
import Contact from "./data/Contact.vue";
import SampleReport from "./data/SampleReport.vue";
import About from "./data/About.vue";
import { component } from "vue/types/umd";
Vue.use(Router);
export default new Router({
  mode: "history",
  base: process.env.BASE_URL,
  routes: [
    {
      path: "/about",
      component: About
    },
    {
      path: "/view",
      component: View
    },
    {
      path : "/contact",
      component : Contact
    },
    {
      path : "/predict",
      component: Predict
    },
    {
      path: "/welcome",
      component: Welcome
    },
    {
      path: "/pcontact",
      component: pContact
    },
    {
      path: "/report",
      component: SampleReport
    },
    {
      path: "/pabout",
      component: pAbout
    },
    {
      path : "/pwelcome",
      component : pWelcome
    },
    {
      path: "/",
      component: Login
    },
    {
      path: "/visualize",
      name: "viewer",
      component: Viewer,
      meta: {
        showMenubar: true, // Menubar will be shown on this route
      },
    },
    {
      path: "/",
      name: "login",
      component: Login,
      meta: {
        requiresAuth: false,
        showMenubar: false, // Menubar won't be shown on this route
      },
    },
    {
      path: "/montage",
      name: "montage",
      // route level code-splitting
      // this generates a separate chunk (about.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import(/* webpackChunkName: "montage" */ "./views/Montage.vue"),
    },
  ],
});
