class DiskManager(object):
    
    def __init__(self):
        pass 
    
    def setCommand(self, command):
        self.command = command
        
    def runCommand(self):
        yield self.command.execute();