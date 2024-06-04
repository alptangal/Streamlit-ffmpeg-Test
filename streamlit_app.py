import pathlib
import subprocess

import ffmpeg
import streamlit as st
import os
import asyncio
import server
import requests
async def main():
    try:
        req=requests.get('http://localhost:8888')
        print(req.status_code)
        print('Client closed')
        exit()
    except:
        os.system('ffmpeg -i video1.mp4 -deinterlace -vcodec libx264 -pix_fmt yuv420p -preset medium -r 30 -g 60 -b:v 2500k -acodec libmp3lame -ar 44100 -threads 6 -qscale 3 -b:a 712000 -bufsize 512k -f flv rtmp://iad05.contribute.live-video.net/app/live_592628789_SEBNXuQGAcjUBxf6kaisYn4ag266WD')
asyncio.run(main())
# global variables
'''stream = ffmpeg.input('input.mp4')
stream = ffmpeg.hflip(stream)
stream = ffmpeg.output(stream, 'output.mp4')
ffmpeg.run(stream)'''