<template>
  <VueRecaptcha
    :sitekey="sitekey"
    :load-recaptcha-script="true"
    @verify="handleSuccess"
    @error="handleError"
  ></VueRecaptcha>
</template>

<script>
import {VueRecaptcha} from "vue-recaptcha";

export default {
  name: "Captcha",
  components: {
    VueRecaptcha
  },
  data(){
    return {
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
  }
}
</script>

<style scoped>
</style>