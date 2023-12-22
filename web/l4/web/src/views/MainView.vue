<template>
  <div>
    <h2>Main Application</h2>

    <div>
      <div>
        <label for="x-coordinate">X ({{ x }}):</label>
        <button v-for="n in [-4, -3, -2, -1, 0, 1, 2, 3, 4]" :key="n" @click="setXCoordinate(n)">
          {{ n }}
        </button>
      </div>
      
      <div class="bg-red">
        <label for="y-coordinate">Y ({{ y }}):</label>
        <input v-model.number="y" type="number" :min="-3" :max="5" />
      </div>

      <div>
        <label for="radius">R ({{ r }}):</label>
        <button v-for="n in [-4, -3, -2, -1, 0, 1, 2, 3, 4]" :key="n" @click="setRadius(n)">
          {{ n }}
        </button>
      </div>
    </div>

    <canvas v-on:click="handleCoordinateClick" id="canvas" width="300" height="300" />

    <!-- Results table component -->
    <table>
      <thead>
        <tr>
          <th>X</th>
          <th>Y</th>
          <th>R</th>
          <th>Hit</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(result, index) in results" :key="index">
          <td>{{ result.x }}</td>
          <td>{{ result.y }}</td>
          <td>{{ result.r }}</td>
          <td>{{ result.hit ? 'Yes' : 'No' }}</td>
        </tr>
      </tbody>
    </table>

    <button @click="logout">Logout</button>
  </div>
</template>

<script lang="ts">
import { onMounted, ref } from 'vue'
import { drawGraph, getCursorPosition } from '../canvas'
import api from '@/api'
import { useNotification } from '@kyvg/vue3-notification'

export default {
  setup() {
    const x = ref(0)
    const y = ref(0)
    const r = ref(1)
    const results = ref([] as { x: number; y: number; r: number; hit: boolean }[])

    const notification = useNotification()

    const setXCoordinate = (newX: number) => {
      x.value = newX
    }

    const setRadius = (newR: number) => {
      r.value = newR
      redrawCoordinatePlane()
    }

    const handleCoordinateClick = async (e: MouseEvent) => {
      let { x, y } = getCursorPosition(e)
      x = ((x - 150) / 100) * r.value
      y = ((-y + 150) / 100) * r.value
      x = Math.round(x * 100) / 100
      y = Math.round(y * 100) / 100
      try {
        const response = await api.get('/check-point', {
          params: { x, y, r: r.value }
        })
        console.log(response)
        results.value.push({ x, y, r: r.value, hit: response.data.hit })
      } catch (error: any) {
        const msg = error?.response?.data?.message
        if (msg) {
          console.log(msg)
          notification.notify({
            title: 'Error',
            text: msg,
            type: 'error'
          })
        }

        console.error('There was an error checking the point:', error)
      }

      redrawCoordinatePlane()
    }

    const redrawCoordinatePlane = () => {
      drawGraph(x.value, y.value, r.value, results.value)
    }

    const logout = () => {
      // Assume the logout function is implemented correctly
    }

    onMounted(() => {
      redrawCoordinatePlane()
    })

    return {
      x,
      y,
      r,
      results,
      setXCoordinate,
      setRadius,
      handleCoordinateClick,
      redrawCoordinatePlane,
      logout
    }
  }
}
</script>

<style scoped>
table {
  width: 100%;
  border-collapse: collapse;
}

table,
th,
td {
  border: 1px solid black;
}

th,
td {
  padding: 8px;
  text-align: left;
}

/* Add other styling as needed */
</style>
