import os
import subprocess as sp

IN_DATA_DIR = "./videos_normilaized"
OUT_DATA_DIR = "./frames"

if not os.path.exists(OUT_DATA_DIR):
    print(f"{OUT_DATA_DIR} doesn't exist. Creating it.")
    os.makedirs(OUT_DATA_DIR)

for video in os.listdir(IN_DATA_DIR):
    video_name = video.split('.')[0]
    print(video_name)

    out_video_dir = f'{OUT_DATA_DIR}/{video_name}/'
    if not os.path.exists(out_video_dir):
        print(f"{out_video_dir} doesn't exist. Creating it.")
        os.makedirs(out_video_dir)

    input = IN_DATA_DIR + f'/{video}'
    out_name = f"{out_video_dir}/{video_name}_%06d.jpg"
    sp.call(f'ffmpeg -i {input} -r 30 -q:v 1 {out_name}',shell=True)

    os.remove(f'{out_video_dir}/{video_name}_000001.jpg')
    os.remove(f"{out_video_dir}/{video_name}_000002.jpg")
