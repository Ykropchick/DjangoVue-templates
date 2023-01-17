<template>
  <form @submit.prevent="submitForm">
    <input type="text" placeholder="username" v-model="username">
    <input type="text" placeholder="password" v-model="password">
    <button type="submit">LogIn</button>
  </form>
</template>

<script>
import axios from 'axios'
export default {
  name: "Login",
  data(){
    return{
      username: '',
      password: '',
    }
  },
  methods: {
    async submitForm(){
      const data = {
        username: this.username,
        password: this.password
      }

  axios.defaults.headers.common['Authorization'] = ''
  localStorage.removeItem('token')
  await axios
      .post('/api/v1/token/login/', data)
      .then(response => {
          const token = response.data.auth_token
          this.$store.commit('setToken', token)
          axios.defaults.headers.common['Authorization'] = 'Token ' + token
          localStorage.setItem('token', token)
          console.log(token)
      })
    },
  },
}
</script>

<style scoped>

</style>