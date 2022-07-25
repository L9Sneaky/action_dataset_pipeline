import os
import cv2
import numpy as np
# %%
path = r".\Dataset\videos"
dir = os.listdir(path)
dir

for i in dir:
    newFramePath = i.split('.')[0]
    outputfolder = './Dataset/videos_normilaized/'
    if not os.path.exists(outputfolder):
        os.makedirs(outputfolder)

    input = r'.\Dataset\videos' + '/' + i
    output = outputfolder + newFramePath + '.mp4'
    command = f"ffmpeg -i {input} -filter:v fps=30 -s 1280x720 -c:a copy {output}"
    os.system(command)
