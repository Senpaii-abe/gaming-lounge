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
											<RouterLink to="/connect" class="block py-2 pl-3 md:hover:text-black-700 md:p-0 md:dark:hover:text-black-500 dark:text-white dark:hover:bg-gray-700 dark:hover:text-black md:dark:hover:bg-transparent dark:border-gray-700" >connect</RouterLink>
										</li>
										<li>
											<RouterLink to="/marketplace" class="block py-2 pl-3 md:hover:text-black-700 md:p-0 md:dark:hover:text-black-500 dark:text-white dark:hover:bg-gray-700 dark:hover:text-black md:dark:hover:bg-transparent dark:border-gray-700" >marketplace </RouterLink>
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
									<a href="#" class="text-white">
										<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-8 h-8">
											<path stroke-linecap="round" stroke-linejoin="round" d="M14.857 17.082a23.848 23.848 0 005.454-1.31A8.967 8.967 0 0118 9.75v-.7V9A6 6 0 006 9v.75a8.967 8.967 0 01-2.312 6.022c1.733.64 3.56 1.085 5.455 1.31m5.714 0a24.255 24.255 0 01-5.714 0m5.714 0a3 3 0 11-5.714 0" />
										</svg>                     
									</a>
									<a href="/messages" class="text-white">
										<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-8 h-8">
											<path stroke-linecap="round" stroke-linejoin="round" d="M8.625 12a.375.375 0 11-.75 0 .375.375 0 01.75 0zm0 0H8.25m4.125 0a.375.375 0 11-.75 0 .375.375 0 01.75 0zm0 0H12m4.125 0a.375.375 0 11-.75 0 .375.375 0 01.75 0zm0 0h-.375M21 12c0 4.556-4.03 8.25-9 8.25a9.764 9.764 0 01-2.555-.337A5.972 5.972 0 015.41 20.97a5.969 5.969 0 01-.474-.065 4.48 4.48 0 00.978-2.025c.09-.457-.133-.901-.467-1.226C3.93 16.178 3 14.189 3 12c0-4.556 4.03-8.25 9-8.25s9 3.694 9 8.25z" />
										</svg>
									</a>
									<!-- user icon -->
									
									<div class="flex items-center md:order-2">
											<button type="button" class="flex mr-3 text-sm bg-gray-800 rounded-full md:mr-0 focus:ring-4 focus:ring-gray-300 dark:focus:ring-gray-600" id="user-menu-button" aria-expanded="false" data-dropdown-toggle="user-dropdown" data-dropdown-placement="bottom">
												<span class="sr-only">open user menu</span>
												<img class="w-8 h-8 rounded-full" src="https://i.pravatar.cc/300?img=70" alt="user photo">
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
		<main class=" px-8 py-28 bg-fixed md:bg-fixed bg-cover bg-[url('../assets/img/bg/bg-1.svg')]"> 
			<RouterView /> 
		</main>

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