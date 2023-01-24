<template>
  <NavBar/>
  <div class="app">
    <router-view></router-view>
  </div>

</template>

<script>
  import axios from "axios";
  import NavBar from "@/components/NavBar.vue";

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
  }
</script>

<style lang="scss">
*{
  padding: 0;
  margin: 0;
  box-sizing: border-box;
}
</style>
