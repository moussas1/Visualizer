import polygon
import os
import glob


class Frame(object):

 
    def __init__(self, number,polygons,directory):
        """Constructor"""
        self._number = number
        self._polygons = polygons
        self._image = None
        self._directory = directory
 
    def set_new_image(self, directory):
        """Update your polygon"""
        os.chdir(directory)
        for file in glob.glob(create_num(number)+'.png'):

            self._image= file


        
   
    def create_num(number):
        x = str(number)
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