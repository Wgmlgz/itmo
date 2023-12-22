import './assets/main.css'
import 'virtual:uno.css';
import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import Notifications from '@kyvg/vue3-notification'

const app = createApp(App)

app.use(Notifications)
app.use(router)

app.mount('#app')
