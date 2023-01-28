<template>
  <div class="map">
    <LeafletMap>

    </LeafletMap>
  </div>

</template>

<script>
import "leaflet/dist/leaflet.css";
import LeafletMap from "@/components/LeafletMap.vue";
export default {
  name: "Map",
  components: {
    LeafletMap,
  },
  data(){
    return {
      zoom: 2,
    }
  },
}
</script>

<style scoped>
.map{
  height: 600px;
  width: 800px;
}
</style>