<template>
  <form @click.prevent="checkButton">
    <input class="form__input" type="email" placeholder="email" v-model="email">
    <input class="form__input" type="text" placeholder="username" v-model="username">
    <input class="form__input" type="text" placeholder="password" v-model="password">
    <button class="form__btn" type="submit">LogIn</button>
  </form>

</template>

<script>
import axios from "axios";

export default {
  name: "SignIn",
  data(){
    return {
      username: '',
      password: '',
      email: '',
    }
  },
  methods:{
    async checkButton(){
      const data = {
        username: this.username,
        password: this.password,
        email: this.email,
      }
      await axios
          .post('/api/v1/users/', data)
          .then(response => {
            console.log(response.data)
          })


    }
  }
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