<template>
    <form 
        v-on:submit.prevent="submitForm"
            method="post">
            <textarea v-model="body" class="p-4 w-full bg-purple_main rounded-full" placeholder="let's talk gaming.."></textarea>

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
export default{
    props: {
        user: Object,
        posts: Array
    },
    data() {
        return{
            body: '',
            is_private: false,
            url: null,
        }
    },

    methods: {
        submitForm(){
            console.log('submitForm', this.body) //textarea v-model="body"
            let formData = new FormData() //image attachments
            formData.append('image', this.$refs.file.files[0])
            formData.append('body', this.body)
            formData.append('is_private', this.is_private)

            axios //sending to backend
                .post('/api/posts/create/', formData, {
                    headers: 
                    { 
                        "Content-Type": "multipart/form-data",
                    }
                })
                .then(response =>{
                    console.log('data', response.data)

                    this.posts.unshift(response.data)
                    this.body = ''
                    this.is_private = false
                    this.$refs.file.value = null
                    this.url = null
                    if (this.user){
                        this.user.posts_count += 1 //add post count automatically in frontend
                    }
                })
                .catch(error =>{
                    console.log('error', error)
                })
        },
    }
}
</script>