import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
// main.js
import axios from "axios";

axios.defaults.baseURL = "http://127.0.0.1:5000"; // Replace with your server's URL
Vue.prototype.$http = axios;

import "bootstrap/dist/css/bootstrap.min.css";

import { initWorker } from "./Worker";

initWorker().then(_ => {

  Vue.config.productionTip = false;

  new Vue({
    router,
    store,
    render: (h) => h(App),
  }).$mount("#app");
});
