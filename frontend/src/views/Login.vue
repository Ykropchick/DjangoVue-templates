<template>
  <div class="form">
    <form @submit.prevent="submitForm">
      <input class="form__input" type="text" placeholder="username" v-model="username">
      <input class="form__input" type="text" placeholder="password" v-model="password">
      <button class="form__btn" type="submit">LogIn</button>
    </form>
  </div>

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
      })
    },
  },
}
</script>

<style scoped lang="scss">
  .form{
    display: inline-block;
  }
  .form__input, .form__btn{
    display: inline-block;
  }
</style>