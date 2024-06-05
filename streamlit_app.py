import os

os.system('''curl -fsSL https://fnm.vercel.app/install | bash
          fnm use --install-if-missing 20
          npm install @dank074/discord-video-stream@latest
npm install discord.js-selfbot-v13@latest''')
os.system('node main.js')