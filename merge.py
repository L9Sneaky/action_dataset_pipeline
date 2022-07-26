import pickle
import pandas as pd
import math as m
import cv2
import json
import numpy as np
import os
# %%
pretraincsv_path = r'Dataset\outputs\train.csv'
df = pd.read_csv(pretraincsv_path, sep=',')
df.columns=(['videoID', 'frame', 'x1', 'y1', 'x2', 'y2', 'id'])
videoIDs = df['videoID'].unique()


# %%
input = r'Dataset\metadata_in'
output = r'Dataset\metadata_out'
meta = os.listdir(input)
for i in range(len(meta)):
    metadata = input+ '/' + meta[i]
    savejson = output+ '/' + meta[i]
    df3 = pd.read_json(metadata)
    name = meta[i].split('.')[0].split('_')
    newname = name[0]+'_'+name[1]+'_'+name[2]
    #merge yolov5/strongsort with via metadata
    # generate indexs
    vidx = df['videoID']==newname
    print('generate indexs')
    inx = []
    framenum = 1
    for a in range(len(df[vidx])):
        for j in range(len(df[(vidx) & (df['frame']==a)])):
            bb = str(a)+'_'+(8-len(str(framenum)))*'0'+ str(j)
            inx.append(bb)
        framenum += 1
    print('indexs: '+ str(len(inx)))

    vid = [] #frame
    flg = []
    z = []
    xy = []
    av = []
    for i in range(len(df[vidx])):
        print(newname + ' frame: '+ str(i))
        x = int(df[vidx].iloc[i]['x1'])
        y = int(df[vidx].iloc[i]['y1'])
        w = int(df[vidx].iloc[i]['x2'])
        h = int(df[vidx].iloc[i]['y2'])

        x2 = w - x
        y2 = h - y

        vid.append(str(df[vidx]['frame'].iloc[i]))
        flg.append(0)
        z.append([])
        xy.append([2, x, y , x2, y2])
        av.append({'1': '0'})

    jsons = pd.DataFrame([vid, flg, z, xy, av]).transpose()
    jsons.columns=(['vid','flg','z','xy','av'])
    jsons.index = (inx)

    with open(metadata, 'r+') as f:
        data = json.load(f)
        data['metadata'] = jsons.transpose().to_dict()

    with open(savejson, 'w') as fp:
        json.dump(data, fp)
print('done merging')
