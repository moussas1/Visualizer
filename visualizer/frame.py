import polygon

class Frame(object):

 
    def __init__(self, number):
        """Constructor"""
        self._number = number
        self._polygons = []
        self._image = None
 
    def set_new_image(self, image):
        """Update your polygon"""
        self._image=image
   
    def get_image(self):
        return self._image
   
    def add_polygon(self,polygon):
        self._polygons.append(polygon)

    def get_polygons(self):
        return self._polygons    