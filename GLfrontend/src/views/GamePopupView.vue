<template>
  <div class="flex justify-center items-center h-screen">
    <form @submit.prevent="handleSubmit" class="p-6 bg-[#c4b6e1] max-w-2xl rounded-full">
      <div class="mb-6">
        <img src="/assets/img/logo/gl_logo.png" alt="logo" class="mx-auto" />
      </div>

      <h2 class="mb-6 leading-tight font-black text-black text-3xl text-center">Gaming Interests</h2>
      <p class="mb-10 text-black text-40 text-center">
        Select the game titles you'd like to see in your feed.
      </p>

      <div class="grid gap-5 grid-cols-3 place-content-center">
        <div v-for="title in gameTitles" :key="title.id" :class="{'bg-purple_main text-white': selectedGameTitles.includes(title.id)}" class="mx-2 bg-[#8250CB] py-3 px-3 text-black text-center rounded-full">
          <label>
            <input type="checkbox" :value="title.id" v-model="selectedGameTitles" class="hidden" /> {{ title.title }}
          </label>
        </div>
      </div>

      <div class="my-7 w-full text-center">
        <button type="submit" class="text-center active:bg-purple_main inline-block w-full p-2 bg-[#8250CB] text-white rounded-full">Continue</button>
      </div>
    </form>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import axios from 'axios';
import { useUserStore } from '@/stores/user';
import { useRouter } from 'vue-router';

const userStore = useUserStore();
const router = useRouter();

const selectedTitles = ref([]);
const gameTitles = ref([]);
const selectedGameTitles = ref([]);

onMounted(async () => {
  try {
    // Ensure userStore.user is available
    if (userStore.user) {
      // Fetch user data including pref_game_category and game_titles
      const response = await axios.get(`/api/get_user/${userStore.user.id}/`);
      const userData = response.data;

      // Log the retrieved user data
      console.log('User Data:', userData);

      // Access and log game titles if it exists
      if (userData.game_titles) {
        // Extract unique titles from game_titles
        const uniqueTitles = [];
        const titleSet = new Set();

        for (const title of userData.game_titles) {
          if (!titleSet.has(title.id)) {
            titleSet.add(title.id);
            uniqueTitles.push(title);
          }
        }

        gameTitles.value = uniqueTitles;
        console.log('Game Titles:', gameTitles.value);
      } else {
        console.error('Game titles not available in user data');
      }
    } else {
      console.error('User data not available');
    }
  } catch (error) {
    console.error('Error fetching user data', error);
  }
});

const handleSubmit = async () => {
  try {
    const user_id = userStore.user.id;
    const selectedTitlesArray = selectedGameTitles.value.length > 0 ? [...selectedGameTitles.value] : null;

    console.log('Selected Titles:', selectedTitlesArray);

    // Step 1: Update user preferences
    const response = await axios.post(`/api/update_user_prefgametitle/${user_id}/`, {
      pref_game_titles: selectedTitlesArray,
    });

    console.log(response.data);
    // Step 2: Redirect or perform other actions
    router.push('/feed'); // Change this to your desired next page
  } catch (error) {
    console.error('Error processing form data', error);
  }
};
</script>