<template>
	<!-- 
        mx-auto: center of the screen 
        put "grid" or "flex" to assign the display before adding "grid-cols" or "flex-cols"
        space-(y or x): space for each elements like posts for example

        check tailwind.config.js for more configurations
        bg-purple_main: color ng header
        bg-blue_link: color ng links
    -->  
	<!-- header start if authenticated-->
		<nav class="bg-purple_main py-5 px-8 fixed w-full z-20 top-0 left-0" v-if="userStore.user.isAuthenticated"> 
					<div class="max-w-7xl mx-auto flex items-center flex-wrap justify-between">
						<!-- left menu logo start -->
								<div class="menu-left flex items-center ">
									<img src="../assets/img/logo/gl_logo.png" alt="logo"/>
								</div>
						<!-- center menu start -->
								<div class="menu-center items-center justify-between hidden w-full md:flex md:w-auto md:order-1 space-x-12 " id="navbar-user" >
									<ul class="flex flex-col font-medium p-4 md:p-0 mt-4 rounded-lg md:flex-row md:space-x-8 md:mt-0">
										<li>
											<RouterLink to="/feed" class="block py-2 pl-3 md:hover:text-black-700 md:p-0 md:dark:hover:text-black-500 dark:text-white dark:hover:bg-gray-700 dark:hover:text-black md:dark:hover:bg-transparent dark:border-gray-700">discussions </RouterLink>   
										</li>
										<li>
											<RouterLink to="/marketplace" class="block py-2 pl-3 md:hover:text-black-700 md:p-0 md:dark:hover:text-black-500 dark:text-white dark:hover:bg-gray-700 dark:hover:text-black md:dark:hover:bg-transparent dark:border-gray-700" >marketplace </RouterLink>
										</li>
										<li>
											<RouterLink to="/connect" class="block py-2 pl-3 md:hover:text-black-700 md:p-0 md:dark:hover:text-black-500 dark:text-white dark:hover:bg-gray-700 dark:hover:text-black md:dark:hover:bg-transparent dark:border-gray-700" >connect</RouterLink>
										</li>
										<li>
											<RouterLink to="/tournaments" class= "block py-2 pl-3 md:hover:text-black-700 md:p-0 md:dark:hover:text-black-500 dark:text-white dark:hover:bg-gray-700 dark:hover:text-black md:dark:hover:bg-transparent dark:border-gray-700" >tournaments </RouterLink>
										</li>
										<li>
											<RouterLink to="/betatesting" class="text-gray-400 rounded-t-lg cursor-not-allowed dark:text-white-500">beta testing </RouterLink>
										</li>
									</ul>
								</div>
						<!-- right menu icons start -->
								<div class="menu-right items-center justify-between hidden w-full md:flex md:w-auto md:order-1 space-x-2">
									<RouterLink to="/search" class="rounded-img p-2 hover:bg-[#28183e] bg-dark_purple">
										<svg height="24" viewBox="0 0 24 24" width="24" xmlns="http://www.w3.org/2000/svg"><path d="M16.3198574,14.9056439 L21.7071068,20.2928932 L20.2928932,21.7071068 L14.9056439,16.3198574 C13.5509601,17.3729184 11.8487115,18 10,18 C5.581722,18 2,14.418278 2,10 C2,5.581722 5.581722,2 10,2 C14.418278,2 18,5.581722 18,10 C18,11.8487115 17.3729184,13.5509601 16.3198574,14.9056439 Z M10,16 C13.3137085,16 16,13.3137085 16,10 C16,6.6862915 13.3137085,4 10,4 C6.6862915,4 4,6.6862915 4,10 C4,13.3137085 6.6862915,16 10,16 Z" fill-rule="evenodd" fill="white"/></svg>
										
									</RouterLink>
									
									<RouterLink to="/messages" class="rounded-img p-2 hover:bg-[#28183e] bg-dark_purple">
										<svg height="24" viewBox="0 0 24 24" width="24" xmlns="http://www.w3.org/2000/svg"><path d="M21,7.38246601 L21,5 L3,5 L3,7.38199365 L12.0000224,11.8824548 L21,7.38246601 Z M21,9.61853399 L11.9999776,14.1185452 L3,9.61810635 L3,19 L21,19 L21,9.61853399 Z M3,3 L21,3 C22.1045695,3 23,3.8954305 23,5 L23,19 C23,20.1045695 22.1045695,21 21,21 L3,21 C1.8954305,21 1,20.1045695 1,19 L1,5 C1,3.8954305 1.8954305,3 3,3 Z" fill-rule="evenodd" fill="white"/></svg>
									</RouterLink>									     
									<a href="#" class="hover:bg-[#28183e] rounded-img p-2 bg-dark_purple">
										<svg height="24" viewBox="0 0 24 24" width="24" xmlns="http://www.w3.org/2000/svg"><path d="M10.1353075,2.27592318 C10.2402118,2.0052531 10.405725,1.75363521 10.6305147,1.54243008 C11.4002733,0.819189975 12.5997267,0.819189975 13.3694853,1.54243008 C13.5947695,1.75409979 13.7605161,2.00636024 13.8653839,2.27770959 C16.7616088,3.1234978 19,5.9408248 19,10 C19,12.6246407 19.5316915,14.1023939 20.5153799,15.1769385 C20.7591805,15.4432571 21.6159553,16.2145106 21.7120353,16.3119441 L22,16.6039656 L22,20.0140878 L15.8743256,20.0140878 C15.6241439,20.9988638 15.0074832,21.861375 14.0878016,22.4226016 C12.8058555,23.2048965 11.1941445,23.2048965 9.91219841,22.4226016 C8.87009269,21.7866669 8.29383594,21.076125 8.08797645,20.0140878 L2,20.0140878 L2,16.6039656 L2.2879647,16.3119441 C2.39205094,16.2070827 3.24384208,15.442761 3.48595854,15.1793313 C4.46898326,14.1097716 5,12.6338939 5,10 C5,5.92919283 7.23535296,3.11802713 10.1353075,2.27592318 Z M10.1786171,20.0140878 C10.3199018,20.276911 10.5607105,20.4753661 10.9540156,20.7153766 C11.596268,21.1073049 12.403732,21.1073049 13.0459844,20.7153766 C13.3433933,20.5338858 13.5757865,20.2937382 13.7367218,20.0140878 L10.1786171,20.0140878 Z M20,17.4519264 C19.701613,17.1774463 19.2506046,16.7572744 19.0401756,16.5274096 C17.7059972,15.0700027 17,13.1077943 17,10 C17,6.23128941 14.6597092,4.01238167 12,4.01238167 C9.33276935,4.01238167 7,6.21989471 7,10 C7,13.1178011 6.29422173,15.0794011 4.95848591,16.5327208 C4.74843403,16.7612633 4.29607181,17.181102 4,17.45237 L4,18.0140878 L20,18.0140878 L20,17.4519264 Z" fill-rule="evenodd" fill="white"/></svg>                    
									</a>
          
									<!-- user icon -->
									
									<div class="flex items-center md:order-2">
											<button type="button" class="flex mr-3 text-sm rounded-img md:mr-0" id="user-menu-button" aria-expanded="false" data-dropdown-toggle="user-dropdown" data-dropdown-placement="bottom">
												<span class="sr-only">open user menu</span>
												<RouterLink :to="{name: 'profile', params:{'id': userStore.user.id}}" >
													<img class="w-10 h-10 rounded-img  hover:opacity-80" src="https://i.pravatar.cc/300?img=70" alt="user photo">
												</RouterLink> 
											</button>
											<!-- Dropdown menu -->
											<div class="z-50 hidden my-4 text-base list-none bg-white divide-y divide-gray-100 rounded-lg shadow dark:bg-gray-700 dark:divide-gray-600" id="user-dropdown">
												<div class="px-4 py-3">
												<span class="block text-sm text-gray-900 dark:text-white">Bonnie Green</span>
												<span class="block text-sm  text-gray-500 truncate dark:text-gray-400">name@flowbite.com</span>
												</div>
												<ul class="py-2" aria-labelledby="user-menu-button">
												<li>
													<a href="#" class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 dark:hover:bg-gray-600 dark:text-gray-200 dark:hover:text-white">profile</a>
												</li>
												<li>
													<a href="#" class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 dark:hover:bg-gray-600 dark:text-gray-200 dark:hover:text-white">settings</a>
												</li>

												<li>
													<a href="#" class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 dark:hover:bg-gray-600 dark:text-gray-200 dark:hover:text-white">logout</a>
												</li>
												</ul>
											</div>
											<button data-collapse-toggle="navbar-user" type="button" class="inline-flex items-center p-2 w-10 h-10 justify-center text-sm text-gray-500 rounded-lg md:hidden hover:bg-gray-100 focus:outline-none focus:ring-2 focus:ring-gray-200 dark:text-gray-400 dark:hover:bg-gray-700 dark:focus:ring-gray-600" aria-controls="navbar-user" aria-expanded="false">
												<span class="sr-only">open main menu</span>
												<svg class="w-5 h-5" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 17 14">
													<path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M1 1h15M1 7h15M1 13h15"/>
												</svg>
											</button>
										</div>
								</div>   
								
					</div>
		
		</nav>
	<!-- header end -->

	<!-- main view-->
		<main class=" px-8 py-28 bg-fixed md:bg-fixed bg-cover bg-[url('../assets/img/bg/bg-2.png')]"> 
			<RouterView /> 
		</main>

		<Toast /> <!--  shows the alert sa frontend -->

		<!-- bg-fixed md:bg-fixed bg-cover bg-[url('../assets/img/bg/bg-1.svg')] -->
	
</template> 

<script>
	import axios from 'axios'
    import Toast from '@/components/Toast.vue'
    import { useUserStore } from '@/stores/user'

    export default {
        setup() {
            const userStore = useUserStore()

            return {
                userStore
            }
        },

        components: {
            Toast
        },

        beforeCreate() {
            this.userStore.initStore()

            const token = this.userStore.user.access

            if (token) {
                axios.defaults.headers.common["Authorization"] = "Bearer " + token;
            } else {
                axios.defaults.headers.common["Authorization"] = "";
            }
        }
    }
</script>