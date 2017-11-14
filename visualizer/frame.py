import polygon
import os
import glob
import cv2 as cv
import numpy as np 


class Frame(object):

 
    def __init__(self, number,polygons):
        """Constructor"""
        self._number = number
        self._polygons = polygons
        self._image = None
        self._directory = None


    
    def set_directory(self):
        cwd = os.getcwd()
        directory = cwd + '/frames'
        

        return directory

 
    def set_new_image(self):
        """Update your polygon"""

        directory = set_directory()
        os.chdir(directory)
        for file in glob.glob(create_num(number)+'.png'):

            self._image= file

            return _image



        
   
    def create_num(number):
        x = str(number+1)
        leng = len(x)
        y = 0
        while(y<(6-leng)):
            x = '0' + x
            y+=1
        return x    


    def get_image(self):
        return self._image
   
    #def add_polygon(self,polygon):
        #self._polygons.append(polygon)

    def get_polygons(self):
        return self._polygons


    def plot(polygons,number):
        img = cv.imread(set_new_image(),1)
        for poly in polygons.get_polygons():
            pts = np.array(poly.get_values(), np.int32)
            pts = pts.reshape(-1,1,2)
            cv.polylines(img,[pts],True,poly.get_color())



