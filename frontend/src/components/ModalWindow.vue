<template>
  <div class="dialog" v-if="show" @click="hideDialog">
    <div @click.stop class="dialog__content">
      <slot>

      </slot>

    </div>
  </div>
</template>

<script>
export default {
  name: "ModalWindow",
  props:{
    show:{
      type: Boolean,
      require: true
    }
  },
  methods: {
    hideDialog(){
      this.$emit('update:show', false)
    }
  }
}
</script>

<style scoped lang="scss">
  .dialog{
    top: 0;
    bottom: 0;
    right: 0;
    left: 0;
    background: rgba(0,0,0,0.5);
    position: fixed;
    display: flex;
  }
  .dialog__content{
      margin: auto;
      background: white;
      border-radius: 12px;
      min-height: 50px;
      min-width: 300px;
  }
</style>