from interfaces import Command; 

#Null Placeholder
class noCommand(Command):
    
    def __init__(self):
        pass 
    
    def execute(self):
        pass 
        
    def cancel(self):
        pass 
    
    def undo(self):
        pass 
    
    def redo(self):
        pass 
    
class cat(Command):
    pass 

class ls(Command):
    
    def __init__(self, path):
        self.path = path; 
    
    def execute(self):
        return self.path.ls()
        
    def cancel(self):
        pass 
    
    def undo(self):
        pass 
    
    def redo(self):
        pass 
    
#Read one or more files;
class cat(Command):
    
    def __init__(self, doc):
        self.doc = doc;
    
    def execute(self):
        return self.doc.read()
        
    def cancel(self):
        pass 
    
    def undo(self):
        pass 
    
    def redo(self):
        pass 