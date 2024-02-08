<template>
  <div>
    <h1 class="text-white">Мацюк Владимир Николаевич, P3215, v909</h1>
    <br />

    <!-- <h2>{{ isRegistering ? 'Register' : 'Login' }}</h2> -->

    <!-- Login Form -->
    <form v-if="!isRegistering" @submit.prevent="submitForm">
      <label for="username">Username: </label>
      <input v-model="username" type="text" id="username" required />

      <br />
      <label for="password">Password: </label>
      <input v-model="password" type="password" id="password" required />
      <br />
      <br />

      <button type="submit">Login</button>
      <button type="button" @click="toggleRegistration">Switch to Register</button>
      <br />
    </form>

    <!-- Registration Form -->
    <form v-if="isRegistering" @submit.prevent="submitForm">
      <label for="username">Username: </label>
      <input v-model="username" type="text" id="username" required />
      <br />

      <label for="password">Password: </label>
      <input v-model="password" type="password" id="password" required />
      <br />
      <br />

      <button type="submit">Register</button>
      <button type="button" @click="toggleRegistration">Switch to Login</button>
    </form>
  </div>
</template>

<script lang="ts">
import api from '../api'
import { onMounted, ref } from 'vue'

import { useNotification } from '@kyvg/vue3-notification'
import router from '@/router'
const notification = useNotification()

export default {
  setup() {
    const username = ref('')
    const password = ref('')
    const isRegistering = ref(false)

    const notification = useNotification()

    const submitForm = async () => {
      try {
        if (isRegistering.value) {
          // Registration logic
          const response = await api.post('/auth/register', {
            username: username.value,
            password: password.value
          })
          console.log('Registration successful:', response.data)
          const msg = response?.data?.message
          notification.notify({
            title: 'Registration successful',
            text: msg,
            type: 'success'
          })
        } else {
          // Login logic
          const response = await api.post('/auth/login', {
            username: username.value,
            password: password.value
          })
          localStorage.setItem('token', response.data)
          console.log('Login successful:', response.data)
          notification.notify({
            title: 'Login successful',
            text: '',
            type: 'success'
          })
          // Redirect to the main page upon successful login
          router.push('/main')
        }
      } catch (error: any) {
        const msg = error?.response?.data?.message
        notification.notify({
          title: 'Error',
          text: msg,
          type: 'error'
        })
        console.error('Error:', msg)
        // Handle errors (display error message, etc.)
      }
    }
    const toggleRegistration = () => {
      isRegistering.value = !isRegistering.value
    }

    return {
      username,
      password,
      isRegistering,
      submitForm,
      toggleRegistration
    }
  }
  // data() {
  //   return {
  //     username: '',
  //     password: '',
  //     isRegistering: false
  //   }
  // },
  // methods: {

  // }
}
</script>

<style scoped>
div {
  text-align: center;
  margin: 20px;
}
/* Add your styling here */
</style>
