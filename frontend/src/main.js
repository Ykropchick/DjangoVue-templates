import { createApp, provide, h } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import axios from 'axios'

import { DefaultApolloClient } from '@vue/apollo-composable'
import {ApolloClient, createHttpLink, from, InMemoryCache} from '@apollo/client/core'

import 'leaflet/dist/leaflet.css'
import L from 'leaflet'

import "bootstrap/dist/css/bootstrap.min.css"
import "bootstrap"




// GraphQL
const cache = new InMemoryCache()
const httpLink = createHttpLink({
    uri: 'https://backend-ykropchick.vercel.app/graphql/'
    }
)

const apolloClient = new ApolloClient({
    link: httpLink,
    cache
})

const app = createApp({
    setup(){
        provide(DefaultApolloClient, apolloClient)
    },
    render: () => h(App)
})


// Auth
axios.defaults.baseURL = 'https://backend-ykropchick.vercel.app'


app.use(store).use(router).mount('#app')
