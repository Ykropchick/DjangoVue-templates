<template>
  <div>
    <nav class="navbar navbar-light bg-light" >
      <div class="container-fluid">
        <a class="navbar-brand nav__element" @click="this.$router.push('/')">
          <img class="img-thumbnail logo" src="../assets/logo.png" alt="">
          The Best man
        </a>
        <div v-if="this.$store.state.isAuthenticated">
          <a class="navbar-brand nav__element" @click="this.$router.push('/UserProfile')">
            <img class="user_logo" :src="this.$store.state.serverUrl + this.ditail.avatar" alt="">
          </a>
          <a class="navbar-brand nav__element" @click="this.$router.push('/UserProfile')">{{this.ditail.username}}</a>
          <a class="navbar-brand nav__element" @click="this.$router.push('/logout')">Logout</a>
        </div>
        <div v-else>
          <a class="navbar-brand nav__element" @click="this.$router.push('/log-in')">Login</a>
          <a class="navbar-brand nav__element" @click="this.$router.push('/sign-in')">Signup</a>
        </div>

      </div>
    </nav>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "NavBar",
  data(){
    return{
      me : {},
      ditail: {},
    }

  },

  async created() {
    if(this.$store.state.isAuthenticated){
      await axios
          .get('/api/v1/users/me/')
          .then(response =>{
            this.me = response.data
          })
          .catch(error => {
            console.log(error)
          })
      await axios
          .get(`/api/v1/userditail/${this.me.id}/`)
          .then(response =>{
            this.ditail = response.data
          })
    }
  }
}
</script>

<style scoped lang="scss">
.logo{
  max-width: 80px;
  max-height: 80px;
}
.nav__element{
  cursor: pointer;
}
.user_logo{
  max-width: 80px;
  max-height: 80px;
}
</style>