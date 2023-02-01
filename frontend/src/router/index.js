import { createRouter, createWebHashHistory } from 'vue-router'
import Login from "@/views/Login.vue";
import SignIn from "@/views/SignIn.vue";
import Logout from "@/views/Logout.vue";
import Map from "@/views/Map.vue";
import Chat from "@/views/Chat.vue";
import TestModalWindow from "@/views/TestModalWindow.vue";


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
  {
    path: '/chat/:name',
    name: 'chat',
    component: Chat
  },
  {
    path: '/test_modal_window',
    name: 'chat',
    component: TestModalWindow
  },
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router
