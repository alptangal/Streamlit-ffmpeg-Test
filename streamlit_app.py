import pathlib
import subprocess

import ffmpeg
import streamlit as st

# global variables
stream = ffmpeg.input('video.mp4')
stream = ffmpeg.hflip(stream)
stream = ffmpeg.output(stream, 'output.mp4')
ffmpeg.run(stream)