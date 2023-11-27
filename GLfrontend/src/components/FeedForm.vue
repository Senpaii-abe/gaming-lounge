<template>
    <form 
        v-on:submit.prevent="submitForm"
            method="post">
            <div class="space-x-2">
              <!-- <select v-model="menu" class="mb-2 p-2 bg-purple_main rounded-full text-white float-left">
                <option value="" disabled>where to post</option>
                <option v-for="choice in menuChoices">{{ choice }}</option>
              </select> -->
              
                <select v-model="game_title" class="mb-2 p-2 w-full bg-purple_main rounded-full text-align">
                  <option value="" disabled>pick your game topic</option>
                  <option v-for="title in gameTitles" :key="title.id" :value="title.id">{{ title.title }}</option>
              </select>

              
            </div>
            
            <textarea v-model="body" class="p-4 w-full bg-purple_main rounded-full" placeholder="let's talk gaming.."></textarea>
            <div v-if="gameTitleError" class="text-red-500 mb-2">
              <p>select a game before posting</p>
            </div>

            
           

            <div v-if="contentError" class="text-red-500 mb-2">
              <p>Please provide a description about your post.</p>
            </div>
            <label>
                <input type="checkbox" v-model="is_private"> friends only
            </label>

            <div id="preview" v-if="url">
                <img :src="url" class="w-[80px] rounded-xl" />
            </div>

        <div class="py-2 border-t border-black justify-between">
                <label class="float-left active:bg-violet1 inline-block text-center w-36 p-2 bg-purple_main text-white rounded-full">
                    <input type="file" ref="file" @change="onFileChange">
                    Attach Image
                </label>
            <button class="active:bg-violet1 inline-block text-center w-24 p-2 bg-purple_main text-white rounded-full">post</button>
        </div>       
    </form>
</template>

<script>
import axios from 'axios'
// profcheck
import { useToastStore } from '@/stores/toast'


export default {
  setup() { //profcheck
        const toastStore = useToastStore()
        return {
            toastStore
        }
    },
  props: {
    user: Object,
    posts: Array
  },
  data() {
    return {
      body: '',
      is_private: false,
      url: null,
      game_title: '',
      gameTitles: [],
      
      menuChoices: ['Discussions', 'Marketplace', 'Connect', 'Tournament', 'Beta Testing'],
      menu: '',
      gameTitleError: false, // Added error flag for game title validation
      contentError: false, // New error flag for post content
      error: null, //profcheck
    }
  },

  mounted() {
    this.fetchGameTitles();
  },

  methods: {
    submitForm() {
      console.log('submitForm', this.body);
      this.gameTitleError = false;
      this.contentError = false;

      // Check if game title is selected
      if (!this.game_title) {
        this.gameTitleError = true;
      }

      // Check if body/content is provided
      if (!this.body.trim()) {
        this.contentError = true;
      }

      // Prevent form submission if either check fails
      if (this.gameTitleError || this.contentError) {
        return;
      }
      let formData = new FormData();
      formData.append('image', this.$refs.file.files[0]);
      formData.append('body', this.body);
      formData.append('is_private', this.is_private);
      formData.append('game_title', this.game_title);
      formData.append('menu', this.menu);

      axios
        .post('/api/posts/create/', formData, {
          headers: {
            "Content-Type": "multipart/form-data",
          }
      })
        .then(response => {
        
        this.toastStore.showToast(5000, 'walang mura ˚ʚ♡ɞ˚ ', 'bg-emerald-600') //profcheck

        this.posts.unshift(response.data);
        this.resetForm();
        if (this.user) {
          this.user.posts_count += 1;
        }
      })
        .catch(error =>{//profcheck
          if (error.response.status === 400) {//profcheck
          const message = error.response.data.error//profcheck

          this.toastStore.showToast(//profcheck
            5000,  //profcheck
            'may mura!!!',//profcheck
            'bg-red-400' //profcheck
          )//profcheck
        }//profcheck
    });
    },
    resetForm() {
            this.body = '';
            this.is_private = false;
            this.$refs.file.value = null;
            this.url = null;
            this.game_title = ''; // Reset to null instead of empty string
            this.menu = '';
        },
        async fetchGameTitles() {
            try {
                const response = await axios.get(`/api/posts/get_gametitle/`);
                this.gameTitles = response.data;
                console.log('Game Titles:', this.gameTitles);
            } catch (error) {
                console.error('Error fetching game titles:', error);
            }
          },
  }
}
</script>