<template>
    <div class="flex justify-center items-center h-screen">
      <form @submit="" class="p-6 bg-[#c4b6e1] max-w-2xl rounded-full"> 
        <div class="mb-6">
			<img src="/assets/img/logo/gl_logo.png" alt="logo" class="mx-auto"/>
		</div>
        <h2 class="mb-6  leading-tight font-black text-black text-3xl text-center">gaming intersets</h2>
        <p class="mb-10 text-black text-40 text-center">
                  pick things you would like to see in your feed
        </p>
        <div class="grid gap-5 grid-cols-3 place-content-center">
            <label v-for="option in options" :key="option.id" :class="{ 'bg-purple_main text-white':selectedOptions.includes(option.value) }" class="mx-2 bg-white py-3 px-3 text-black text-center rounded-full">{{ option.label }}
                <input type="checkbox" :value="option.value" v-model="selectedOptions" class="hidden"/>
            </label>
        </div>

        <div class="my-5 text-center">
            <button type="submit" class=" active:bg-purple_main inline-block text-center w-3/4 p-2 bg-[#8250CB] text-white rounded-full">Continue</button>
        </div>
      </form>
    </div>
    <div class="flex flex-col">
  </div>
  </template>

<script lang="ts" setup>
import { ref } from 'vue';

function handleSubmit() {
    // Do something with selectedOptions
    console.log(selectedOptions.value);
  }

const options = ref<{ id: number; label: string; value: string }[]>([
  { id: 1, label: 'MOBA', value: 'option1' },
  { id: 2, label: 'FPS', value: 'option2' },
  { id: 3, label: 'Real Time Strategy', value: 'option3' },
  { id: 4, label: 'Role Playing Games', value: 'option4' },
  { id: 5, label: 'Horror', value: 'option5' },
  { id: 6, label: 'Survival', value: 'option6' },
  { id: 7, label: 'action', value: 'option7' },
  { id: 8, label: 'open world', value: 'option8' },
  { id: 9, label: 'battle royale', value: 'option9' },
  { id: 10, label: 'family', value: 'option10' },
  { id: 11, label: 'creative', value: 'option11' },
  { id: 12, label: 'independent', value: 'option12' },
  { id: 13, label: 'retro', value: 'option13' },
  { id: 14, label: 'classic', value: 'option14' },
  { id: 15, label: 'rhythm', value: 'option15' },
]);

const selectedOptions = ref<string[]>([]);

</script>
