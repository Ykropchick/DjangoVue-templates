<template>
  <router-view/>
</template>

<script>
  import axios from "axios";

  export default {
    name: 'App',
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
</style>
