<template>
  <div class="grid grid-cols-6 h-full pb-10 bg-gray-100">
    <div class="col-start-2 col-span-4">
    <div class="w-full text-center p-1 text-gray-800">SWC course project</div>
    <div class="w-full text-center text-2xl p-1 text-red-900 mb-2">Amsterdam touristic sights</div>
    <div class="grid grid-cols-3 gap-3">
      <div v-for="(place, index) in places" :key="index" class="p-2 text-center bg-white shadow-md rounded-md hover:bg-blue-100 cursor-default">
        <div class="text-lg">{{ place.name }}</div>
        <div>{{ place.description }}</div>
      </div>
    </div>
  </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'App',
  data() {
    return {
      places: []
    }
  },
  methods: {
    fetchDummy() {
      let place = {
        name: "Rijks Museum",
        description: "The Rijksmuseum is a Dutch national museum dedicated to arts and history in Amsterdam. The museum is located at the Museum Square in the borough Amsterdam South, close to the Van Gogh Museum, the Stedelijk Museum Amsterdam, and the Concertgebouw."
      }

      for (let i = 0; i < 9; i++) 
        this.places.push(place)
    },
    async fetchPlaces() {
      await axios.get('http://localhost:8000/api').then((response) => {
        if (response.data) {
          this.places = response.data.places
        }
      })
      // fetch('http://localhost:8000/api', {
      //   method: "GET",
      //   headers: {
      //     "Content-type" : "application/json"
      //   }
      // })
      //   .then(response => response.json())
      //   .then(data => console.log(data));
    }
  },
  mounted() {
    // uncomment for using api
    this.fetchPlaces()

    // comment when using api
    // this.fetchDummy()
  },
}
</script>
