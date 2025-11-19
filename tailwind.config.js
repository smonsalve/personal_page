/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./templates/**/*.html",
    "./static/js/**/*.js"
  ],
  theme: {
    extend: {
      colors: {
        // Add your custom colors here
        'primary': '#3B82F6',
        'secondary': '#10B981',
      },
      fontFamily: {
        // Add your custom fonts here
        'sans': ['Inter', 'system-ui', 'sans-serif'],
      },
    },
  },
  plugins: [],
}
