<template>
    <!-- top part ng post-->
    <div class="mb-4 flex items-center justify-between">
        <!-- username nd pfp -->
            <div class="flex items-center space-x-4">
                <img src="https://i.pravatar.cc/300?img=70" class="w-[45px] rounded-img">
                    <p class="font-medium">
                        <RouterLink :to="{name: 'profile', params:{'id': comment.created_by.id}}">{{ comment.created_by.name }}</RouterLink>
                    </p>
            </div>
                    <!-- time posted -->
                    <p class="text-gray-400 text-xs font-light">{{ comment.created_at_formatted}}</p> 
    </div>

                    <p class="text-base/7 font-light">{{ comment.body }}</p>

                    <!-- if may image <img src="https://images.unsplash.com/photo-1661956602868-6ae368943878?ixlib=rb-4.0.3&amp;ixid=MnwxMjA3fDF8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&amp;auto=format&amp;fit=crop&amp;w=2670&amp;q=80" class="w-full rounded-full"> --> 


</template>

<script>
import { RouterLink } from 'vue-router'

export default{
    props: {
        comment: Object
    },
    components: { RouterLink }
}
</script>