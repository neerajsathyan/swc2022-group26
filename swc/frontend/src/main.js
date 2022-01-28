// import { createApp } from 'vue'
import App from './App.vue'
import './index.css'

import * as Vue from 'vue'
import axios from 'axios'
import VueAxios from 'vue-axios'

// createApp(App).mount('#app')

const app = Vue.createApp(App).mount('#app')
app.use(VueAxios, axios)
