<template>

</template>

<script>
import axios from "axios";
import {useLink} from "vue-router";

export default {
  name: "UserList",
  data(){
    return{
      users: [],
    }
  },
  created(){
    axios
        .get('/api/v1/users/')
        .then(response =>{
          this.users.push(response.data)
        })
    console.log(this.users)
  }
}
</script>

<style scoped>

</style>