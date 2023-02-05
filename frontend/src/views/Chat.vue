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
          <input type="text" maxlength="500" v-model="my_message" class="form-control">
          <button @click.prevent="sendMessage" class="btn btn-outline-secondary">Send</button>
        </div>
      </div>
    </form>
  </div>



</template>

<script>
import axios from "axios";

export default {
  name: "Chat",
  data(){
    return{
      connection: '',
      my_message: '',
      messages: [],
    }
  },
  async mounted() {
    await this.takeMessageHistory()
    this.connectWebSocket(`ws://backend-beta-ruddy.vercel.app/ws/chat/${this.room_name}/`)
  },
  methods:{
    sendMessage(){
      this.connection.send(JSON.stringify({
        "user": this.$store.state.phone,
        "message": this.my_message,
      }))
      this.my_message = ''
    },
    async takeMessageHistory(){
      await axios
          .get(`/api/v1/chat/messages/${this.room_name}/`)
          .then(response => {
            response.data.forEach(({user, text}) => {
              this.messages.push({
                    "user" : user.phone,
                    "message": text,
                  }
              )
            })
          })

    },
    connectWebSocket(url){
      this.connection = new WebSocket(url)
      this.connection.onopen = (event) =>{
        console.log("connected")
        this.connection.send(JSON.stringify({
          type: "Init",
          username: this.$store.state.phone
        }))
      }
      this.connection.onmessage = (event) => {
        const message = JSON.parse(event.data)
        this.messages.push(message)
      }
    },

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