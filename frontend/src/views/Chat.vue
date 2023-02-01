<template>
  <div class="container">
    <div class="message_area align-self-center overflow-scroll">
      <div v-for="({message, user}) in this.messages">
        <div v-if="user === this.$store.state.phone" class="my_message text-end">
          {{ message }}
        </div>
        <div v-else class="other_message text-start">
          {{ message }}
        </div>
      </div>

    </div>
    <form>
      <div class="row">
        <div class="input-group mb-3">
          <input type="text" v-model="my_message" class="form-control">
          <button @click.prevent="sendMessage" class="btn btn-outline-secondary">Send</button>
        </div>
      </div>
    </form>
  </div>



</template>

<script>
export default {
  name: "Chat",
  data(){
    return{
      connection: '',
      my_message: '',
      messages: [],
    }
  },
  mounted() {
    this.connection = new WebSocket(`ws://127.0.0.1:8001/ws/chat/${this.room_name}/`)
    this.connection.onopen = (event) =>{
      console.log("connected")
    }
    this.connection.onmessage = (event) => {
      const message = JSON.parse(event.data)
      this.messages.push(message)
    }
  },
  methods:{
    sendMessage(){
      this.connection.send(JSON.stringify({
        "user": this.$store.state.phone,
        "message": this.my_message,
      }))
      this.my_message = ''
    }
  },
  computed: {
    room_name(){
      return this.$route.params.name
    }
  }
}
</script>

<style scoped lang="scss">
.message_area{
  border: 2px solid black;
  height: 75vh;
}

</style>