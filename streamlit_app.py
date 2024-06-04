import pathlib
import subprocess

import ffmpeg
import streamlit as st
import os

os.system('ffmpeg -i video.mp4 -deinterlace -vcodec libx264 -pix_fmt yuv420p -preset medium -r 30 -g 60 -b:v 2500k -acodec libmp3lame -ar 44100 -threads 6 -qscale 3 -b:a 712000 -bufsize 512k -f flv rtmp://a.rtmp.youtube.com/live2/vf7p-py39-erw8-k6z0-56d2')

# global variables
'''stream = ffmpeg.input('input.mp4')
stream = ffmpeg.hflip(stream)
stream = ffmpeg.output(stream, 'output.mp4')
ffmpeg.run(stream)'''