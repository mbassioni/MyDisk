from abc import ABCMeta, abstractmethod
import os; 


class Document(object):
    
    __metaclass__ = ABCMeta
    pass 

class File(Document):
    
    def __init__(self, filename=None):
        self.filename = filename; 
    
    def read(self):
        try:
            with open(self.filename, 'r') as f:
                return f.readlines()
        except Exception as e: 
            print "Errors opening %s" %self.filename
            print e;
