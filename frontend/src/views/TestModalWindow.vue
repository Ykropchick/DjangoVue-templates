<template>
  <ModalWindow v-model:show="show">
    <p>
      Lorem ipsum dolor sit amet, consectetur adipisicing elit. Alias doloremque eos facere hic itaque, molestiae officia omnis pariatur perferendis placeat possimus quaerat, quis reiciendis rem repellat, saepe sapiente sequi vel!
      <span>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Eius fuga hic id quo reprehenderit. Blanditiis dolore dolorem impedit iste, laboriosam molestiae molestias mollitia nisi nobis quas quisquam rerum sed vel!</span><span>Aperiam assumenda cupiditate, eius maxime mollitia odit sequi totam. Aliquid animi, architecto aut consequuntur dolorem, eligendi esse excepturi laudantium magni nostrum possimus quaerat quibusdam quidem quisquam, quos ratione ut voluptas?</span><span>Ab aperiam cupiditate delectus deleniti dicta facilis illum in, iste laudantium saepe sit tenetur unde voluptatum! Dignissimos eaque facilis illum ipsa provident saepe ut. Atque exercitationem illo labore quia quis.</span><span>Aperiam doloribus fuga, minus necessitatibus neque quae quidem recusandae repellendus repudiandae. Commodi dicta dignissimos doloremque excepturi, incidunt ipsa, magnam molestias, obcaecati porro quaerat qui sed sit totam ullam velit veritatis.</span>
    </p>
  </ModalWindow>
</template>

<script>
import ModalWindow from "@/components/ModalWindow.vue";
import axios from "axios";

export default {
  name: "TestModalWindow",
  components: {ModalWindow},
  data(){
    return{
      show: false,
    }
  },
  async mounted() {
    const data = {
      'room_name': 12,
    }
    console.log()
    await axios
        .get("/api/v1/chat/messages/12/")
        .then(response => {
          console.log(response.data)
        })
  }
}
</script>

<style scoped>

</style>