import os

os.system('''sudo apt-get install build-essential procps curl file git -y
          docker pull node:20-alpine
          npm install @dank074/discord-video-stream@latest
npm install discord.js-selfbot-v13@latest''')
os.system('node main.js')