import cv2
import random
import numpy as np
import glob
import sys
import pandas as pd


print('ファイル検索．．．')
csvs1 = glob.glob('Photodata_Msize/data_Msize.csv')
print('検索したファイル', csvs1)


########################################## M Size #########################################
data = []
dataset_list =[]
i = 0
for filepath in csvs1:
	with open(filepath) as f:
		while True:
			s_line = f.readline()
			if not s_line:	
				break
			data = s_line.split(',')
			img = cv2.imread(filepath.replace('data_Msize.csv', '')  + 'cropped' + data[0].zfill(6) + '.jpg')
			#img = cv2.resize(img, dsize =(60,150))
			#data's range M or L size
			if float(data[5]) >= 150 and float(data[5]) < 230 and float(data[4])> 10 and float(data[3])<10:
			#if float(data[5]) >= 230 and float(data[5]) < 350 and float(data[4])> 10 and float(data[3])<10:
				if data[1] == "1" or data[1] == "3":
					row = [img/255.0]
					for j in range(len(data) - 1):
						row.append(int(data[j + 1].strip()))
					dataset_list.append(row)

#二進数に変更
for k in range(len(dataset_list)):
	if dataset_list[k][1] == 1:
		dataset_list[k][1] = 0 			#長手
	if dataset_list[k][1] == 3:
		dataset_list[k][1] = 1 			#短手
#print(dataset_list)

random.shuffle(dataset_list)
convlist = []
for l in range(len(data)):
	tmp = []
	for m in range(len(dataset_list)):
		tmp.append(dataset_list[m][l])
	convlist.append(tmp)
#print(convlist[0])
#print(len(convlist))
#print(dataset_list)
#print(len(data))
#print(len(dataset_list))
#print(i)

np.save(file = 'image_train_Msize.npy', arr = np.array(convlist[0]))
np.save(file = 'info_label_Msize.npy', arr = np.array(convlist[1]))

########################################## L Size #########################################
print('ファイル検索．．．')
csvs2 = glob.glob('Photodata_Lsize/data_Lsize.csv')
print('検索したファイル', csvs2)
data = []
dataset_list =[]
i = 0
for filepath in csvs2:
	with open(filepath) as f:
		while True:
			s_line = f.readline()
			if not s_line:	
				break
			data = s_line.split(',')
			img = cv2.imread(filepath.replace('data_Lsize.csv', '')  + 'cropped' + data[0].zfill(6) + '.jpg')
			#img = cv2.resize(img, dsize =(60,150))
			#data's range M or L size
			#if float(data[5]) >= 150 and float(data[5]) < 230 and float(data[4])> 10 and float(data[3])<10:
			if float(data[5]) >= 230 and float(data[5]) < 350 and float(data[4])> 10 and float(data[3])<10:
				if data[1] == "1" or data[1] == "3":
					row = [img/255.0]
					for j in range(len(data) - 1):
						row.append(int(data[j + 1].strip()))
					dataset_list.append(row)
#二進数に変更
for k in range(len(dataset_list)):
	if dataset_list[k][1] == 1:
		dataset_list[k][1] = 0 			#長手
	if dataset_list[k][1] == 3:
		dataset_list[k][1] = 1 			#短手
#print(dataset_list)

random.shuffle(dataset_list)
convlist = []
for l in range(len(data)):
	tmp = []
	for m in range(len(dataset_list)):
		tmp.append(dataset_list[m][l])
	convlist.append(tmp)
#print(convlist[1])
#print(len(convlist))
#print(dataset_list)
#print(len(data))
#print(len(dataset_list))
#print(i)

np.save(file = 'image_train_Lsize.npy', arr = np.array(convlist[0]))
np.save(file = 'info_label_Lsize.npy', arr = np.array(convlist[1]))

print('処理終了')
