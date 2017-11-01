 
class Polygon(object):
 
    def __init__(self, name, initial_values):
        """Constructor"""
        self._name = name
        self._values = initial_values
 
    def set_new_values(self, new_values):
        """Update your polygon"""
        self._values = new_values
   
    def get_values(self):
        """just a getter"""
        return self._values