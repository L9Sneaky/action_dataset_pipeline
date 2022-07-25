@echo off

call activate ads-pipeline

cd Dataset/
python turn_30fps.py
python cut_frames.py
cd ..
cd Yolov5_StrongSORT_OSNet
python track_g.py
PAUSE
