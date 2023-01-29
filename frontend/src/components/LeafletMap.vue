<template>
  <div>
    <div id="map"></div>
  </div>
</template>

<script>
import login from "@/views/Login.vue";
import logo from '../assets/logo.png'
export default {
  name: "LeafletMap",
  props:{
    zoom: {
      type: Number,
      default: 10,
    },
    center:{
      type: Array,
      default: [51.505, -0.09]
    },
    markers:{
      type: Array,
      default: [],
    },

  },
  setup() {
    let map
    return {
      map,
      initMap() {
        map = L.map('map').setView([51.505, -0.09], 13)
        L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
          attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
        }).addTo(map)

        const icon = L.icon({
          iconUrl: logo,
          iconSize: [38, 95], // size of the icon
          iconAnchor: [22, 94], // point of the icon which will correspond to marker's location
          popupAnchor: [-3, -76] // point from which the popup should open relative to the iconAnchor
        })

        map.on('click', (e) => {
          let marker = L.marker(e.latlng, {icon: icon}).addTo(map)
        })

        // marker1 = L.marker([51.5, -0.09])
        // marker1.bindPopup("<b>Hello world!</b><br>I am a new popup.").openPopup();
        // marker1.setIcon(icon)
        //
        // marker2 = L.marker([51.51, -0.09])
        // marker2.bindPopup("<b>Hello world!</b><br>I am a popup.").openPopup();
        // this.markers.push(marker1)
        // this.markers.push(marker2)


        for (const index in this.markers){
          this.markers[index].addTo(map)
        }

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