<template>
  <div class="flex justify-center items-center h-screen">
    <div class="bg-white p-6 rounded shadow-md text-center" v-if="clientInfo">
      <h2 class="text-xl">Привет, {{ clientInfo.first_name }}, {{ clientInfo.last_name }} - {{ clientInfo.username }}!</h2>
      <p>До твоего дня рождения осталось {{ clientInfo.days_to_birthday }} дней.</p>
      <button @click="share" class="mt-4 bg-green-500 text-white p-2 rounded">Поделиться</button>
    </div>
    <div v-else class="text-center">Загрузка данных...</div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRoute } from 'vue-router'

const route = useRoute()
const clientInfo = ref(null)

onMounted(async () => {
  const response = await fetch(`/api/clients/${route.params.username}`)
  if (response.ok) {
    clientInfo.value = await response.json()
  } else {
    alert('Клиент не найден')
  }
})

const share = () => {
  const shareLink = `tg://resolve?domain=virgo_cluster_bot&start=client-info/${clientInfo.value.username}`
  navigator.clipboard.writeText(shareLink)
  alert('Ссылка скопирована в буфер обмена!')
}
</script>
