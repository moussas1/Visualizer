 
class Polygon(object):
 
    def __init__(self, name, frame_number):
        """Constructor"""
        self._name = name
        self._values = None
        self._color = None 
        self._frame = frame_number
 
    def set_new_values(self, new_values):
        """Update your polygon"""
        self._values = new_values
   
    def get_values(self):
        """just a getter"""
        return self._values

    def set_color(self,color):

        self._color = color

    def get_color(self):

        return self._color

    def get_frame(self):

        return self._frame


