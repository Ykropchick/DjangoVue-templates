<template>
  <div>
    <div id="map"></div>
  </div>
</template>

<script>
export default {
  name: "LeafletMap",
  setup() {
    let map
    let marker
    let marker2
    return {
      map,
      marker,
      marker2,
      initMap() {
        map = L.map('map').setView([51.505, -0.09], 13)
        L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
          attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
        }).addTo(map)
        marker = L.marker([51.5, -0.09]).addTo(map)
        marker2 = L.marker([51.51, -0.09]).addTo(map)
        marker.bindPopup("<b>Hello world!</b><br>I am a popup.").openPopup();
        marker2.bindPopup("<b>Hello world!</b><br>I am a popup.").openPopup();
      }
    }
  },
  mounted() {
    this.initMap()
  }
}
</script>

<style scoped>
#map{
  height: 960px;
  width: 960px;
}
</style>