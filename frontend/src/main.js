import { createApp } from 'vue'
import App from './App.vue'
import axios from "axios";

// import router from './router'
// import store from './store'


const app = createApp(App);
// app.use(store)
// app.use(router)

axios.defaults.xsrfCookieName = 'csrftoken';
axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
app.mount('#app')
