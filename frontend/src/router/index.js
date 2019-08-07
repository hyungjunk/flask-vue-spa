import Vue from 'vue'
import Router from 'vue-router'
const routerOptions = [
  { path: '/', component: 'Chat' },
  { path: '/about', component: 'About' },
  { path: '*', component: 'NotFound' },
  { path: '/help', component: 'NeedHelp' },
  { path: '/home', component: 'Home' },
];

const routes = routerOptions.map(route => {
  return {
    ...route,
    component: () => import(`@/components/${route.component}.vue`)
  }
});

Vue.use(Router);
export default new Router({
  routes,
  mode: 'history'
})
