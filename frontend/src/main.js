import { createApp, provide, h } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import axios from 'axios'

import { DefaultApolloClient } from '@vue/apollo-composable'
import {ApolloClient, createHttpLink, InMemoryCache} from '@apollo/client/core'

import "bootstrap/dist/css/bootstrap.min.css"
import "bootstrap"


// GraphQL
const cache = new InMemoryCache()
const httpLink = createHttpLink({
    uri: 'http://127.0.0.1:8001/graphql/'
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
axios.defaults.baseURL = 'http://127.0.0.1:8001'

app.use(store).use(router).mount('#app')
