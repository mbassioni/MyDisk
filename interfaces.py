from abc import ABCMeta, abstractmethod

class Command(object):
    
    __metaclass__ = ABCMeta;
    
    @abstractmethod
    def execute(self):
        pass 
    
    @abstractmethod
    def cancel(self):
        pass 
    
    @abstractmethod
    def undo(self):
        pass 
    
    @abstractmethod
    def redo(self):
        pass