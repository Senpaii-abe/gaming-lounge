<template>
        <div class="max-w-7xl mx-auto grid grid-cols-2 gap-4">
            <!-- left part -->
            <div class="main-left self-center ">    
                    <h1 class="mb-6 tracking-wide leading-tight font-black text-6xl">
                        DISCOVER YOUR<br>GAMING QUEST.
                    </h1>
                    <p class="mb-6 text-lg font-light w-4/5">
                        Look no further - Gaming Lounge is the ultimate one-stop<br> hub for gaming fans. Connect and quest alongside casual and competitive gamers.
                    </p>
                    <p class="font-medium text-xl">
                    already have an account? <RouterLink to="/Login" class="font-semibold active:text-blue_link underline">click here </RouterLink> to login!
                    </p>
            </div>
            <!-- right part -->
            <div class="main-right py-28 justify-self-end">
                <h1 class="mb-14 font-bold tracking-wide text-6xl">
                    Welcome<br>Gamer!
                </h1>
                <form class="space-y-6 w-96" v-on:submit.prevent="submitForm">
                    <div>
                        <!-- username -->
                        <input type="text" v-model="form.name" placeholder="enter your username" class="bg-transparent w-full py-3 px-6 border border-purple1 rounded-full">
                    </div>
                    <div>
                        <!-- email -->
                        <input type="email" v-model="form.email" placeholder="enter your email" class="bg-transparent w-full py-3 px-6 border border-violet1 rounded-full">
                    </div>
                    <div>
                        <!-- password -->
                        <input type="password" v-model="form.password1" placeholder="enter your password" class="bg-transparent w-full py-3 px-6 border border-purple1 rounded-full">
                    </div>
                    <div>
                        <!-- confirm password -->
                        <input type="password" v-model="form.password2" placeholder="confirm password" class="bg-transparent w-full py-3 px-6 border border-violet1 rounded-full">
                    </div>

                    <template v-if="errors.length > 0">
                        <div class="bg-red-300 text-white rounded-lg p-6">
                            <p v-for="error in errors" v-bind:key="error">{{ error }}</p>                        </div>
                    </template>

                    <div class="space-y-2">
                        <button class="active:bg-purple_main tracking-wider bg-[#8250CB] w-full mt-8 py-3 px-6 text-white rounded-full font-semibold">register</button>

                        <p class="text-center text-[0.86rem] font-light">by clicking register, you agree to the gaming lounges' 
                            <a class="text-blue_link underline active:text-[#0085FF]" href="#">terms of service</a> and 
                            <a class="text-blue_link underline active:text-[#0085FF]" href="#">privacy policy</a>
                        </p>
                    </div>
                </form>
            </div>

        </div>

</template>

<script>
import axios from 'axios'

import { useToastStore } from '@/stores/toast'

export default {
    setup() {
        const toastStore = useToastStore()

        return {
            toastStore
        }
    },

    data() {
        return {
            form: {
                email: '',
                name: '',
                password1: '',
                password2: '',
            },
            errors: [],
        }
    },

    methods: {
        submitForm() {
            this.errors = []

            //validation of data

            if (this.form.email === ''){
                this.errors.push('Your email is missing')
            }

            if (this.form.name === ''){
                this.errors.push('Your name is missing')
            }

            if (this.form.password1 === ''){
                this.errors.push('Your password is missing')
            }

            if (this.form.password1 !== this.form.password2){
                this.errors.push('Your password does not match')
            }

            if (this.errors.length === 0){
                axios
                    .post('/api/signup/', this.form)
                    .then(response => {
                        if (response.data.message === 'success') {
                            this.toastStore.showToast(5000, 'The user is registered. Please log in ', 'bg-emerald-500')
    
                            this.form.email = ''
                            this.form.name = ''
                            this.form.password1 = ''
                            this.form.password2 = ''

                        } else {
                            this.toastStore.showToast(5000, 'Something went wrong. Please try again','bg-red-300')
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