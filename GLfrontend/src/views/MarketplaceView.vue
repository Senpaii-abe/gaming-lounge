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
    <div class="max-w-screen mx-auto grid grid-cols-4 gap-4 px-12">
            
        <LeftPanel />
       
        <!-- center -->
        <!-- col-span-2: takes 2 of the 4 columns
                 space-y-4: 6 spaces each post -->
        <div class="px-4 main-center col-span-2 space-y-6">
            <!-- post area -->
            <div class="p-5 bg-purple_main rounded-full border-2 border-gray-400" v-for="post in posts" v-bind:key="post.id"> <!-- loop ng post -->
                <FeedItem :post="post" @postDeleted="handlePostDeleted" />
            </div>
        </div>

        <!-- right side -->
        <div class="main-right col-span-1 space-y-6 sticky top-[8rem] h-screen overflow-auto">


     
            <PeopleYouMayKnow />

        </div>


    </div>
</template> 


<script>
import axios from 'axios'
import PeopleYouMayKnow from '../components/PeopleYouMayKnow.vue'
import { useUserStore } from '@/stores/user'
import FeedItem from '../components/FeedItem.vue'
import LeftPanel from '@/components/LeftPanel.vue'
export default {
    name: 'MarketplaceView',

    emits: ['postDeleted'],

    setup() {
        const userStore = useUserStore()

        return {
            userStore
        }
    },
    components: {
        PeopleYouMayKnow,
        LeftPanel,
        FeedItem,
    },
    data() {
        return {
            posts: [],
            body: '',
        }
    },
    mounted() {
        this.getFeed()
    },
    methods:
    {
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
        getFeed() {
            axios
                .get('/api/posts/marketplace_posts/')
                .then(response => {
                    console.log('data', response.data)
                    this.posts = response.data
                })
                .catch(error => {
                    console.log('error', error)
                })
        },
        search() {
            // Redirect to the search page with the query as a URL parameter
            this.$router.push({ name: 'search', query: { q: this.searchQuery } });
        },
    }
}
</script>