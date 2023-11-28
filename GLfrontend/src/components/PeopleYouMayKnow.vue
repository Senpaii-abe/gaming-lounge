<template>
    <div class="p-4 bg-purple_main border-gray-200 rounded-full">
        <h3 class="mb-6 font-semibold text-xl tracking-wide text-center">people you may know</h3>

        <div class="space-y-4">
            <div 
                class="flex items-center justify-between"
                v-for="user in users"
                v-bind:key="user.id"
            >
                <div class="flex items-center space-x-2">
                    <img :src="user.get_avatar" class="h-[40px] w-[40px] rounded-img">
                                    
                    <p class="text-xs"><strong>{{ user.name }}</strong></p>
                </div>

                <RouterLink :to="{name: 'profile', params: {id: user.id}}" class="py-2 px-3 bg-purple-600 text-white text-xs rounded-lg">Show</RouterLink>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
import { RouterLink } from 'vue-router'

export default {
    data() {
        return {
            users: []
        };
    },
    mounted() {
        this.getFriendSuggestions();
    },
    methods: {
        getFriendSuggestions() {
            axios
                .get('/api/friends/suggested/')
                .then(response => {
                console.log(response.data);
                this.users = response.data;
            })
                .catch(error => {
                console.log('error', error);
            });
        }
    },
    components: { RouterLink }
}

</script>