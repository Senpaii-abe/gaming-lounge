<template>
    <div class="max-w-screen px-12 mx-auto grid grid-cols-4 gap-4">

        <!-- left side 
             col-span-1: takes 1 of the 4 columns -->
        <div class="main-left col-span-1 space-y-6"> 
            <!-- profile -->
            <div class="p-4 bg-purple_main rounded-full">
                <!-- profile picture -->
                <div class="flex items-center space-x-4">
                    <img :src="user.get_avatar" class="h-[80px] w-[80px] rounded-img"> 
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
                        <p class="text-lg/none">{{ user.charisma_score }}</p>
                        <label class="text-sm">charisma</label>
                    </div>
                
                </div>
                <!-- about me -->
                <p class="px-1 text-sm/5 font-light text-justify">{{ user.bio }}</p>
                
                <!-- send friend request button -->
                <div class = "mt-6">
                    <button 
                        class = "inline-block py-3 hover:bg-purple-600 bg-[#28183e] font-semibold rounded-full w-full" 
                        @click="sendFriendshipRequest"
                        v-if="userStore.user.id !== user.id && can_send_friendship_request"
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
                        class = "inline-block py-3 my-4 text-center hover:bg-purple-600 bg-[#28183e] font-semibold rounded-full w-full" 
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
                <FeedForm v-bind:user="user" v-bind:posts="posts"/>
            </div>
            <!-- post -->     
            <div class="p-5 bg-purple_main rounded-full border-2 border-gray-400"
                    v-for="post in posts" 
                    v-bind:key="post.id"> <!-- loop ng post -->

                    <FeedItem :post="post" @postDeleted="handlePostDeleted" />
            </div>
        </div>
        
        <!-- right side -->
        <div class="main-right col-span-1 space-y-6">
            
         

            <PeopleYouMayKnow />
    


        </div>
    </div>
</template> 

<style>
input[type="file"] {
    display: none;
}
.custom-file-upload {
    border: 1px solid #ccc;
    display: inline-block;
    padding: 6px 12px;
    cursor: pointer;
}
</style>

<script>
import axios from 'axios'
import PeopleYouMayKnow from '../components/PeopleYouMayKnow.vue'

import FeedForm from '../components/FeedForm.vue'
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

        FeedItem,
        FeedForm
    },
    data(){
        return {
            posts:[],
            user: {
                id: ''
            },
            can_send_friendship_request: null,
        }
    }, 
    mounted() {
        this.getFeed();
        this.getUserPostCount(); // Fetch and update user's post count
        this.getCharismaScore();
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
        deletePost(id) {
            // Filter out the deleted post
            this.posts = this.posts.filter(post => post.id !== id);
        },

        handlePostDeleted(deletedPostId) {
            this.posts = this.posts.filter(post => post.id !== deletedPostId);
            // Decrement the user's posts count
            if (this.user) {
                this.user.posts_count -= 1;
            }
        },

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

                    this.can_send_friendship_request = false

                    if (response.data.message == 'request already sent')
                    {
                        this.toastStore.showToast(5000, 'The request has already been sent', 'bg-red-400')
                    }
                    else{
                        this.toastStore.showToast(5000, 'The request was sent!', 'bg-emerald-500')
                         // Update friends count if the request was successful
                        if (response.data.request_accepted) {
                             // Update friends count if the request was accepted
                            this.user.friends_count += 1; // Increment friends count here
                        }
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
                    this.can_send_friendship_request = response.data.can_send_friendship_request

                })
                .catch(error => {
                    console.log('error', error)
                })
        },
        getUserPostCount() {
            axios
                .get(`/api/posts/profile/${this.$route.params.id}/post_count/`)
                .then((response) => {
                // Update the user's post count in the component state
                this.user.posts_count = response.data.posts_count;
                })
                .catch((error) => {
                console.error('Error fetching user post count', error);
                });
        },
        getCharismaScore() {
            axios
                .get(`/api/posts/profile/${this.$route.params.id}/charisma_score/`)
                .then((response) => {
            
                // Update the user's post count in the component state
                this.user.charisma_score = response.data.charisma_score_count;
                })
                .catch((error) => {
                console.error('Error fetching user charisma score', error);
                });
        },
        logout() {
            console.log('Log out')
            this.userStore.removeToken()

            this.$router.push('/')
        }
    }
}
</script>