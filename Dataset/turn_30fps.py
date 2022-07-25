import os
import cv2
import numpy as np
# %%
path = r".\videos"
dir = os.listdir(path)

for i in dir:
    newFramePath = i.split('.')[0]
    outputfolder = './videos_normilaized/'
    if not os.path.exists(outputfolder):
        os.makedirs(outputfolder)

    input = r'.\videos' + '/' + i
    output = outputfolder + newFramePath + '.mp4'
    command = f"ffmpeg -i {input} -filter:v fps=30 -s 1280x720 -c:a copy {output}"
    os.system(command)
