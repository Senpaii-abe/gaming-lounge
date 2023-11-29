<template>
  <div class="flex justify-center items-center h-screen">
    <form @submit.prevent="handleSubmit" class="p-6 bg-[#c4b6e1] max-w-2xl rounded-full"> 
      <div class="mb-6">
        <img src="/assets/img/logo/gl_logo.png" alt="logo" class="mx-auto"/>
      </div>

      <h2 class="mb-6 leading-tight font-black text-black text-3xl text-center">gaming interests</h2>
        <p class="mb-10 text-black text-40 text-center">
          pick things you would like to see in your feed
        </p>

        <div class="grid gap-5 grid-cols-3 place-content-center">
          <div
            v-for="option in options"
            :key="option.id"
            :class="{'bg-purple_main text-white': selectedOptions.includes(option.value)}"
            class="mx-2 bg-[#8250CB] py-3 px-3 text-black text-center rounded-full"
          >
            <label>
              <input type="checkbox" :value="option.value" v-model="selectedOptions" class="hidden" /> {{ option.label }}
            </label>
        </div>
        
      </div>
      <div class="my-7 mx-4w-4/5 text-center">
          <button type="submit" class=" text-center active:bg-purple_main inline-block w-full p-2 bg-[#8250CB] text-white rounded-full">Continue</button>
        </div>
    </form>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue';
import axios from 'axios'
import { useUserStore } from '@/stores/user'
import { useRouter } from 'vue-router';

const userStore = useUserStore()
const router = useRouter();

const options = ref([]);
const selectedOptions = ref([]) 

onMounted(async () => {
  try {
    // Fetch game categories from the backend
    const response = await axios.get('/api/get_game_categories/');
    options.value = response.data.map(category => ({
      id: category.id,
      label: category.game_category,
      value: category.game_category,
    }));
  } catch (error) {
    console.error('Error fetching game categories', error);
  }
});

const handleSubmit = async () => {
  try {
    const user_id = userStore.user.id;

    // Step 1: Update user preferences
    const response = await axios.post(`/api/update_user_preferences/${user_id}/`, {
      pref_game_category: selectedOptions.value.join(','), // Save selected options as a comma-separated string
    });

    console.log(response.data);
    // console.log('Game Titles:', gameTitles);
    router.push('/gametitle');

  } 
  catch (error) {
    console.error('Error processing form data', error);
  }
};

</script>
