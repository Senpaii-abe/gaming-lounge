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
                    <p class="font-semibold text-lg">{{ userStore.user.name }}</p>
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
            <div class="rounded-full bg-transparent space-y-1 text-right">
                <form 
                    v-on:submit.prevent="submitForm"
                    method="post">
                    <textarea v-model="body" class="p-4 w-full bg-purple_main rounded-full" placeholder="let's talk gaming.."></textarea>
                    <button class="active:bg-violet1 inline-block text-center w-24 p-2 bg-purple_main text-white rounded-full">post</button>
                </form>
            </div>
            <!-- post -->     
            <div class="p-4 bg-purple_main rounded-full"
                    v-for="post in posts" 
                    v-bind:key="post.id"> <!-- loop ng post -->
                <!-- top part ng post-->
                <div class="mb-4 flex items-center justify-between">
                    <!-- username nd pfp -->
                    <div class="flex items-center space-x-4">
                        <img src="https://i.pravatar.cc/300?img=70" class="w-[45px] rounded-img">
                        <p class="font-medium">{{ post.created_by.name}}</p>
                    </div>
                    <!-- time posted -->
                    <p class="text-gray-400 text-xs font-light">{{ post.created_at_formatted}}</p> 
                </div>

                    <p class="text-base/7 font-light">{{ post.body }}</p>

                    <!-- if may image <img src="https://images.unsplash.com/photo-1661956602868-6ae368943878?ixlib=rb-4.0.3&amp;ixid=MnwxMjA3fDF8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&amp;auto=format&amp;fit=crop&amp;w=2670&amp;q=80" class="w-full rounded-full"> --> 

                <!-- lower part ng post -->
                <div class="mt-6 flex justify-between">
                    <div class="flex space-x-6">
                        <!-- likes -->
                        <div class="flex items-center space-x-2">
                            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
                                <path stroke-linecap="round" stroke-linejoin="round" d="M21 8.25c0-2.485-2.099-4.5-4.688-4.5-1.935 0-3.597 1.126-4.312 2.733-.715-1.607-2.377-2.733-4.313-2.733C5.1 3.75 3 5.765 3 8.25c0 7.22 9 12 9 12s9-4.78 9-12z"></path>
                            </svg>  
                            
                            <span class="text-gray-300 text-xs">82 likes</span>
                        </div>
                        <!-- comments -->
                        <div class="flex items-center space-x-2">
                            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
                                <path stroke-linecap="round" stroke-linejoin="round" d="M12 20.25c4.97 0 9-3.694 9-8.25s-4.03-8.25-9-8.25S3 7.444 3 12c0 2.104.859 4.023 2.273 5.48.432.447.74 1.04.586 1.641a4.483 4.483 0 01-.923 1.785A5.969 5.969 0 006 21c1.282 0 2.47-.402 3.445-1.087.81.22 1.668.337 2.555.337z"></path>
                            </svg> 

                            <span class="text-gray-300 text-xs ">0 comments</span>
                        </div>
                    </div>
                    <div> 
                        <!-- three dots -->
                        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
                            <path stroke-linecap="round" stroke-linejoin="round" d="M12 6.75a.75.75 0 110-1.5.75.75 0 010 1.5zM12 12.75a.75.75 0 110-1.5.75.75 0 010 1.5zM12 18.75a.75.75 0 110-1.5.75.75 0 010 1.5z"></path>
                        </svg>   
                    </div>   
                </div>  
            </div>
        </div>
        
        <!-- right side -->
        <div class="main-right col-span-1 space-y-6">
            
            <div>
                <input type="text" placeholder="search" class="bg-purple_main w-full py-3 px-6 rounded-large">
            </div>

            <ul class="text-center">
                <li class="mb-4">
                    <a href="">                     
                        <img src="/assets/img/ads-1.png" class="h-auto max-w-full"
                    alt="logo" />
                    </a>
                </li>

                <li>
                    <a href="">
                        <img src="/assets/img/ads-2.png" class="h-auto max-w-full"
                    alt="logo" />
                    </a>
                </li>
            </ul>

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

export default {
    name: 'ProfileView',

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
            posts:[],
            body: '',
        }
    }, 
    mounted(){
        this.getFeed()
    },
    methods: {
        getFeed(){
            axios
                .get(`/api/posts/profile/${this.$route.params.id}/`) //using ` for the js
                .then(response => {
                    console.log('data', response.data)

                    this.posts = response.data
                })
                .catch(error => {
                    console.log('error', error)
                })
        },
        submitForm(){
            console.log('submitForm', this.body) //textarea v-model="body" 

            axios //sending to backend
                .post('/api/posts/create/', {
                    'body': this.body
                })
                .then(response =>{
                    console.log('data', response.data)

                    this.posts.unshift(response.data)
                    this.body = ''
                })
                .catch(error =>{
                    console.log('error', error)
                })
        }
    }
}
</script>