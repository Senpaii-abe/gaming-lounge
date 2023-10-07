<template>
    <div class="max-w-7xl mx-auto grid grid-cols-4 gap-4">

        <!-- left side 
             col-span-1: takes 1 of the 4 columns -->
        <div class="main-left col-span-1 space-y-6"> 
            <!-- profile -->
            <div class="p-4 bg-purple_main rounded-full">
                <!-- profile picture -->
                <div class="flex items-center space-x-4">
                    <img src="https://i.pravatar.cc/300?img=70" class="w-[80px] rounded-img">
                    <p class="font-semibold text-lg">{{ user.name }}</p>
                </div>
                <!-- charisma points nd posts-->
                <div class="my-5 px-12 py-4 flex flex-row justify-between items-center bg-dark_purple rounded-full text-center">
                    <div>
                        <p class="text-lg/none">182</p>
                        <label class="text-sm">posts</label>
                    </div>
                     <div class="font-semibold" >
                        <p class="text-lg/none">120</p>
                        <label class="text-sm">charisma</label>
                    </div>
                
                </div>
                <!-- about me -->
                <p class="px-1 text-sm/7 font-extralight">tungkol sakin</p>
                
            </div>  
            <!-- trending games -->
    
        </div> 
        
        <!-- center -->
            <!-- col-span-2: takes 2 of the 4 columns
                 space-y-4: 6 spaces each post -->
        <div class="px-4 main-center col-span-2 space-y-6">
            <!-- write something -->
            <div class="text-center space-y-6 rounded-full" 
            v-if="friendshipRequests.length"
            >
                <div 
                    class="p-6 bg-purple_main text-center rounded-full "
                    v-for="friendshipRequests in friendshipRequests"
                    v-bind:key="friendshipRequests.id"
                >
                    <img src="https://i.pravatar.cc/100?img=70" class=" mb-4 mx-auto rounded-img">
                                 
                     @<RouterLink class="font-medium text-lg" :to="{name: 'profile', params:{'id': friendshipRequests.created_by.id}}">{{ friendshipRequests.created_by.name }}</RouterLink>
                       
                    <div class="mt-2 mb-2 flex space-x-8 justify-around">
                        <p class="text-sm text-gray-400">182 friends</p>
                        <p class="text-sm text-gray-400">120 posts</p>
                    </div>
                    <div class="mt-6 space-x-4">
                        <button class="inline-block py-3 px-5 hover:bg-[#28183e] bg-purple-800 text-sm font-medium rounded-img">accept</button>
                        <button class="inline-block py-3 px-5 hover:bg-[#28183e] bg-dark_purple text-sm font-medium rounded-img">reject</button>
                    </div>
                </div>
               
                
             </div>
             <hr>
        </div>
        
        <!-- right side -->
        <div class="main-right col-span-1 space-y-6">
            
            <div>
                <input type="text" placeholder="search" class="bg-purple_main w-full py-3 px-6 rounded-large">
            </div>

            <PeopleYouMayKnow />
            <Trends />

           
        </div>


    </div> 
</template> 


<script>

import axios from 'axios'
import PeopleYouMayKnow from '../components/PeopleYouMayKnow.vue'
import Trends from '../components/Trends.vue'
import { useUserStore } from '@/stores/user'
import FeedItem from '../components/FeedItem.vue'

export default {
    name: 'FriendsView',

    setup() {
        const userStore = useUserStore()

        return {
            userStore
        }
    },
         
    components: {
        PeopleYouMayKnow,
        Trends,
        FeedItem,
    },
    data(){
        return {
            user: {},
            friendshipRequests: [],
            friends: []
        }
    }, 
    mounted() {
        this.getFriends()
    },

    methods: {
        getFriends() {
            axios
                .get(`/api/friends/${this.$route.params.id}/`) //using ` for the js
                .then(response => {
                    console.log('data', response.data)

                    this.friendshipRequests = response.data.requests
                    this.friends = response.data.friends
                    this.user = response.data.user
                })
                .catch(error => {
                    console.log('error', error)
                })
        }
    }
}
</script>