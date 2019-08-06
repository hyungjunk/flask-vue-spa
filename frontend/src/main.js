import Vue from 'vue'
import App from './App'
import router from './router'
import BootstrapVue from 'bootstrap-vue'
import VueProgress from 'vue-progress'

Vue.use(BootstrapVue);
Vue.use(VueProgress);
Vue.config.productionTip = false;

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  render: h => h(App),
  data: {
    show: true
  }
});
