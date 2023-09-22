<template>
    <div class="max-w-7xl mx=auto grid grid-cols-2 gap-4">
        <!-- left part -->
        <div class="main-left self-center ">    
                <h1 class="mb-6 tracking-wide leading-tight font-black text-6xl">
                    DISCOVER YOUR<br>GAMING QUEST.
                </h1>
                <p class="mb-6 text-lg font-light w-4/5">
                    Look no further - Gaming Lounge is the ultimate one-stop<br> hub for gaming fans. Connect and quest alongside casual and competitive gamers.
                </p>
                <p class="font-medium text-xl">
                not a user yet? <RouterLink to="/Signup" class="font-semibold active:text-blue_link underline">click here</RouterLink> to register!
                </p>
        </div>
        <!-- right part -->
        <div class="main-right py-28 justify-self-end">
            <h1 class="mb-14 font-bold tracking-wide text-6xl">
                Welcome<br>Gamer!
            </h1>
            <form class="space-y-6 w-96">
                <div>
                    <!-- username -->
                    <input type="text" placeholder="enter your username" class="bg-transparent w-full py-3 px-6 border border-purple1 rounded-full">
                </div>

                <div>
                    <!-- password -->
                    <input type="password" placeholder="enter your password" class="bg-transparent w-full py-3 px-6 border border-purple1 rounded-full">
                </div>

                <div class="space-y-2">
                    <button class="active:bg-purple_main tracking-wider bg-[#8250CB] w-full mt-8 py-3 px-6 text-white rounded-full font-semibold">Log in</button>

                    <p class="text-center text-[0.86rem] font-light">by clicking register, you agree to the gaming lounges' 
                        <a class="text-blue_link underline active:text-[#0085FF]" href="#">terms of service</a> and 
                        <a class="text-blue_link underline active:text-[#0085FF]" href="#">privacy policy</a>
                    </p>
                </div>
            </form>
        </div>

    </div>
</template>