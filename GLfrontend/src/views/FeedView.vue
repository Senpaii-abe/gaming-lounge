<template>
    <!-- 
        mx-auto: center of the screen 
        put "grid" or "flex" to assign the display before adding "grid-cols" or "flex-cols"
        space-(y or x)-number: space for each elements like posts for example
        
        check tailwind.config.js for more configurations
        bg-purple_main: color ng header
        bg-blue_link: color ng links

        text-base/7 font-light: default class ng texts sa post
        rounded-full: default class ng borders natin
    -->    
    <div class="max-w-7xl mx-auto grid grid-cols-4 gap-4">

        <!-- left side 
             col-span-1: takes 1 of the 4 columns -->
        <div class="main-left col-span-1 space-y-6"> 
            <!-- profile -->
            <div  class="p-4 bg-purple_main rounded-full">
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
            <!-- post area -->     
            <div class="p-4 bg-purple_main rounded-full"
                    v-for="post in posts" 
                    v-bind:key="post.id"> <!-- loop ng post -->

                <FeedItem v-bind:post="post" />
            </div>
        </div>
        
        <!-- right side -->
        <div class="main-right col-span-1 space-y-6">
            <!-- <div class="p-4 bg-purple_main rounded-full">
                <h3 class="mb-6 text-xl">trending topics</h3>
                        <div class="space-y-4">
                            <div class="flex items-center justify-between">
                                <div class="flex items-center space-x-2">
                                    <img src="https://i.pravatar.cc/300?img=70" class="w-[40px] rounded-full">
                                    
                                    <p class="text-xs">Code With Stein</p>
                                </div>

                                <a href="#" class="py-2 px-3 bg-purple-600 text-white text-xs rounded-lg">Show</a>
                            </div>

                            <div class="flex items-center justify-between">
                                <div class="flex items-center space-x-2">
                                    <img src="https://i.pravatar.cc/300?img=70" class="w-[40px] rounded-full">
                                    
                                    <p class="text-xs">Code With Stein</p>
                                </div>

                                <a href="#" class="py-2 px-3 bg-purple-600 text-white text-xs rounded-lg">Show</a>
                            </div>

                            <div class="flex items-center justify-between">
                                <div class="flex items-center space-x-2">
                                    <img src="https://i.pravatar.cc/300?img=70" class="w-[40px] rounded-full">
                                    
                                    <p class="text-xs">Code With Stein</p>
                                </div>

                                <a href="#" class="py-2 px-3 bg-purple-600 text-white text-xs rounded-lg">Show</a>
                            </div>
                        </div>
            </div> -->
            <!-- <div>
                <input type="text" placeholder="search" class="bg-purple_main w-full py-3 px-6 rounded-large">
            </div> -->
            <div class="flex">
                    <div class="flex w-10 items-center justify-center rounded-tl-lg rounded-bl-lg border-r border-gray-200 bg-white p-5">
                        <svg viewBox="0 0 20 20" aria-hidden="true" class="pointer-events-none absolute w-5 fill-gray-500 transition">
                            <path d="M16.72 17.78a.75.75 0 1 0 1.06-1.06l-1.06 1.06ZM9 14.5A5.5 5.5 0 0 1 3.5 9H2a7 7 0 0 0 7 7v-1.5ZM3.5 9A5.5 5.5 0 0 1 9 3.5V2a7 7 0 0 0-7 7h1.5ZM9 3.5A5.5 5.5 0 0 1 14.5 9H16a7 7 0 0 0-7-7v1.5Zm3.89 10.45 3.83 3.83 1.06-1.06-3.83-3.83-1.06 1.06ZM14.5 9a5.48 5.48 0 0 1-1.61 3.89l1.06 1.06A6.98 6.98 0 0 0 16 9h-1.5Zm-1.61 3.89A5.48 5.48 0 0 1 9 14.5V16a6.98 6.98 0 0 0 4.95-2.05l-1.06-1.06Z"></path>
                        </svg>
                    </div>
                    <input type="search" class="w-full bg-white pl-2 text-black text-base font-semibold outline-0" placeholder="Search..." id="">
                    <button @click="search" class="p-3 bg-purple_main w-15 p-2 rounded-tr-lg rounded-br-lg text-white font-semibold hover:bg-blue-800 transition-colors">Search</button>
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
import FeedItem from '../components/FeedItem.vue'

export default {
    name: 'FeedView',


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
            posts:[],
            body: '',
        }
    },
    mounted(){
        this.getFeed()
    },
    methods: 
    {
        getFeed()
        {
            axios
                .get('/api/posts/')
                .then(response => {
                    console.log('data', response.data)

                    this.posts = response.data
                })
                .catch(error => {
                    console.log('error', error)
                })
        },
        submitForm()
        {
            console.log('submitForm', this.body) //textarea v-model="body" 

            axios //sending to backend
                .post('/api/posts/create/', 
                {
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
        },
        search() 
        {
        // Redirect to the search page with the query as a URL parameter
        this.$router.push({ name: 'search', query: { q: this.searchQuery } });
        },
    }
}
</script>