<template>
  <div class="flex justify-center items-center h-screen">
    <div class="bg-white p-6 rounded shadow-md">
      <h2 class="text-xl mb-4">Привет, {{ firstName }} {{ lastName }}!</h2>
      <form @submit.prevent="submit">
        <label for="birth_date">Введите свою дату рождения:</label>
        <input v-model="birthDate" type="date" id="birth_date" required class="border p-2 rounded">
        <button type="submit" class="mt-4 bg-blue-500 text-white p-2 rounded">Продолжить</button>
      </form>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter, useRoute } from 'vue-router'

const birthDate = ref(null)
const router = useRouter()
const route = useRoute()

const firstName = ref(route.query.first_name || '')
const lastName = ref(route.query.last_name || '')
const username = ref(route.query.username || '')

const submit = async () => {
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
    router.push({ name: 'ClientInfo', params: { data } })
  }
}
</script>
