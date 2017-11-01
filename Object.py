 
class Object(object):
 
    def __init__(self, name, nid):
        
        self._name = name
        self._nid = nid
  

    def get_name(self):
    	return self._name


   def get_nid(self):
    	return self._nid 
   