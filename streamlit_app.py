import os
import server
import asyncio
import requests

async def main():
    try:
        req=requests.get('http://localhost:8888')
        print(req.status_code)
        print('Client closed')
        exit()
    except:
        server.b()  
        os.system('''
                npm install @dank074/discord-video-stream@latest
                npm install discord.js-selfbot-v13@latest
                ''')
        os.system('node main.js')
asyncio.run(main())