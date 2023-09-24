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
        'blue_link': '#8AC6FD', // color for link
        'dark_purple': '#020816' // color ng background
      },
      borderRadius: {
        'none': '0',
        'sm': '0.125rem',
        DEFAULT: '0.25rem',
        DEFAULT: '4px',
        'md': '0.375rem',
        'lg': '0.5rem',
        'full': '20px',
        'img':'9999px',
        'large': '100px',
      },
      fontSize: {
        sm: '0.8rem',
        base: '1rem',
        xl: '1.25rem',
        '2xl': '1.563rem',
        '3xl': '1.953rem',
        '4xl': '2.441rem',
        '5xl': '3.052rem',
      },



      // backgroundImage: {
      //   'hero-pattern': "url('/assets/img/bg/bg-1.svg')",
      //   'footer-texture': "url('/img/footer-texture.png')",
      // }
    },
  },
  plugins: [],
}

