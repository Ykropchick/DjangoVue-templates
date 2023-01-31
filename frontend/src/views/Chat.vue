<template>

  <form>
    <textarea cols="30" rows="10" v-model="message"/>
    <button @click.prevent="sendMessage">Send</button>
  </form>


</template>

<script>
export default {
  name: "Chat",
  data(){
    return{
      connection: '',
      message: '',
    }
  },
  mounted() {
    this.connection = new WebSocket('ws://127.0.0.1:8001/ws/chat/12/')
    this.connection.onmessage = (message) =>{
      console.log(message.data)
    }
  },
  methods:{
    sendMessage(){
      this.connection.send(JSON.stringify({"message": this.message}))
      this.message = ''
    }
  }
}
</script>

<style scoped lang="scss">

</style>