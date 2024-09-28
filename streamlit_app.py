import os,sys
import server
import asyncio
import requests

async def main():
    try:
        print(11111)
        req=requests.get('http://localhost:8888')
        print(req.status_code)
        print('Client closed')
        exit()
    except:
        server.b()
        os.system('ffmpeg -re -stream_loop -1 -i video1.mp4 -c:v libx264 -preset veryfast -maxrate 3000k -bufsize 6000k -vf "format=yuv420p" -g 50 -c:a aac -b:a 128k -f flv rtmp://live.twitch.tv/app/live_592628789_TRD4VwvElUMsxSSauahoWFXVONOTq2')
asyncio.run(main())