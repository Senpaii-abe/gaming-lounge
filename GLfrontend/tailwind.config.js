/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./index.html",
    "./src/**/*.{html,vue,js,ts,jsx,tsx}", // joey added html
  ],
  theme: {
    extend: {
      colors: {
        'purple1': '#A35DD2', // for border
        'violet1': '#8150CA',  // for border
        'purple_main': '#4B2E75', // main color of the website
        'blue_link': '#8AC6FD' // color for link
      }

      // backgroundImage: {
      //   'hero-pattern': "url('/assets/img/bg/bg-1.svg')",
      //   'footer-texture': "url('/img/footer-texture.png')",
      // }
    },
  },
  plugins: [],
}

