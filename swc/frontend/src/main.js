// import { createApp } from 'vue'
import App from './App.vue'
import './index.css'

import * as Vue from 'vue'
import axios from 'axios'
import VueAxios from 'vue-axios'

const app = Vue.createApp(App)

app.mount('#app')
app.use(VueAxios, axios)