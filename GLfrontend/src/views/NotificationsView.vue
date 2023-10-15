<template>
<div class="max-w-7xl mx-auto grid grid-cols-4 gap-4">

        <!-- left side 
        col-span-1: takes 1 of the 4 columns -->
        <div class="main-left col-span-1 space-y-6"> 

        </div>
        <div class="p-4 bg-purple_main rounded-full">
            
        </div> 

    <!-- center -->
        <!-- col-span-2: takes 2 of the 4 columns
            space-y-4: 6 spaces each post -->
    <div class="px-4 main-center col-span-2 space-y-6">
        <!-- write something -->
        <!-- post area -->     
        <div class="p-4 bg-purple_main rounded-full"
                v-for="notification in notifications" 
                v-bind:key="notification.id"> <!-- loop ng post -->
                {{ notification.body }}
        </div>
    
    </div>

</div> 

</template>

<script>
import axios from 'axios'

export default{
    name: 'notifications', 

    data(){
        return {
            notifications: []
        }
    },

    mounted(){
        this.getNotifications()
    },
    methods: {
        getNotifications() 
        {
            axios
                .get('api/notifications/')
                .then(response => {
                    console.log(response.data)
                    this.notifications = response.data
                })
                .catch(error => {
                    console.log('Error: ', error)
                })
        }
    },
}
</script>