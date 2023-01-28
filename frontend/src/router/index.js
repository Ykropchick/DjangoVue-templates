import { createRouter, createWebHashHistory } from 'vue-router'
import Login from "@/views/Login.vue";
import SignIn from "@/views/SignIn.vue";
import Logout from "@/views/Logout.vue";
import Map from "@/views/Map.vue";


const routes = [
  {
    path: '/log-in',
    name: 'login',
    component: Login
  },
  {
    path: '/sign-in',
    name: 'signin',
    component: SignIn
  },
  {
    path: '/logout',
    name: 'logout',
    component: Logout
  },
  {
    path: '/map',
    name: 'map',
    component: Map
  },
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router
