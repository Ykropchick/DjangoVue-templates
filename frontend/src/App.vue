<template>
  <NavBar/>
  <div class="app">
    <router-view></router-view>
  </div>

</template>

<script>
  import axios from "axios";
  import NavBar from "@/components/NavBar.vue";
  import gql from 'graphql-tag'
  import {useQuery, useResult} from "@vue/apollo-composable";
  import {computed, watchEffect} from "vue";

  export default {
    name: 'App',
    components: {NavBar},
    beforeCreate() {
      this.$store.commit('initializeStore')
      if (this.$store.state.token) {
        axios.defaults.headers.common['Authorization'] = "Token " + this.$store.state.token
      } else {
        axios.defaults.headers.common['Authorization'] = ""
      }
    },
    async created(){
      const ALL_USERS_QUERY = gql`
        query {
          users{
            id
            admin
           }
        }
      `
      const { result } = useQuery(ALL_USERS_QUERY)
      const users = computed( () => result.value?.users ?? [] )
      watchEffect(() => {
        console.log(users.value)
      })
    },

  }
</script>

<style lang="scss">
*{
  padding: 0;
  margin: 0;
  box-sizing: border-box;
}
</style>
