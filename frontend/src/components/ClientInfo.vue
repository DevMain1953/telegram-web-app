<template>
  <div class="flex justify-center items-center h-screen bg-gray-100">
    <div class="bg-white p-6 rounded shadow-md text-center" v-if="clientInfo">
      <h2 class="text-xl mb-4">
        Привет, {{ clientInfo.first_name }}, {{ clientInfo.last_name }} -
        {{ clientInfo.username }}!
      </h2>
      <p>
        До твоего дня рождения осталось {{ clientInfo.days_to_birthday }} дней.
      </p>
      <button @click="share" class="mt-4 bg-green-500 text-white p-2 rounded">
        Поделиться
      </button>
    </div>
    <div v-else class="text-center">Загрузка данных...</div>
  </div>
</template>

<script lang="ts">
import { ref, onMounted } from "vue";
import { useRoute } from "vue-router";

interface ClientInfo {
  first_name: string;
  last_name: string;
  username: string;
  days_to_birthday: number;
}

export default {
  setup() {
    const route = useRoute();
    const clientInfo = ref<ClientInfo | null>(null);

    onMounted(async () => {
      try {
        const response = await fetch(`/api/clients/${route.params.username}`);
        if (response.ok) {
          clientInfo.value = await response.json();
        } else {
          alert("Клиент не найден");
        }
      } catch (error) {
        console.error("Ошибка при загрузке данных:", error);
        alert("Произошла ошибка при загрузке данных");
      }
    });

    const share = () => {
      if (clientInfo.value) {
        const shareLink = `https://t.me/virgo_cluster_bot/test_web_app?username=${clientInfo.value.username}`;
        navigator.clipboard
          .writeText(shareLink)
          .then(() => {
            alert("Ссылка скопирована в буфер обмена!");
          })
          .catch((err) => {
            console.error("Ошибка при копировании ссылки:", err);
            alert("Не удалось скопировать ссылку");
          });
      } else {
        alert("Нет данных для создания ссылки");
      }
    };

    return {
      clientInfo,
      share,
    };
  },
};
</script>
