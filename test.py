import pickle
import pandas as pd
import torch
import math as m
import cv2
import json
import numpy as np
# %%
torch.cuda.is_available()
# %%
img = cv2.imread(r'pipeline\Dataset\frames\video1\video1_000001.jpg')
vh, vw, _  = img.shape
vh,vw
# %%
X = pickle.load(open(r"annotations\ava_dense_proposals_train.FAIR.recall_93.9.pkl", "rb"))
X
type(X)
type(X['3IOE-Q3UWdA,0902'])
X
pd.DataFrame(X['3IOE-Q3UWdA,0902'], columns=[[ 'x1', 'y1', 'x2', 'y2', 'conf']])

# %%

Y = pd.read_csv(r'annotations\ava_train_v2.2.csv')
Y.columns=[['videoID', 'Frame', 'x1', 'y1', 'x2', 'y2', 'action', 'id']]
Y.loc[(Y['videoID'] == '3IOE-Q3UWdA').to_numpy() & (Y['Frame'] == 1798).to_numpy()]

Y.loc[(Y['videoID'] == '3IOE-Q3UWdA').to_numpy()]

# %%

Z = pd.read_csv(r'annotations\ava_train_excluded_timestamps_v2.2.csv')
Z.columns =[['video_id','second_idx']]
Z.loc[(Z['video_id'] == '3IOE-Q3UWdA').to_numpy()]

# %%
proposal_path = r'Yolov5_DeepSort_OSNet\runs\track\exp43\tracks\video_crop_proposal.pickle'
proposal_path2 = r'Yolov5_DeepSort_OSNet\runs\track\exp43\tracks\video_crop.txt'
pretraincsv_path = r'Yolov5_DeepSort_OSNet\runs\track\exp43\tracks\video_crop2.txt'
# .loc[(Y['videoID'] == '-5KQ66BBWC4').to_numpy()]

test = pickle.load(open(proposal_path, "rb"))
test


df1 = pd.read_csv(proposal_path2, sep = ' ')
df1.columns=[['x1', 'y1', 'x2', 'y2', 'conf']]
df1.head()

df = pd.read_csv(pretraincsv_path, index_col=0)
df.columns=([['videoID', 'frame', 'x1', 'y1', 'x2', 'y2', 'id']])
df


# %%

action_list= {
    "0": "Talking",
    "1": "Listing",
    "2": "shaking hands"
}

df3 = pd.read_json('099f30aa_22Jun2022_09h55m25s.json')
df3['metadata']
df4 = pd.DataFrame(df3['metadata'].dropna().to_dict()).transpose()
df4['vid'] = df4['vid'].values.astype('int32')-2
df4

a = df4['vid'].tolist()
a


b = []
for i in range(len(df4['xy'])):
    b.append(df4['xy'][i][1:])
b

c = []
for i in range(len(df4['av'])):
    c.append(df4['av'][i]['1'].split(','))
c

len(a)
len(c)
test = pd.DataFrame([a, c]).transpose() #{'frame': a ,'action': c}
test.columns = [['frame', 'action']]
test

df5 = pd.merge(df,test,how='left').dropna().reset_index(drop=True)
df5


vid = []
frame = []
x1 = []
y1 = []
x2 = []
y2 = []
ac = []
pid = []
for i in range(len(df5)):
    for j in range(len(df5.loc[i]['action'])):
        vid.append(str(df5.loc[i]['videoID']))
        frame.append(df5.loc[i]['frame'])
        x1.append(df5.loc[i]['x1'])
        y1.append(df5.loc[i]['y1'])
        x2.append(df5.loc[i]['x2'])
        y2.append(df5.loc[i]['y2'])
        ac.append(df5.loc[i]['action'][j])
        pid.append(df5.loc[i]['id'])

fdf = pd.DataFrame([vid, frame, x1, y1, x2, y2, ac, pid]).transpose()
fdf.columns = [['videoID', 'Frame', 'x1', 'y1', 'x2', 'y2', 'action', 'id']]
fdf #train/val.csv


df


inx = []
aa = 2
for i in range(m.ceil(len(df)/2)):
    for j in range(2):
        aa = str(aa)
        bb = str(i+2)+'_'+(8-len(aa))*'0'+aa
        inx.append(bb)
        aa = int(aa)+1
len(inx)

vid = [] #frame
flg = []
z = []
xy = []
av = []
for i in range(len(df)):
    x = int(df.loc[i]['x1'])
    y = int(df.loc[i]['y1'])
    w = int(df.loc[i]['x2'])
    h = int(df.loc[i]['y2'])

    x2 = w - x
    y2 = h - y
    vid.append(str(df.loc[i]['frame']))
    flg.append(0)
    z.append([])
    xy.append([2, x, y , x2, y2])
    av.append({'1': '1'})

jsons = pd.DataFrame([vid, flg, z, xy, av]).transpose()
jsons.columns = df4.keys()
jsons.index = (inx)

# %%
jsons
df4
df
# %%
