<template>
  <button @click="logout"> Logout </button>
</template>

<script>
export default {
  name: "Logout",
  methods: {
    logout(){
      localStorage.removeItem('token')
      this.$store.state.token = ''
      this.$store.state.isAuthenticated = false
    }
  }
}
</script>

<style scoped>

</style>