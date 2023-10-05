<template>
    <div class="max-w-7xl mx-auto grid grid-cols-4 gap-4">
        <!--Search bar-->
        <div class="main-left col-span-3 space-y-4">
            <div class="bg-purple_main border-gray-200 rounded-lg">
                <form v-on:submit.prevent="submitForm" class="p-4 flex space-x-4">  
                    <input v-model="query" type="search" class="p-4 w-full text-black bg-gray-100 rounded-lg" placeholder="What are you looking for?">
                    <button class="inline-block py-4 px-6 bg-purple-600 text-white rounded-lg">Search</button>
                </form>
            </div>

            <div 
            class="p-4 bg-purple_main border-gray-200 rounded-lg grid grid-cols-4 gap-4"
            v-if="users.length"
            >
                <div 
                    class="p-4 bg-purple_main border-gray-200 text-center rounded-lg"
                    v-for="user in users"
                    v-bind:key="user.id"
                >
                    <img src="https://i.pravatar.cc/300?img=70" class="mb-6 rounded-full">
                        
                    <p>
                        <strong>
                            <RouterLink :to="{name: 'profile', params:{'id': user.id}}">{{ user.name }}</RouterLink>
                        </strong>
                    </p>

                    <div class="mt-6 flex space-x-8 justify-around">
                        <p class="text-xs text-gray-500">182 friends</p>
                        <p class="text-xs text-gray-500">120 posts</p>
                    </div>
                </div>
            </div>

            <!-- post area -->
            <div class="p-4 bg-purple_main rounded-full"
                    v-for="post in posts" 
                    v-bind:key="post.id"> <!-- loop ng post -->
                
                <FeedItem v-bind:post="post" />
            </div>
        </div>

        <div class="main-right col-span-1 space-y-4">
           <PeopleYouMayKnow />
           <Trends />
        </div>
    </div>
</template>

<script>
import axios from 'axios'
import PeopleYouMayKnow from '../components/PeopleYouMayKnow.vue' 
import Trends from '../components/Trends.vue'
import FeedItem from '../components/FeedItem.vue'

export default {
    name: 'SearchView',
    components: {
        PeopleYouMayKnow,
        Trends,
        FeedItem,
    },

    data() {
        return {
            query: '',
            searchQuery: '',
            users: [],
            posts: []
        }
    },

    methods: 
    {
        submitForm() 
        {
            console.log('submitForm', this.query)

            axios
                .post('/api/search/', 
                {
                    query: this.query
                })
                .then(response => 
                {
                    console.log('response:', response.data)

                    this.users = response.data.users
                    this.posts = response.data.posts
                })
                .catch(error =>
                {
                    console.log('error:', error)
                })
        }
    }


}
</script>