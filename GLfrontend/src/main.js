import { createApp } from 'vue'
import { createPinia } from 'pinia'

import App from './App.vue'
import router from './router'
import axios from 'axios'

import './assets/main.css'

// axios.default.baseURL = 'https://127.0.0.1:8000/'
axios.defaults.baseURL = import.meta.env.VITE_API_URL
// axios.defaults.baseURL = import.meta.env.VITE_API_URL

const app = createApp(App)

app.use(createPinia())
app.use(router,axios)

app.mount('#app')
