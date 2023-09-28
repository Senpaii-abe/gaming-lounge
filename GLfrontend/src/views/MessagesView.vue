<template>
    <!-- scroll: h-full overflow-y-scroll -->
    <div class="max-w-7xl mx-auto grid grid-cols-4 gap-4">
        <!-- inbox -->
        <div class="main-left col-span-1 flex flex-col bg-purple_main rounded-full p-4 overflow-auto h-full">
            <!-- <div class="p-4 bg-purple_main rounded-full">
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
            </div> -->
            <label for="" class="text-center text-xl font-semibold border-b pb-2">chats</label>
            
            <ul class="mt-3">
                <li class="p-3 transition hover:bg-[#181327] rounded-lg">                  
                    <a href="#" class="flex justify-between items-center">
                        <div class="flex items-center space-x-3">
                            <img src="https://i.pravatar.cc/300?img=70" class="w-[45px] rounded-full">
                            <h3 class="font-semibold text-base justify-self-start">Akhil Gautam</h3>
                        </div>    
                        <span class="text-xs text-gray-400 font-light ">23m ago</span>
                    </a>
                </li>
                <li class="p-3 transition hover:bg-[#181327] rounded-lg">                  
                    <a href="#" class="flex justify-between items-center">
                        <div class="flex items-center space-x-3">
                            <img src="https://i.pravatar.cc/300?img=70" class="w-[45px] rounded-full">
                            <h3 class="font-semibold text-base justify-self-start">Akhil Gautam</h3>
                        </div>    
                        <span class="text-xs text-gray-400 font-light ">23m ago</span>
                    </a>
                </li>
                <li class="p-3 transition hover:bg-[#181327]  rounded-lg">                  
                    <a href="#" class="flex justify-between items-center">
                        <div class="flex items-center space-x-3">
                            <img src="https://i.pravatar.cc/300?img=70" class="w-[45px] rounded-full">
                            <h3 class="font-semibold text-base justify-self-start">Akhil Gautam</h3>
                        </div>    
                        <span class="text-xs text-gray-400 font-light ">23m ago</span>
                    </a>
                </li>
                <li class="p-3 transition hover:bg-[#181327] rounded-lg">                  
                    <a href="#" class="flex justify-between items-center">
                        <div class="flex items-center space-x-3">
                            <img src="https://i.pravatar.cc/300?img=70" class="w-[45px] rounded-full">
                            <h3 class="font-semibold text-base justify-self-start">Akhil Gautam</h3>
                        </div>    
                        <span class="text-xs text-gray-400 font-light ">23m ago</span>
                    </a>
                </li>
                
             
            </ul>
 
        </div>
        <!-- messages -->
        <div class="main-center col-span-3 space-y-4">
            <div class="bg-purple_main rounded-full">
                <div class="flex flex-col flex-grow p-4">
                    <div class="flex w-full mt-2 space-x-3 max-w-md ml-auto justify-end">
                        <div>
                            <div class="bg-[#181327] text-white p-3 rounded-l-full rounded-br-full">
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
                            <div class="bg-[#181327] text-white p-3 rounded-l-full rounded-br-full">
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
                            <div class="bg-[#181327] p-3 rounded-r-full rounded-bl-full">
                                <p class="text-sm">Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. </p>
                            </div>
                            <span class="text-xs text-gray-400 font-light leading-none">2 min ago</span>
                        </div>
                    </div>
                </div>
            </div>
            <!-- compose message 8454B4 -->
          
                 <!-- <div class="text-right">
                    <textarea class="p-4 w-full bg-purple_main rounded-large" placeholder="what do you want to say?"></textarea>
            
                    <a href="#" class="inline-block p-2 active:bg-violet1 inline-block text-center w-24 p-2 bg-purple_main text-white rounded-full">send</a>
                 </div> -->
                 <form>
                    <label for="chat" class="sr-only">your message</label>
                        <div class="flex items-center px-3 py-2 rounded-large bg-gray-50 dark:bg-purple_main">
                            <button type="button" class="p-2 text-gray-500 rounded-large cursor-pointer hover:text-gray-900 hover:bg-gray-100 dark:text-gray-400 dark:hover:text-white dark:hover:bg-gray-600">
                                <svg class="w-5 h-5" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 20 20">
                                    <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13.408 7.5h.01m-6.876 0h.01M19 10a9 9 0 1 1-18 0 9 9 0 0 1 18 0ZM4.6 11a5.5 5.5 0 0 0 10.81 0H4.6Z"/>
                                </svg>
                                <span class="sr-only">Add emoji</span>
                            </button>
                            <textarea id="chat" rows="1" class="block mx-2 p-2.5 w-full text-sm rounded-large dark:bg-[#181327]" placeholder="your message.."></textarea>
                                <button type="submit" class="inline-flex justify-center p-2 text-blue-600 rounded-full cursor-pointer hover:bg-blue-100 dark:text-blue-500 dark:hover:bg-gray-600">
                                <svg class="w-5 h-5 rotate-90" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="white" viewBox="0 0 18 20">
                                    <path d="m17.914 18.594-8-18a1 1 0 0 0-1.828 0l-8 18a1 1 0 0 0 1.157 1.376L8 18.281V9a1 1 0 0 1 2 0v9.281l6.758 1.689a1 1 0 0 0 1.156-1.376Z"/>
                                </svg>
                                <span class="sr-only">send message</span>
                            </button>
                        </div>
                </form>
                    
            
            
        </div>
    </div>

</template>
