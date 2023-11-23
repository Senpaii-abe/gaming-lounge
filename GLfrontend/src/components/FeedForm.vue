<template>
    <form 
        v-on:submit.prevent="submitForm"
            method="post">
            <select v-model="game_title" class="mb-2 float-left px-2 w-55 bg-purple_main rounded-full">
                <option value="" disabled>Select a game title...</option>
                <option v-for="title in gameTitles" :key="title.id" :value="title.id">{{ title.title }}</option>
            </select>
            <textarea v-model="body" class="p-4 w-full bg-purple_main rounded-full" placeholder="let's talk gaming.."></textarea>
            <div v-if="gameTitleError" class="text-red-500 mb-2">
              <p>Please select a game title before posting.</p>
            </div>
            <div v-if="contentError" class="text-red-500 mb-2">
              <p>Please provide a description about your post.</p>
            </div>
            <label>
                <input type="checkbox" v-model="is_private"> Private
            </label>

            <div id="preview" v-if="url">
                <img :src="url" class="w-[80px] rounded-xl" />
            </div>

        <div class="p-2 border-t border-black justify-between">
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


export default {
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
      gameTitleError: false, // Added error flag for game title validation
      contentError: false, // New error flag for post content
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

      axios.post('/api/posts/create/', formData, {
        headers: {
          "Content-Type": "multipart/form-data",
        }
      })
      .then(response => {
        console.log('data', response.data);
        this.posts.unshift(response.data);
        this.resetForm();
        if (this.user) {
          this.user.posts_count += 1;
        }
      })
      .catch(error => {
        console.log('error', error);
      });
    },
    resetForm() {
            this.body = '';
            this.is_private = false;
            this.$refs.file.value = null;
            this.url = null;
            this.game_title = null; // Reset to null instead of empty string
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