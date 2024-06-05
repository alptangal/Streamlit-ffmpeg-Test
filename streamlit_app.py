import os

os.system('''cargo install fnm
          docker pull node:20-alpine
          npm install @dank074/discord-video-stream@latest
npm install discord.js-selfbot-v13@latest''')
os.system('node main.js')