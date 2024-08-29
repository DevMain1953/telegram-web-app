<template>
    <div class="flex justify-center items-center h-screen">
      <div class="bg-white p-6 rounded shadow-md text-center">
        <h2 class="text-xl">Привет, {{ clientInfo.first_name }}!</h2>
        <p>До твоего дня рождения осталось {{ clientInfo.days_to_birthday }} дней.</p>
        <button @click="share" class="mt-4 bg-green-500 text-white p-2 rounded">Поделиться</button>
      </div>
    </div>
  </template>
  
  <script setup>
  import { onMounted, ref } from 'vue'
  import { useRoute } from 'vue-router'
  
  const clientInfo = ref({})
  
  onMounted(() => {
    const route = useRoute()
    clientInfo.value = route.params.data || JSON.parse(localStorage.getItem('clientInfo'))
  })
  
  const share = () => {
    const shareLink = `${window.location.origin}/share/${clientInfo.value.username}`
    navigator.clipboard.writeText(shareLink)
    alert('Ссылка скопирована в буфер обмена!')
  }
  </script>
  