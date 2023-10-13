<template>
    <div class="max-w-7xl mx-auto grid grid-cols-4 gap-4">

        <!-- left side 
             col-span-1: takes 1 of the 4 columns -->
        <div class="main-left col-span-1 space-y-6"> 
            <!-- profile -->
            <div class="p-4 bg-purple_main rounded-full">
                <!-- profile picture -->
                <div class="flex items-center space-x-4">
                    <img :src="user.get_avatar" class="w-[80px] rounded-img">
                    <p class="font-semibold text-xl">{{ user.name }}</p>
                </div>
                <!-- charisma points nd posts-->
                <div class="my-5 px-12 py-4 flex flex-row justify-between items-center bg-dark_purple rounded-full text-center">
                    <div>
                        <p class="text-lg/none">{{ user.posts_count }}</p>
                        <label class="text-sm">posts</label>
                    </div>
                  
                    <div v-if="user.id">
                        <p class="text-lg/none">{{ user.friends_count }}</p>
                        <RouterLink :to="{name: 'friends', params: {id: user.id}}" class="text-sm">friends</RouterLink>
                    </div>
                
                </div>
                <!-- about me -->
                <p class="px-1 text-sm/5 font-light text-justify">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean vitae velit vel urna viverra pellentesque. Etiam sed neque sit amet nibh ullamcorper tempor. Etiam finibus, felis in semper rutrum, arcu nibh vehicula nulla.</p>
                
                <!-- send friend request button -->
                <div class = "mt-6">
                    <button 
                        class = "inline-block py-3 hover:bg-purple-600 bg-[#28183e] font-semibold rounded-full w-full" 
                        @click="sendFriendshipRequest"
                        v-if="userStore.user.id !== user.id"
                        >
                        add friend
                    </button>
                    <button 
                        class = "inline-block py-3 mt-4 hover:bg-purple-600 bg-[#28183e] font-semibold rounded-full w-full" 
                        @click="sendDirectMessage"
                        v-if="userStore.user.id !== user.id"
                        >
                        Send Direct Message
                    </button> 
                    
                    <!-- edit profile button -->
                    <RouterLink
                        class = "inline-block mr-2 py-3 hover:bg-purple-600 bg-[#28183e] font-semibold rounded-full w-full" 
                        to="/profile/edit"
                        v-if="userStore.user.id === user.id"
                        >
                        Edit Profile
                    </RouterLink> 

                    <!-- Logout button -->
                    <button 
                        class = "inline-block py-3 hover:bg-red-400 bg-[#28183e] font-semibold rounded-full w-full" 
                        @click="logout"
                        v-if="userStore.user.id === user.id"
                        >
                        logout
                    </button> 
                 </div>
            </div>  
            <!-- trending games -->
            <div class="p-4 bg-purple_main rounded-full">
                <h3 class="mb-1 text-lg">useful links</h3>

                <p class="text-base/7 font-light mb-6">our instance rules are here and cover the ideals and how we want this community to evolve.</p>
                <p class="text-base/7 font-light mb-2">where you can download games:</p>

                <ul class="list-inside">

                    <li class="p-1 hover:underline">
                        <a href="https://www.riotgames.com/en" target="_blank" rel="noopener noreferrer" ><img src="/assets/img/logo/riot_logo.png" class="h-auto max-w-full"
                    alt="logo" /></a></li>
                    
                    <li class="p-1 hover:underline">
                        <a href="https://store.steampowered.com/" target="_blank" rel="noopener noreferrer" ><img src="/assets/img/logo/steam_logo.png" class="h-auto max-w-full"
                    alt="logo" /></a></li>

                    <li class="p-1 hover:underline">                       
                        <a href="https://store.epicgames.com/en-US/" target="_blank" rel="noopener noreferrer"><img src="/assets/img/logo/epic_logo.png" class="h-auto max-w-full"
                    alt="logo"/></a></li>

                    <li class="p-1 hover:underline">                       
                        <a href="https://us.shop.battle.net/en-us" target="_blank" rel="noopener noreferrer"><img src="/assets/img/logo/battle_logo.png" class="h-auto max-w-full"
                    alt="logo" /></a></li>
            
                </ul>
                

            </div>
        </div> 
        
        <!-- center -->
            <!-- col-span-2: takes 2 of the 4 columns
                 space-y-4: 6 spaces each post -->
        <div class="px-4 main-center col-span-2 space-y-6">
            <!-- write something -->
            <div 
                class="rounded-full bg-transparent space-y-1 text-right"
                v-if="userStore.user.id === user.id"
                >
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

                    <FeedItem v-bind:post="post" />
            </div>
        </div>
        
        <!-- right side -->
        <div class="main-right col-span-1 space-y-6">
            
         

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
import { useUserStore } from '@/stores/user'
import { useToastStore } from '@/stores/toast'



export default {
    name: 'ProfileView',

    setup() {
        const userStore = useUserStore()
        const toastStore = useToastStore()

        return {
            userStore,
            toastStore
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
            user: {
                id: ''
            },
            body: '',
        }
    }, 
    mounted(){
        this.getFeed()
    },
    watch: {
        '$route.params.id': {
            handler: function() {
                this.getFeed()
            },
            deep: true,
            immediate: true 
        }
    },
    // updated() {
    //     // this.getFeed()
    //     // console.log('updated')
    // },

    methods: {
        sendDirectMessage() {
            console.log('sendDirectMessage')

            axios
                .get(`api/chat/${this.$route.params.id}/get-or-create/`)
                .then(response => {
                    console.log(response.data)

                    this.$router.push('/chat')
                })
                .catch(error => {
                    console.log('error', error)
                })
        },
        sendFriendshipRequest() {
            axios
                .post(`/api/friends/${this.$route.params.id}/request/`) 
                .then(response => {
                    console.log('data', response.data)

                    if (response.data.message == 'request already sent')
                    {
                        this.toastStore.showToast(5000, 'The request has already been sent', 'bg-red-400')
                    }
                    else{
                        this.toastStore.showToast(5000, 'The request was sent!', 'bg-emerald-500')
                    }
                })
                .catch(error => {
                    console.log('error', error)
                })
        },

        getFeed(){
            axios
                .get(`/api/posts/profile/${this.$route.params.id}/`) //using ` for the js
                .then(response => {
                    console.log('data', response.data)

                    this.posts = response.data.posts
                    this.user = response.data.user

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
                    this.user.posts_count += 1 //add post count automatically in frontend
                })
                .catch(error =>{
                    console.log('error', error)
                })
        },
        logout() {
            console.log('Log out')
            this.userStore.removeToken()

            this.$router.push('/')
        }
    }
}
</script>