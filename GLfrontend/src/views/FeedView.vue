<template>

    <div data-te-infinite-scroll-init class="max-w-screen mx-auto grid grid-cols-4 gap-4 px-12" id="spinners-and-async-example">

        <!-- left side 
             col-span-1: takes 1 of the 4 columns -->
            <div class="main-left col-span-1 space-y-6 sticky top-[8rem] h-screen overflow-auto">
            <!-- trending games -->
            <!-- <div class="bg-transparent rounded-full">
                <h3 class="mb-2 text-2xl font-semibold text-center">topics</h3>
                <div class="space-y-4 text-center">
                    <div class="flex items-center justify-between">
                        <a href="#"
                            class="py-2 px-3 text-lg rounded-large w-full border border-gray hover:bg-purple_main">Valorant</a>
                    </div>
                    <div class="flex items-center justify-between ">
                        <a href="#"
                            class="w-full border border-gray hover:bg-purple_main py-2 px-3 text-lg rounded-large">Farlight
                            84</a>
                    </div>
                    <div class="flex items-center justify-between ">
                        <a href="#"
                            class="w-full border border-gray py-2 px-3 text-lg rounded-large hover:bg-purple_main ">League
                            of Legends</a>
                    </div>
                    <div class="flex items-center justify-between ">
                        <a href="#"
                            class="w-full border border-gray py-2 px-3 text-lg rounded-large hover:bg-purple_main ">Action</a>
                    </div>
                    <div class="flex items-center justify-between ">
                        <a href="#"
                            class="w-full border border-gray py-2 px-3 text-lg rounded-large hover:bg-purple_main ">Phasmaphobia</a>
                    </div>
                </div>
            </div> -->
            <div class="p-4 bg-purple_main rounded-full">
                <h3 class="mb-6 font-semibold tracking-wide">useful links</h3>

                <p class="text-base/7 italic mb-6">our instance rules are here and cover the ideals and how we want this
                    community to evolve.</p>
                <p class="text-base/7 italic mb-2">where you can download games:</p>

                <ul class="list-inside">

                    <li class="p-1 hover:underline">
                        <a href="https://www.riotgames.com/en" target="_blank" rel="noopener noreferrer"><img
                                src="/assets/img/logo/riot_logo.png" class="h-auto max-w-full" alt="logo" />riot games</a>
                    </li>

                    <li class="p-1 hover:underline">
                        <a href="https://store.steampowered.com/" target="_blank" rel="noopener noreferrer"><img
                                src="/assets/img/logo/steam_logo.png" class="h-auto max-w-full" alt="logo" />steam</a>
                    </li>

                    <li class="p-1 hover:underline">
                        <a href="https://store.epicgames.com/en-US/" target="_blank" rel="noopener noreferrer"><img
                                src="/assets/img/logo/epic_logo.png" class="h-auto max-w-full" alt="logo" />epic games</a>
                    </li>

                    <li class="p-1 hover:underline">
                        <a href="https://us.shop.battle.net/en-us" target="_blank" rel="noopener noreferrer"><img
                                src="/assets/img/logo/battle_logo.png" class="h-auto max-w-full" alt="logo" />battle.net</a>
                    </li>

                </ul>
            </div>
        </div>

        <!-- center -->
        <!-- col-span-2: takes 2 of the 4 columns
                 space-y-4: 6 spaces each post -->
        <div class="px-4 main-center col-span-2 space-y-6"> <!--whole feed-->
            <div class="feed"> <!--modal design-->
                    <Modal @close="toggleModal" :modalActive="modalActive">
                        <div class="rounded-full bg-transparent space-y-1 text-right model-content">
                           
                            <FeedForm v-bind:user="null" v-bind:posts="posts"/>
                        </div>
                    </Modal>
                <div class="flex items-center justify-between rounded-full space-x-2 py-4">
                    <img :src="userStore.user.avatar" alt="user.profile" class="w-14 h-14 rounded-img">
                    <button @click="toggleModal" class="py-4 px-3 w-full bg-[#0A001266] bg-opacity-30 rounded-img text-left transition-colors duration-150 focus:shadow-outline hover:bg-purple-900 hover:bg-opacity-30"> 
                        <span class="text-gray-400 pl-2 italic">lets talk gaming?</span>
                    </button>
                </div>

            </div>
       
            <!-- write something -->
            <!-- bg-gradient-to-r from-violet-900  -->
            <!-- post area -->
                <div class="p-5 bg-purple_main rounded-full border-2 border-gray-400"  v-for="post in posts" v-bind:key="post.id">
                
                <!-- loop ng post -->

                <FeedItem :post="post" @postDeleted="handlePostDeleted"/>
            </div>
        </div>

        <!-- right side -->
        <div class="main-right col-span-1 space-y-6 sticky top-[8rem] h-screen overflow-auto">
            <PeopleYouMayKnow />
        </div>
        <div
            id="spinner"
            class="hidden h-8 w-8 animate-spin rounded-full border-4 border-solid border-current border-r-transparent align-[-0.125em] motion-reduce:animate-[spin_1.5s_linear_infinite]"
            role="status">
            <span
            class="!absolute !-m-px !h-px !w-px !overflow-hidden !whitespace-nowrap !border-0 !p-0 ![clip:rect(0,0,0,0)]"
            >Loading...</span
            >
  </div>

    </div>
</template> 


<script>


import axios from 'axios'
import FeedForm from '../components/FeedForm.vue'
import FeedItem from '../components/FeedItem.vue'
import PeopleYouMayKnow from '../components/PeopleYouMayKnow.vue'
import { useUserStore } from '@/stores/user'

import Modal from '@/components/Modal.vue';
import {ref} from 'vue'
export default {
    name: 'FeedView',

    emits: ['postDeleted'],

    setup() {
        const userStore = useUserStore()

        const modalActive = ref(false)
        const toggleModal = () => {
            modalActive.value = !modalActive.value;
        }


      
        return {
            userStore,
            modalActive,
            toggleModal,
        }
        
    },
        components: {
            PeopleYouMayKnow,
            Modal,
            FeedItem,
            FeedForm,
        },
        
    data() {
    
        return {
            posts: [],
            body: '',
          
            currentPage: 1,
            totalPages: null,

        }
    },
    mounted() {
        this.getFeed()
        this.userStore.initStore();

        window.onscroll = () => {
            if(this.currentPage < this.totalPages) {
            let bottomOfWindow = document.documentElement.scrollTop + window.innerHeight === document.documentElement.offsetHeight
            if (bottomOfWindow) { 
                this.currentPage += 1
                this.getFeed()
            }
            }
        }
        }, 
    methods:
    {
        getFeed() {
            axios
                .get(`/api/posts/?page=${this.currentPage}`)
                // .get('/api/posts')
                .then(response => {
                    this.posts = this.posts.concat(response.data) 
                    this.currentPage = response.data.currentPage
                    this.totalPages = response.data.totalPages

                    this.hasNext=false

                    if(response.data.next){
                        this.hasNext = true
                    }
                    
                    console.log(response.data)
                })
  
                .catch(error => {
                    console.log('error', error)
                })
        },

        handlePostDeleted(deletedPostId) {
            this.posts = this.posts.filter(post => post.id !== deletedPostId);
            // Decrement the user's posts count
            if (this.user) {
                this.user.posts_count -= 1;
            }
        },

        search() {
            // Redirect to the search page with the query as a URL parameter
            this.$router.push({ name: 'search', query: { q: this.searchQuery } });
        },
    }
}
</script>

<style lang="scss" scoped>

</style>