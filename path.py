import os;

class Path(object):
    
    @property
    def __path__(self):
        return self._path_value; 
    
    @__path__.setter
    def __path__(self, value=None):
        self._path_value = value;
        
    def __init__(self, dir=None):
        self.__path__ = dir; 
        
    def ls(self):
        if not isinstance(self.__path__, type(None)):
            return os.listdir(self.__path__)
            
    