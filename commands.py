from interfaces import Command; 

#Null Placeholder
#Tested
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
    
#No tested
class explore(Command):
    
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

#No tested
class open(Command):
    
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

#No tested
class write(Command):
    
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

#No tested
class delete(Command):
    
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

#No tested
class find(Command):
    
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

#No tested
class rename(Command):
    
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

#No tested
class zip(Command):
    
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

#Should behave like Linux-grep
class grep(Command):
    pass 

#No tested
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
#No tested
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