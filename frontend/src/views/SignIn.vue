<template>
  <form >
    <input class="form__input" type="text" placeholder="phone" v-model="phone">
    <input class="form__input" type="text" placeholder="username" v-model="username">
    <input class="form__input" type="text" placeholder="password" v-model="password">
    <VueRecaptcha
      :sitekey="sitekey"
      :load-recaptcha-script="true"
      @verify="handleSuccess"
      @error="handleError"
    ></VueRecaptcha>
    <button class="form__btn" @click.prevent="checkButton">SignIn</button>
  </form>

</template>

<script>
import axios from "axios";
import {VueRecaptcha} from "vue-recaptcha";

export default {
  name: "SignIn",
  components: {
    VueRecaptcha
  },
  data(){
    return {
      username: '',
      password: '',
      phone: '',
      captcha: null,
      sitekey: '6LfT_jskAAAAANglfKqAVEHFR9w5DGcu7qz3ZxXc'
    }
  },
  methods:{
    handleSuccess(response){
      console.log(response)
      this.captcha = true
    },
    handleError(){
      console.log()
    },

    async checkButton(){
      console.log(this.captcha)
      // if (this.captcha){
      //   const data = {
      //   username: this.username,
      //   password: this.password,
      //   phone: this.phone,
      // }
      // await axios
      //     .post('/api/v1/users/', data)
      //     .then(response => {
      //       console.log(response.data)
      //     })
      //     .catch( error =>{
      //       console.log(error)
      //     })
      // }
    }
  }
}
</script>

<style scoped>
  .form{
    display: inline-block;
  }
  .form__input, .form__btn{
    display: inline-block;
  }
</style>