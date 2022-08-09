import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import components from "@/components/GlobalUI"
import axios from "axios"

axios.defaults.baseURL = "http://127.0.0.1:8000/"

const app = createApp(App)

components.forEach(function(component){
	app.component(component.name,component)
})

app.use(store).use(router).mount('#app')
