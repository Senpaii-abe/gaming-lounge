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
    <div class="max-w-7xl mx-auto grid grid-cols-4 gap-4">
        <!-- left side 
             col-span-1: takes 1 of the 4 columns -->
        <div class="main-left col-span-1"> 
            <div class="p-4 bg-purple_main rounded-full">
                <!-- profile picture -->
                <div class="flex items-center space-x-4">
                    <img src="https://i.pravatar.cc/300?img=70" class="w-[80px] rounded-img">
                    <p class="font-medium text-lg">Code With Stein</p>
                </div>
                <!-- charisma points nd posts-->
                <div class="my-5 px-12 py-4 flex flex-row justify-between items-center bg-dark_purple rounded-full text-center">
                    <div>
                        <p class="text-lg/none">182</p>
                        <label class="text-sm">posts</label>
                    </div>
                     <div class="font-semibold" >
                        <p class="text-lg/none">120</p>
                        <label class="text-sm">charisma</label>
                    </div>
                </div>
                <!-- about me -->
                <p class="px-1 text-sm/7 font-extralight">tungkol sakin</p>

            </div>  
        </div> 
        <!-- center -->
            <!-- col-span-2: takes 2 of the 4 columns
                 space-y-4: 4 spaces each post -->
        <div class="px-4 main-center col-span-2 space-y-6">
            <!-- write something -->
            <div class="rounded-full bg-transparent space-y-1 text-right">
                <textarea class="p-4 w-full bg-purple_main rounded-full" placeholder="let's talk gaming.."></textarea>
                <a href="#" class="active:bg-violet1 inline-block text-center w-24 p-2 bg-purple_main text-white rounded-full">post</a>
            </div>
            <!-- post -->
            <div class="p-4 bg-purple_main rounded-full">
                <!-- top part ng post-->
                <div class="mb-4 flex items-center justify-between">
                    <!-- username nd pfp -->
                    <div class="flex items-center space-x-4">
                        <img src="https://i.pravatar.cc/300?img=70" class="w-[40px] rounded-img">
                        <p class="font-medium">BBM_SUPOT23</p>
                    </div>
                    <!-- time posted -->
                    <p class="text-gray-400 text-xs font-light">18 minutes ago</p> 
                </div>
                <!-- mid part - posted image/text -->
                    <!-- <img src="https://images.unsplash.com/photo-1661956602868-6ae368943878?ixlib=rb-4.0.3&amp;ixid=MnwxMjA3fDF8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&amp;auto=format&amp;fit=crop&amp;w=2670&amp;q=80" class="w-full rounded-full"> -->

                    <p class="text-base/7 font-light">THIS PAGE IS UNDER CONSTRUCTION!!!!!</p>
                <!-- lower part ng post -->
                <div class="mt-6 flex justify-between">
                    <div class="flex space-x-6">
                        <!-- likes -->
                        <div class="flex items-center space-x-2">
                            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
                                <path stroke-linecap="round" stroke-linejoin="round" d="M21 8.25c0-2.485-2.099-4.5-4.688-4.5-1.935 0-3.597 1.126-4.312 2.733-.715-1.607-2.377-2.733-4.313-2.733C5.1 3.75 3 5.765 3 8.25c0 7.22 9 12 9 12s9-4.78 9-12z"></path>
                            </svg>  
                            
                            <span class="text-gray-300 text-xs">82 likes</span>
                        </div>
                        <!-- comments -->
                        <div class="flex items-center space-x-2">
                            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
                                <path stroke-linecap="round" stroke-linejoin="round" d="M12 20.25c4.97 0 9-3.694 9-8.25s-4.03-8.25-9-8.25S3 7.444 3 12c0 2.104.859 4.023 2.273 5.48.432.447.74 1.04.586 1.641a4.483 4.483 0 01-.923 1.785A5.969 5.969 0 006 21c1.282 0 2.47-.402 3.445-1.087.81.22 1.668.337 2.555.337z"></path>
                            </svg> 

                            <span class="text-gray-300 text-xs ">0 comments</span>
                        </div>
                    </div>
                    <div> 
                        <!-- three dots -->
                        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
                            <path stroke-linecap="round" stroke-linejoin="round" d="M12 6.75a.75.75 0 110-1.5.75.75 0 010 1.5zM12 12.75a.75.75 0 110-1.5.75.75 0 010 1.5zM12 18.75a.75.75 0 110-1.5.75.75 0 010 1.5z"></path>
                        </svg>   
                    </div>   
                </div>  
            </div>
            <!-- post 1 -->
            <div class="p-4 bg-purple_main rounded-full">
                <!-- top part ng post-->
                <div class="mb-4 flex items-center justify-between">
                    <!-- username nd pfp -->
                    <div class="flex items-center space-x-4">
                        <img src="https://i.pravatar.cc/300?img=70" class="w-[40px] rounded-img">
                        <p class="font-medium">Code With Stein</p>
                    </div>
                    <!-- time posted -->
                    <p class="text-gray-400 text-xs font-light">18 minutes ago</p> 
                </div>
                <!-- mid part - posted image/text -->

                    <img src="https://images.unsplash.com/photo-1661956602868-6ae368943878?ixlib=rb-4.0.3&amp;ixid=MnwxMjA3fDF8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&amp;auto=format&amp;fit=crop&amp;w=2670&amp;q=80" class="w-full rounded-full">

                <!-- lower part ng post -->
                <div class="mt-6 flex justify-between">
                    <div class="flex space-x-6">
                        <!-- likes -->
                        <div class="flex items-center space-x-2">
                            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
                                <path stroke-linecap="round" stroke-linejoin="round" d="M21 8.25c0-2.485-2.099-4.5-4.688-4.5-1.935 0-3.597 1.126-4.312 2.733-.715-1.607-2.377-2.733-4.313-2.733C5.1 3.75 3 5.765 3 8.25c0 7.22 9 12 9 12s9-4.78 9-12z"></path>
                            </svg>  
                            
                            <span class="text-gray-300 text-xs">82 likes</span>
                        </div>
                        <!-- comments -->
                        <div class="flex items-center space-x-2">
                            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
                                <path stroke-linecap="round" stroke-linejoin="round" d="M12 20.25c4.97 0 9-3.694 9-8.25s-4.03-8.25-9-8.25S3 7.444 3 12c0 2.104.859 4.023 2.273 5.48.432.447.74 1.04.586 1.641a4.483 4.483 0 01-.923 1.785A5.969 5.969 0 006 21c1.282 0 2.47-.402 3.445-1.087.81.22 1.668.337 2.555.337z"></path>
                            </svg> 

                            <span class="text-gray-300 text-xs ">0 comments</span>
                        </div>
                    </div>
                    <div> 
                        <!-- three dots -->
                        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
                            <path stroke-linecap="round" stroke-linejoin="round" d="M12 6.75a.75.75 0 110-1.5.75.75 0 010 1.5zM12 12.75a.75.75 0 110-1.5.75.75 0 010 1.5zM12 18.75a.75.75 0 110-1.5.75.75 0 010 1.5z"></path>
                        </svg>   
                    </div>   
                </div>  
            </div>
            <!-- post 2 -->
            <div class="p-4 bg-purple_main rounded-full">
                <!-- top part ng post-->
                <div class="mb-4 flex items-center justify-between">
                    <!-- username nd pfp -->
                    <div class="flex items-center space-x-4">
                        <img src="https://i.pravatar.cc/300?img=70" class="w-[40px] rounded-img">
                        <p class="font-medium">Code With Stein</p>
                    </div>
                    <!-- time posted -->
                    <p class="text-gray-400 text-xs font-light">18 minutes ago</p> 
                </div>
                <!-- mid part - posted image/text -->

                    <img src="https://images.unsplash.com/photo-1661956602868-6ae368943878?ixlib=rb-4.0.3&amp;ixid=MnwxMjA3fDF8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&amp;auto=format&amp;fit=crop&amp;w=2670&amp;q=80" class="w-full rounded-full">

                <!-- lower part ng post -->
                <div class="mt-6 flex justify-between">
                    <div class="flex space-x-6">
                        <!-- likes -->
                        <div class="flex items-center space-x-2">
                            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
                                <path stroke-linecap="round" stroke-linejoin="round" d="M21 8.25c0-2.485-2.099-4.5-4.688-4.5-1.935 0-3.597 1.126-4.312 2.733-.715-1.607-2.377-2.733-4.313-2.733C5.1 3.75 3 5.765 3 8.25c0 7.22 9 12 9 12s9-4.78 9-12z"></path>
                            </svg>  
                            
                            <span class="text-gray-300 text-xs">82 likes</span>
                        </div>
                        <!-- comments -->
                        <div class="flex items-center space-x-2">
                            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
                                <path stroke-linecap="round" stroke-linejoin="round" d="M12 20.25c4.97 0 9-3.694 9-8.25s-4.03-8.25-9-8.25S3 7.444 3 12c0 2.104.859 4.023 2.273 5.48.432.447.74 1.04.586 1.641a4.483 4.483 0 01-.923 1.785A5.969 5.969 0 006 21c1.282 0 2.47-.402 3.445-1.087.81.22 1.668.337 2.555.337z"></path>
                            </svg> 

                            <span class="text-gray-300 text-xs ">0 comments</span>
                        </div>
                    </div>
                    <div> 
                        <!-- three dots -->
                        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
                            <path stroke-linecap="round" stroke-linejoin="round" d="M12 6.75a.75.75 0 110-1.5.75.75 0 010 1.5zM12 12.75a.75.75 0 110-1.5.75.75 0 010 1.5zM12 18.75a.75.75 0 110-1.5.75.75 0 010 1.5z"></path>
                        </svg>   
                    </div>   
                </div>  
            </div>

        </div>

    </div> 
</template> 

<!----> 