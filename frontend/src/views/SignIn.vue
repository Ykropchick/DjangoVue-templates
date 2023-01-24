<template>
  <form >
    <input class="form__input" type="text" placeholder="phone" v-model="phone">
    <input class="form__input" type="text" placeholder="username" v-model="username">
    <input class="form__input" type="text" placeholder="password" v-model="password">
    <button class="form__btn" @click.prevent="checkButton">SignIn</button>
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
      phone: '',
    }
  },
  methods:{
    async checkButton(){
      const data = {
        username: this.username,
        password: this.password,
        phone: this.phone,
      }
      await axios
          .post('/api/v1/users/', data)
          .then(response => {
            console.log(response.data)
          })
          .catch( error =>{
            console.log(error)
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