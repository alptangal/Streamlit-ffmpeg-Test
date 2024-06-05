import os,sys
import server
import asyncio
import requests

async def main():
    try:
        req=requests.get('http://localhost:8888')
        print(req.status_code)
        if req.status_code<400:
            print('Client closed')
            os._exit()
    except Exception as error:
        print(error)
        if 'No connection could be made because the target machine actively refused it' in str(error) or ('req' in locals() and req.status_code>=400):
            server.b()  
            os.system('''
                    npm install @dank074/discord-video-stream@latest
                    npm install discord.js-selfbot-v13@latest
                    ''')
            os.system('node main.js')
asyncio.run(main())