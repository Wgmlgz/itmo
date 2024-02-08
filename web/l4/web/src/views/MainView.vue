<template>
  <div>
    <h1 class="text-white">Main Application</h1>
    <a class="cursor-pointer" @click="logout">Logout</a>

    <br />
    <br />
    <div class="grid grid-cols-2 place-items-center justify-center sus gap-4">
      <div class="grid m-0 gap-2">
        <div class="flex items-center justify-center gap-2 m-0 gridder">
          <label class="min-w-50px" for="x-coordinate">X = {{ x }}:</label>
          <div class="w-375px">
            <button
              v-for="n in [-4, -3, -2, -1, 0, 1, 2, 3, 4]"
              :key="n"
              @click="setXCoordinate(n)"
            >
              {{ n }}
            </button>
          </div>
        </div>

        <div class="flex items-center justify-center gap-2 m-0 gridder">
          <label class="min-w-50px" for="y-coordinate">Y = {{ y }}:</label>
          <div class="w-375px">
            <input v-model.number="y" type="number" :min="-3" :max="5" />
          </div>
        </div>

        <div class="flex items-center justify-center gap-2 m-0 gridder">
          <label class="min-w-50px" for="radius">R = {{ r }}:</label>
          <div class="w-375px">
            <button v-for="n in [-4, -3, -2, -1, 0, 1, 2, 3, 4]" :key="n" @click="setRadius(n)">
              {{ n }}
            </button>
          </div>
        </div>

        <div class="flex items-center justify-center gap-2 m-0 gridder">
          <button @click="handleButtonClick">Check</button>
          <button @click="handleRemove">Remove all</button>
        </div>
      </div>

      <div>
        <canvas
          class="rounded-md"
          v-on:click="handleCoordinateClick"
          id="canvas"
          width="300"
          height="300"
        />
      </div>
    </div>

    <!-- Results table component -->
    <div class="p-10">
      <table class="bg-white text-black rounded-md">
        <thead class="font-bold">
          <tr>
            <th class="font-bold">X</th>
            <th class="font-bold">Y</th>
            <th class="font-bold">R</th>
            <th class="font-bold">Hit</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(result, index) in results" :key="index">
            <td>{{ result.x }}</td>
            <td>{{ result.y }}</td>
            <td>{{ result.r }}</td>
            <td>{{ result.hit ? '✅' : '❌' }}</td>
          </tr>
        </tbody>
      </table>
    </div>
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

      handleCheck(x, y, r.value)
    }

    const handleButtonClick = async (e: MouseEvent) => {
      // let { x, y } = getCursorPosition(e)
      // x = ((x - 150) / 100) * r.value
      // y = ((-y + 150) / 100) * r.value
      // x = Math.round(x * 100) / 100
      // y = Math.round(y * 100) / 100

      handleCheck(x.value, y.value, r.value)
    }

    const handleCheck = async (x: number, y: number, r: number) => {
      try {
        const response = await api.get('/check-point', {
          params: { x, y, r },
          headers: {
            Authorization: `Bearer ${localStorage.getItem('token')}`
          }
        })
        results.value.push({ x, y, r, hit: response.data.hit })
      } catch (error: any) {
        const msg = error?.response?.data?.message
        if (msg) {
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

    const handleRemove = async () => {
      try {
        const { data } = await api.delete('/results', {
          headers: {
            Authorization: `Bearer ${localStorage.getItem('token')}`
          }
        })
        results.value = []
        results.value.pop()
      } catch (error: any) {
        const msg = error?.response?.data?.message
        if (msg) {
          notification.notify({
            title: 'Error',
            text: msg,
            type: 'error'
          })
        }

        console.error('There was an error removing the points:', error)
      }

      redrawCoordinatePlane()
    }

    const redrawCoordinatePlane = () => {
      drawGraph(x.value, y.value, r.value, results.value)
    }

    const initTable = async () => {
      const { data } = await api.get('results', {
        headers: {
          Authorization: `Bearer ${localStorage.getItem('token')}`
        }
      })
      results.value = data
    }

    const logout = () => {
      window.location.href = '../'
    }

    onMounted(async () => {
      await initTable()
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
      handleButtonClick,
      handleRemove,
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

<style scoped>
.sus > div {
  text-align: left;
  margin: 0px;
}
/* Global styles */
/* div > div {
    display: flex;
    justify-content: space-around;
    margin-bottom: 10px;
  } */

label {
  display: block;
  /* margin-bottom: 5px; */
  font-weight: bold;
}

input {
  width: 100%;
  padding: 8px;
  /* margin-bottom: 10px; */
  box-sizing: border-box;
}

table {
  width: 100%;
  border-collapse: collapse;
  margin-top: 20px;
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

div {
  text-align: center;
}
/* Media queries for responsive design */
@media (min-width: 1207px) {
  /* Desktop styles */
  h1 {
    font-size: 32px;
  }

  /* div > div {
      flex-direction: row;
    } */
}

@media (min-width: 835px) and (max-width: 1206px) {
  /* Tablet styles */
  h1 {
    font-size: 28px;
  }

  .sus {
    grid-template-columns: repeat(1, minmax(0, 1fr));
  }
  /* div > div {
      flex-direction: column;
    } */
}

@media (max-width: 834px) {
  /* Mobile styles */
  h1 {
    font-size: 24px;
  }
  .gridder {
    display: grid;
  }
  .sus {
    grid-template-columns: repeat(1, minmax(0, 1fr));
  }
  /* div > div {
      flex-direction: column;
    } */
}
</style>
