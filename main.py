import visualizer
import csv 
import pandas as pd 
import numpy as np 
import sys



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


def polygon_gen(data_frame,color_list):
	
	size = data_frame.shape[0]
	size = size -1
	index = 1
	poly_list = []
	
	 while(index <= size):
	    frame_num = data_frame.ix[index,1]
	    temp = data_frame.ix[index,3:]
	    polygon_values = temp.dropna().tolist()
	    it = iter(polygon_values)
	    zip(it,it)
	    name = data_frame.ix[index,2]
	    poly = polygon.Polygon(name,frame_num)
	    poly.set_color(color_list.get(name))
	    poly.set_new_values(polygon_values)
	    poly_list.append(poly)
	    index = index+1

	return poly_list

def frame_gen(polygons):
	index = 0 
	for items in polygons:

