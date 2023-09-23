<template>
	<!-- 
        mx-auto: center of the screen 
        put "grid" or "flex" to assign the display before adding "grid-cols" or "flex-cols"
        space-(y or x): space for each elements like posts for example

        check tailwind.config.js for more configurations
        bg-purple_main: color ng header
        bg-blue_link: color ng links
    -->  
	<!-- header start -->
		<nav class="bg-purple_main py-5 px-8">
				<div class="max-w-7xl mx-auto">
					<div class="flex items-center justify-between">
						<!-- left menu logo start -->
								<div class="menu-left">
									<img src="../assets/img/logo/gl_logo.png" alt="logo"/>
								</div>
						<!-- center menu start -->
								<div class="menu-center flex space-x-12">
									<a href="#" class="text-black">discussions</a>                         
									<a href="#" class="text-white">connect</a>
									<a href="#" class="text-white">marketplace</a>
									<a href="#" class="text-white">tournaments</a>
									<a href="#" class="text-white">beta testing</a>
								</div>
						<!-- right menu icons start -->
								<div class="menu-right flex space-x-2">
									<a href="#" class="text-white">
										<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-8 h-8">
											<path stroke-linecap="round" stroke-linejoin="round" d="M14.857 17.082a23.848 23.848 0 005.454-1.31A8.967 8.967 0 0118 9.75v-.7V9A6 6 0 006 9v.75a8.967 8.967 0 01-2.312 6.022c1.733.64 3.56 1.085 5.455 1.31m5.714 0a24.255 24.255 0 01-5.714 0m5.714 0a3 3 0 11-5.714 0" />
										</svg>                     
									</a>
									<a href="#" class="text-white">
										<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-8 h-8">
											<path stroke-linecap="round" stroke-linejoin="round" d="M8.625 12a.375.375 0 11-.75 0 .375.375 0 01.75 0zm0 0H8.25m4.125 0a.375.375 0 11-.75 0 .375.375 0 01.75 0zm0 0H12m4.125 0a.375.375 0 11-.75 0 .375.375 0 01.75 0zm0 0h-.375M21 12c0 4.556-4.03 8.25-9 8.25a9.764 9.764 0 01-2.555-.337A5.972 5.972 0 015.41 20.97a5.969 5.969 0 01-.474-.065 4.48 4.48 0 00.978-2.025c.09-.457-.133-.901-.467-1.226C3.93 16.178 3 14.189 3 12c0-4.556 4.03-8.25 9-8.25s9 3.694 9 8.25z" />
										</svg>
									</a>
									<!-- <a href="#"><img src="https://i.pravatar.cc/40" class="rounded-full"></a> -->
								</div>   
					</div>
			</div>
		</nav>
	<!-- header end -->
	
	<!-- main view-->
		<main class="flex justify-center items-center flex-wrap px-8 py-6 bg-fixed bg-[url('../assets/img/bg/bg-1.svg')]"> 
			<RouterView /> 
		</main>
	
</template> 