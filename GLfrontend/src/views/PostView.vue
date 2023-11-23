<template>
    <div class="max-w-7xl mx-auto grid grid-cols-4 gap-4">

        <div class="main-left col-span-1 space-y-6"> 
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
        <div class="col-span-2 space-y-2 ">
            <div class="bg-purple_main rounded-tr-full rounded-tl-full">            
                <!-- post area -->     
                <div class="p-4 text-lg border-b border-gray-400  rounded-tr-full rounded-tl-full"
                        v-if="post.id">

                    <FeedItem v-bind:post="post" />             
                </div>

                
                <!-- comment area -->
                <div 
                    class="py-4 pl-8 pr-4 border-b border-gray-400 "
                    v-for="comment in post.comments"
                    v-bind:key="comment.id"
                >
                    <CommentItem v-bind:comment="comment"/>
                </div>   
            </div>
            <!-- write something comment -->
             
                <form v-on:submit.prevent="submitForm"
                    method="post">
                        <div class="flex items-center px-3 py-2 rounded-br-full rounded-bl-full dark:bg-purple_main">
                            <textarea v-model="body" rows="2" class="bg-purple_main block mr-2 p-2.5 w-full rounded-br-full rounded-bl-full" placeholder="say something about this post.."></textarea>
                                <button type="submit" class="inline-flex justify-center p-3 rounded-img cursor-pointer hover:bg-[#28183e]">
                                <svg class="w-6 h-6 rotate-90" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="white" viewBox="0 0 18 20">
                                    <path d="m17.914 18.594-8-18a1 1 0 0 0-1.828 0l-8 18a1 1 0 0 0 1.157 1.376L8 18.281V9a1 1 0 0 1 2 0v9.281l6.758 1.689a1 1 0 0 0 1.156-1.376Z"/>
                                </svg>
                                </button>
                        </div>
                </form>

            
        </div>
        
        <!-- right side -->
        <div class="main-right col-span-1  space-y-6">
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
import CommentItem from '../components/CommentItem.vue'

export default {
    name: 'PostView',


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
        CommentItem,
    },
    data(){
        return {
            post:{
                id: null,
                comments: []
            },
            body: ''
        }
    },
    mounted(){
        this.getPost()
    },

    methods: 
    {
        getPost()
        {
            axios
                .get(`/api/posts/${this.$route.params.id}/`)
                .then(response => {
                    console.log('data', response.data)

                    this.post = response.data.post
                })
                .catch(error => {
                    console.log('error', error)
                })
        },  
        submitForm()
        {
            console.log('submitForm', this.body) //textarea v-model="body" 

            axios //sending to backend
                .post(`/api/posts/${this.$route.params.id}/comment/`, 
                {
                    'body': this.body
                })
                .then(response =>{
                    console.log('data', response.data)

                    this.post.comments.push(response.data)
                    this.post.comments_count += 1
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