<template>
  
  <div class="main-left col-span-1 space-y-6">

    <div class="p-4 bg-purple_main border-gray-200 rounded-full">
        <h3 class="mb-6 font-semibold text-xl tracking-wide">most talked about games</h3>

        <div class="space-y-4 px-4 text-left">
                <div v-for="game in popularGames" :key="game.id" class="flex items-center justify-between border-b-2">
                    <a :href="'/games/' + game.id" class="w-full py-2 px-3 hover:bg-purple_main">{{ game.title }}</a>
                </div>
        </div>
    </div>
     
            <div class="p-4 bg-purple_main rounded-full">
                <h3 class="mb-6 text-lg">useful links</h3>

                <p class="text-base/7 font-light mb-6">our instance rules are here and cover the ideals and how we want this
                    community to evolve.</p>
                <p class="text-base/7 font-light mb-2">where you can download games:</p>

                <ul class="list-inside">

                    <li class="p-1 hover:underline">
                        <a href="https://www.riotgames.com/en" target="_blank" rel="noopener noreferrer"><img
                                src="/assets/img/logo/riot_logo.png" class="h-auto max-w-full" alt="logo" />riot games</a>
                    </li>

                    <li class="p-1 hover:underline">
                        <a href="https://store.steampowered.com/" target="_blank" rel="noopener noreferrer"><img
                                src="/assets/img/logo/steam_logo.png" class="h-auto max-w-full" alt="logo" />steam</a>
                    </li>

                    <li class="p-1 hover:underline">
                        <a href="https://store.epicgames.com/en-US/" target="_blank" rel="noopener noreferrer"><img
                                src="/assets/img/logo/epic_logo.png" class="h-auto max-w-full" alt="logo" />epic games</a>
                    </li>

                    <li class="p-1 hover:underline">
                        <a href="https://us.shop.battle.net/en-us" target="_blank" rel="noopener noreferrer"><img
                                src="/assets/img/logo/battle_logo.png" class="h-auto max-w-full" alt="logo" />battle.net</a>
                    </li>

                </ul>
            </div>
        </div>
</template>

<script>
    import axios from 'axios';

export default {
  data() {
    return {
      popularGames: [],
    };
  },
  mounted() {
    this.fetchPopularGames();
  },
  methods: {
    fetchPopularGames() {
      axios.get('/api/posts/popular_games') // Replace with your actual API endpoint
        .then(response => {
          this.popularGames = response.data;
        })
        .catch(error => {
          console.error('Error fetching popular games:', error);
        });
    },
  },
};
</script>