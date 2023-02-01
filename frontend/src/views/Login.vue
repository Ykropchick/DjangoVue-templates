<template>
  <div class="form">
    <form @submit.prevent="submitForm">
      <input class="form__input" type="text" placeholder="phone" v-model="phone">
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
      phone: '',
      password: '',
    }
  },
  methods: {
    async submitForm(){
      const data = {
        phone: this.phone,
        password: this.password,
      }

    axios.defaults.headers.common['Authorization'] = ''
    localStorage.removeItem('token')
    localStorage.removeItem('phone')
    await axios
        .post('/api/v1/token/login/', data)
        .then(response => {
            const token = response.data.auth_token
            this.$store.commit('setToken', token)
            axios.defaults.headers.common['Authorization'] = 'Token ' + token
            localStorage.setItem('token', token)
            localStorage.setItem('phone', this.phone)
        })
        .catch(error => {
            console.log(error)
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