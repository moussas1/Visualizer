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



