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

    def set_new_image(self):
        """Update your polygon"""  
        directory = os.getcwd() + '/frames'
        self._image = '%s/%s.png' % (directory, self.create_num(self._number))
        return self._image
   
    def create_num(self, number):
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

    def plot(self):
        image_file = self.set_new_image()
        img = cv.imread(image_file,1)
        for poly in self._polygons:
            pts = np.array(poly.get_values(), np.int32)
            pts = pts.reshape(-1,1,2)
            cv.polylines(img,[pts],True,(255,255,255))
        
        cv.imwrite(image_file, img)


