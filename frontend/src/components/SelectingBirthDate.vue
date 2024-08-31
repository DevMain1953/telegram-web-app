<template>
  <div class="flex items-center justify-center h-screen bg-gray-100">
    <div class="bg-white p-6 rounded shadow-md w-full max-w-md">
      <h2 class="text-xl mb-4 text-center">Привет, {{ firstName }} {{ lastName }}!</h2>
      <label for="custom_date" class="block mb-2 text-sm font-medium text-gray-700">
        Введите свою дату рождения:
      </label>
      <div class="flex space-x-2 mb-4">
        <select v-model="selectedYear" class="border p-2 rounded">
          <option v-for="year in years" :key="year" :value="year">{{ year }}</option>
        </select>
        <select v-model="selectedMonth" class="border p-2 rounded">
          <option v-for="month in months" :key="month.index" :value="month.index">{{ month.name }}</option>
        </select>
        <select v-model="selectedDay" class="border p-2 rounded">
          <option v-for="day in daysInMonth" :key="day" :value="day">{{ day }}</option>
        </select>
      </div>
      <button @click="submit" class="w-full bg-blue-500 text-white p-2 rounded">
        Продолжить
      </button>
    </div>
  </div>
</template>

<script lang="ts" setup>
import { ref, computed } from 'vue'
import { useRouter, useRoute } from 'vue-router'

interface Month {
  index: number
  name: string
}

const today = new Date()
const currentYear = today.getFullYear()

const years = Array.from({ length: 100 }, (_, i) => currentYear - i)
const months: Month[] = [
  { index: 1, name: 'Январь' },
  { index: 2, name: 'Февраль' },
  { index: 3, name: 'Март' },
  { index: 4, name: 'Апрель' },
  { index: 5, name: 'Май' },
  { index: 6, name: 'Июнь' },
  { index: 7, name: 'Июль' },
  { index: 8, name: 'Август' },
  { index: 9, name: 'Сентябрь' },
  { index: 10, name: 'Октябрь' },
  { index: 11, name: 'Ноябрь' },
  { index: 12, name: 'Декабрь' },
]

const selectedYear = ref<number>(currentYear)
const selectedMonth = ref<number>(today.getMonth() + 1)
const selectedDay = ref<number>(today.getDate())

const daysInMonth = computed(() => {
  const days = new Date(selectedYear.value, selectedMonth.value, 0).getDate()
  return Array.from({ length: days }, (_, i) => i + 1)
})

const birthDate = computed(() => {
  return `${selectedYear.value}-${String(selectedMonth.value).padStart(2, '0')}-${String(selectedDay.value).padStart(2, '0')}`
})

const router = useRouter()
const route = useRoute()

const firstName = ref<string>(route.query.first_name as string || '')
const lastName = ref<string>(route.query.last_name as string || '')
const username = ref<string>(route.query.username as string || '')

const submit = async () => {
  try {
    const response = await fetch('/api/clients/', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ 
        first_name: firstName.value, 
        last_name: lastName.value, 
        username: username.value, 
        birth_date: birthDate.value 
      })
    })

    if (response.ok) {
      const data = await response.json()
      localStorage.setItem('clientInfo', JSON.stringify(data))
      router.push({ name: 'ClientInfo', params: { username: data.username } })
    } else {
      alert('Ошибка при сохранении данных клиента')
    }
  } catch (error) {
    console.error('Ошибка при выполнении запроса:', error)
    alert('Произошла ошибка при сохранении данных клиента')
  }
}
</script>
