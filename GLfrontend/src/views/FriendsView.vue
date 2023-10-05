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
            <div class="bg-transparent rounded-full">
                <h3 class="mb-2 text-2xl font-semibold text-center">topics</h3>
                        <div class="space-y-4 text-center">
                            <div class="flex items-center justify-between">                                               
                                <a href="#" class="py-2 px-3 text-lg rounded-large w-full border border-gray hover:bg-purple_main">Valorant</a>
                            </div>
                            <div class="flex items-center justify-between ">                                               
                                <a href="#" class="w-full border border-gray hover:bg-purple_main py-2 px-3 text-lg rounded-large">Farlight 84</a>
                            </div>
                            <div class="flex items-center justify-between ">                                               
                                <a href="#" class="w-full border border-gray py-2 px-3 text-lg rounded-large hover:bg-purple_main ">League of Legends</a>
                            </div>
                            <div class="flex items-center justify-between ">                                               
                                <a href="#" class="w-full border border-gray py-2 px-3 text-lg rounded-large hover:bg-purple_main ">Action</a>
                            </div>
                            <div class="flex items-center justify-between ">                                               
                                <a href="#" class="w-full border border-gray py-2 px-3 text-lg rounded-large hover:bg-purple_main ">Phasmaphobia</a>
                            </div>

                        
                        </div>
            </div>
        </div> 
        
        <!-- center -->
            <!-- col-span-2: takes 2 of the 4 columns
                 space-y-4: 6 spaces each post -->
        <div class="px-4 main-center col-span-2 space-y-6">
            <!-- write something -->
            <div class="p-4 bg-purple_main border-gray-200 rounded-lg grid grid-cols-4 gap-4" v-if="friends.length">
                <div 
                    class="p-4 bg-purple_main border-gray-200 text-center rounded-lg"
                    v-for="user in friends"
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
        </div>
        
        <!-- right side -->
        <div class="main-right col-span-1 space-y-6">
            
            <div>
                <input type="text" placeholder="search" class="bg-purple_main w-full py-3 px-6 rounded-large">
            </div>

            <PeopleYouMayKnow />
            <Trends />

            <div class="p-4 bg-purple_main rounded-full">
                <h3 class="mb-6 text-lg">useful links</h3>

                <p class="text-base/7 font-light mb-6">our instance rules are here and cover the ideals and how we want this community to evolve.</p>
                <p class="text-base/7 font-light mb-2">where you can download games:</p>

                <ul class="list-inside">

                    <li class="p-1 hover:underline">
                        <a href="https://www.riotgames.com/en" target="_blank" rel="noopener noreferrer" ><img src="/assets/img/logo/riot_logo.png" class="h-auto max-w-full"
                    alt="logo" />riot games</a></li>
                    
                    <li class="p-1 hover:underline">
                        <a href="https://store.steampowered.com/" target="_blank" rel="noopener noreferrer" ><img src="/assets/img/logo/steam_logo.png" class="h-auto max-w-full"
                    alt="logo" />steam</a></li>

                    <li class="p-1 hover:underline">                       
                        <a href="https://store.epicgames.com/en-US/" target="_blank" rel="noopener noreferrer"><img src="/assets/img/logo/epic_logo.png" class="h-auto max-w-full"
                    alt="logo"/>epic games</a></li>

                    <li class="p-1 hover:underline">                       
                        <a href="https://us.shop.battle.net/en-us" target="_blank" rel="noopener noreferrer"><img src="/assets/img/logo/battle_logo.png" class="h-auto max-w-full"
                    alt="logo" />battle.net</a></li>
            
                </ul>
                

            </div>
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
    },
    data(){
        return {
            user: {},
            friendshipRequests: [],
            friends: [],
        }
    }, 
    mounted() {
        this.getFriends()
    },

    methods: {
        getFriends(){
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