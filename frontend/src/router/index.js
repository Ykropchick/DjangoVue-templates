import { createRouter, createWebHashHistory } from 'vue-router'
import Login from "@/views/Login.vue";
import SignIn from "@/views/SignIn.vue";
import Logout from "@/views/Logout.vue";


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
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router
