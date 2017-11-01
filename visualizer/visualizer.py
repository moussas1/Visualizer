
import sys
import matplotlib.pyplot as plt
from scipy.misc import imread
import os
import numpy as np
import csv
import pandas as pd 
import random
from Polygon import Polygon 
from Frame import Frame




video_file = sys.argv[1]
visual_csv = sys.argv[2]
output_vid = sys.argv[3]


#Get current directory
cwd = os.getcwd()

#make new directory
image_directory = cwd+ '/' + video_file

if not os.path.exists(image_directory):
    os.makedirs(image_directory)

#split video into frames using ffmpeg
subprocess.call('ffmpeg -i ' + video_file+ '-q:v 1' + image_directory+ 'output_%06d.png')
print "extracting frames"

#read the visualizing csv

#with open(visual_csv, 'r') as f:
	#stock = list(csv.reader(f, delimiter = ','))

#to get max rows

def gen_rows(stream, max_length=None):
      rows = csv.reader(stream)
      if max_length is None:
          rows = list(rows)
          max_length = max(len(row) for row in rows)
      for row in rows:
          yield row + [None] * (max_length - len(row))


#load csv into pandas datafram
with open(visual_csv) as f:
     df = pd.DataFrame.from_records(list(gen_rows(f)))

#create list for object ids
object_list = []
object_list = df.ix[1:,2].tolist()
object_list = set(object_list)

#random hex color creator
def gen_hex_colour_code():
   return ''.join([random.choice('0123456789ABCDEF') for x in range(6)])


#create dictionary with object ids and color codes
color_dict = {}   

for objs in object_list:
	color_dict[objs] = '#' + gen_hex_colour_code()





points  = [[300,400],[500,800],[600,500]]
img  = imread('2.jpg')
polygon = plt.Polygon(points)
plt.gca().add_patch(polygon)
plt.Polygon(points,zorder=1, fill = None, edgecolor = 'r')
plt.gca().add_patch(polygon)
plt.imshow(img, zorder=0)
plt.show()
