<template>
    <div class="max-w-7xl mx-auto grid grid-cols-4 gap-4">
        <!-- inbox -->
        <div class="main-left col-span-1">
            <div class="p-4 bg-purple_main rounded-full">
                <div class="space-y-4">
                    <div class="flex items-center justify-between">
                        <div class="flex items-center space-x-2">
                            <img src="https://i.pravatar.cc/300?img=70" class="w-[45px] rounded-full">
                            <p class="font-light"><strong>Code With Stein</strong></p>
                        </div>

                        <span class="text-xs text-gray-400 font-light">18 minutes ago</span>
                    </div>

                    <div class="flex items-center justify-between">
                        <div class="flex items-center space-x-2">
                            <img src="https://i.pravatar.cc/300?img=70" class="w-[45px] rounded-full">
                            
                            <p class="font-light"><strong>Code With Stein</strong></p>
                        </div>

                        <span class="text-xs text-gray-400 font-normal">18 minutes ago</span>
                    </div>

                    <div class="flex items-center justify-between">
                        <div class="flex items-center space-x-2">
                            <img src="https://i.pravatar.cc/300?img=70" class="w-[45px] rounded-full">
                            
                            <p class="font-light"><strong>Code With Stein</strong></p>
                        </div>

                        <span class="text-xs text-gray-400 font-light">18 minutes ago</span>
                    </div>
                </div>
            </div>
        </div>
        <!-- messages -->
        <div class="main-center col-span-3 space-y-4">
            <div class="bg-purple_main border border-2 rounded-full">
                <div class="flex flex-col flex-grow p-4">
                    <div class="flex w-full mt-2 space-x-3 max-w-md ml-auto justify-end">
                        <div>
                            <div class="bg-blue-600 text-white p-3 rounded-l-lg rounded-br-lg">
                                <p class="text-sm">Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod.</p>
                            </div>
                            <span class="text-xs text-gray-400 font-light leading-none">2 min ago</span>
                        </div>
                        <div class="flex-shrink-0 h-10 w-10 rounded-full bg-gray-300">
                            <img src="https://i.pravatar.cc/300?img=70" class="w-[40px] rounded-full">
                        </div>
                    </div>

                    <div class="flex w-full mt-2 space-x-3 max-w-md ml-auto justify-end">
                        <div>
                            <div class="bg-blue-600 text-white p-3 rounded-l-lg rounded-br-lg">
                                <p class="text-sm">Lorem ipsum dolor sit amet</p>
                            </div>
                            <span class="text-xs text-gray-400 font-light leading-none">2 min ago</span>
                        </div>
                        <div class="flex-shrink-0 h-10 w-10 rounded-full bg-gray-300">
                            <img src="https://i.pravatar.cc/300?img=70" class="w-[40px] rounded-full">
                        </div>
                    </div>

                    <div class="flex w-full mt-2 space-x-3 max-w-md">
                        <div class="flex-shrink-0 h-10 w-10 rounded-full bg-gray-300">
                            <img src="https://i.pravatar.cc/300?img=70" class="w-[40px] rounded-full">
                        </div>
                        <div>
                            <div class="bg-gray-300 p-3 rounded-r-lg rounded-bl-lg">
                                <p class="text-sm">Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. </p>
                            </div>
                            <span class="text-xs text-gray-400 font-light leading-none">2 min ago</span>
                        </div>
                    </div>
                </div>
            </div>
            <!-- compose message -->
          
                 <div class="text-right">
                    <textarea class="p-4 w-full bg-purple_main rounded-full" placeholder="what do you want to say?"></textarea>
            
                    <a href="#" class="inline-block p-2 active:bg-violet1 inline-block text-center w-24 p-2 bg-purple_main text-white rounded-full">send</a>
                 </div>
                    
            
            
        </div>
    </div>

</template>