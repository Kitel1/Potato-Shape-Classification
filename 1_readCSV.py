import cv2
import random
import numpy as np
import glob
import sys
import shutil
import os
import csv
import pandas as pd

data = []
dataset_Msize_list =[]
dataset_Lsize_list =[]

i = 0
x=0
x1=0
x2=0
y=0
y1=0
y2=0

print('ファイル検索．．．')
csvs = glob.glob('Photodata/*/*/data.csv')
print('検索したファイル', csvs)

#
for filepath in csvs:
	with open(filepath) as f:
		while True:
			s_line = f.readline()	
			if not s_line:	
				break
			data = s_line.split(',')
			img = cv2.imread(filepath.replace('data.csv', '')  + 'cropped' + data[0].zfill(6) + '.jpg')
			img = cv2.resize(img, dsize =(60,150))
			#data's range ： M size
			if float(data[5]) >= 150 and float(data[5]) < 230 and float(data[4])> 10 and float(data[3])<10:
				if data[1] == "1" or data[1] == "3":
					#make new data image
					new_filename='cropped' + str(x).zfill(6) + '.jpg'
					os.makedirs('Photodata_Msize', exist_ok=True) 
					output_path ='Photodata_Msize'
					output_file = os.path.join(output_path, new_filename)
					cv2.imwrite(output_file, img)

					datasetlist=[]	
					for j in range(len(data) - 1):
						datasetlist.append(int(data[j + 1].strip()))
					dataset_Msize_list.append(datasetlist)
					x+=1
				

				if data[1] == "1":	#長手
					x1+=1
				if data[1] == "3":	#短手
					x2+=1
			#data's range ： L size							
			elif float(data[5]) >= 230 and float(data[5]) < 350 and float(data[4])> 10 and float(data[3])<10:
				if data[1] == "1" or data[1] == "3":
					
					new_filename='cropped' + str(y).zfill(6) + '.jpg'
					os.makedirs('Photodata_Lsize', exist_ok=True) 
					output_path ='Photodata_Lsize'
					output_file = os.path.join(output_path, new_filename)
					cv2.imwrite(output_file, img)
				
					
					datasetlist=[]
					for j in range(len(data) - 1):
						datasetlist.append(int(data[j + 1].strip()))
					dataset_Lsize_list.append(datasetlist)
					y+=1

				if data[1] == "1":
					y1+=1
				if data[1] == "3":
					y2+=1
						
			
			i += 1

a=0
b=0
for filepath in csvs:
	with open(filepath) as f:
		while True:
			s_line = f.readline()
			if not s_line:	
				break
			data = s_line.split(',')
			img = cv2.imread(filepath.replace('data.csv', '')  + 'cropped' + data[0].zfill(6) + '.jpg')
			img = cv2.resize(img, dsize =(60,150))
			#data's range : M size
			if float(data[5]) >= 150 and float(data[5]) < 230 and float(data[4])> 10 and float(data[3])<10:
				if data[1] == "3":
					
					if a < (x1-x2):
						#make new data image
						img=cv2.flip(img,-1) 	#Flipped horizontally and vertically
						new_filename='cropped' + str(x + a).zfill(6) + '.jpg'
						output_path ='Photodata_Msize'
						output_file = os.path.join(output_path, new_filename)
						cv2.imwrite(output_file, img)

						
						datasetlist=[]
						for j in range(len(data) - 1):
							datasetlist.append(int(data[j + 1].strip()))
						dataset_Msize_list.append(datasetlist)
					a+=1

			#data's range : L size							
			elif float(data[5]) >= 230 and float(data[5]) < 350 and float(data[4])> 10 and float(data[3])<10:
				
				if data[1] == "3":
					
					if b<(y1-y2):	
						#make new data
						img=cv2.flip(img,-1) 	#Flipped horizontally and vertically
						new_filename='cropped' + str(y + b).zfill(6) + '.jpg'
						output_path ='Photodata_Lsize'
						output_file = os.path.join(output_path, new_filename)	
						cv2.imwrite(output_file, img)

						datasetlist=[]
						for j in range(len(data) - 1):
							datasetlist.append(int(data[j + 1].strip()))
						dataset_Lsize_list.append(datasetlist)
					b+=1


df = pd.DataFrame(dataset_Msize_list)

df.to_csv('Photodata_Msize/data_Msize.csv')

df = pd.DataFrame(dataset_Lsize_list)

df.to_csv('Photodata_Lsize/data_Lsize.csv')

print(len(data))

print(i)
print('M:',x,'nagate:',x1,'mijikate:',x2, ' + ',(x1-x2))
print('L:',y,'nagate:',y1,'mijikate:',y2, ' + ',(y1-y2))

