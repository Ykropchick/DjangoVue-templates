import { createRouter, createWebHashHistory } from 'vue-router'
import Login from "@/views/Login.vue";


const routes = [
  {
    path: '/log-in',
    name: 'login',
    component: Login
  },
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router
