<template>
    <div class="max-w-7xl mx-auto grid grid-cols-2 gap-4">
        <!-- left part -->
        <div class="main-left self-center ">    
               

                <RouterLink to ="/profile/edit/password" class="underline text-lg">
                    Edit password
                </RouterLink> <br>
                <RouterLink to ="/popup" class="underline text-lg">
                    Edit category & Game Titles
                </RouterLink>


        </div>
        <!-- right part -->
        <div class="main-right py-28 justify-self-end">
            <h1 class="mb-14 font-bold tracking-wide text-6xl">
                Edit<br>Profile
            </h1>
            <form class="space-y-6 w-96" v-on:submit.prevent="submitForm">
                <div>
                    <!-- username -->
                    <input type="text" v-model="form.name" placeholder="enter your username" class="bg-transparent w-full py-3 px-6 border border-purple1 rounded-full">
                </div>
                <div>
                    <!-- email -->
                    <input type="email" v-model="form.email" placeholder="enter your email" class="bg-transparent w-full py-3 px-6 border font-white border-violet1 rounded-full">
                </div>

                <div>
                    <!-- bio -->
                    <input type="text" v-model="form.bio" placeholder="enter something about yourself" class="bg-transparent w-full py-3 px-6 border font-white border-violet1 rounded-full">
                </div>

                <div>
                    <!-- avatar -->
                    <label class="float-left active:bg-violet1 inline-block text-center w-36 p-2 bg-purple_main text-white rounded-full">
                        <input type="file" ref="file" @change="onFileChange">
                        Upload Image
                    </label>
                </div>

                <template v-if="errors.length > 0">
                    <div class="bg-red-400 text-white rounded-lg p-6">
                        <p v-for="error in errors" v-bind:key="error">{{ error }}
                        </p>                        
                    </div>
                </template>

                <div class="space-y-2">
                    <button class="active:bg-purple_main tracking-wider bg-[#8250CB] w-full mt-8 py-3 px-6 text-white rounded-full font-semibold">save changes</button>
                    
                </div>
            </form>
        </div>
        <br>
        <br>
    </div>

</template>

<script>
import axios from 'axios'

import { useToastStore } from '@/stores/toast'
import { useUserStore } from '@/stores/user'

export default {
    setup() {
        const toastStore = useToastStore()
        const userStore = useUserStore()

        return {
            toastStore,
            userStore
        }
    },

    data() {
        return {
            form: {
                name: this.userStore.user.name,
                email: this.userStore.user.email, 
                bio: this.userStore.user.bio,         
            },
            errors: [],
        }
    },

    methods: {
        submitForm() {
            this.errors = []

            //validation of data


            if (this.form.name === ''){
                this.errors.push('your name is missing')
            }

            if (this.form.email === ''){
                this.errors.push('your email is missing')
            }
            if (this.errors.length === 0) {
                let formData = new FormData() //avatar
                formData.append('avatar', this.$refs.file.files[0])
                formData.append('name', this.form.name)
                formData.append('email', this.form.email)
                formData.append('bio', this.form.bio)

                axios
                    .post('/api/editprofile/', formData, {
                        headers: { // to let the backend know that there other content types or info
                            "Content-Type": "multipart/form-data",
                        }
                    })
                    .then(response => {
                        if (response.data.message === 'information updated') {
                            this.toastStore.showToast(5000, 'Profile Information Updated!','bg-emerald-500')
                            
                            //update the user store in the browser 
                            this.userStore.setUserInfo({
                                id: this.userStore.user.id,
                                name: this.form.name,
                                email: this.form.email,
                                bio: this.form.bio,
                                avatar: response.data.user.get_avatar
                            })
                            
                            //to go back to profile page after edit profile info
                            this.$router.back()
                        } else {
                            this.toastStore.showToast(5000, `${response.data.message}. Please try again`, 'bg-red-300')
                        }
                    })
                    .catch(error => {
                        console.log('error', error)
                    })
            }

        }
    }

}
</script>