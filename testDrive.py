from disk_manager import DiskManager; 
from commands import cat, ls
from document import  File; 
from path import Path; 

if __name__ == "__main__":
	#Create a disk instance
	disk = DiskManager()
	#Create a command object instance
	path = Path('c:\sandbox')
	#Define our command
	cmd = ls(path);
	#set & call our command
	disk.setCommand(cmd)
	for d in disk.runCommand():
	    print d;


	# In[130]:

	#define our command Object (File)
	fileObj = File('c:\sandbox\ipconfig.txt')
	cmd = cat(fileObj)
	disk.setCommand(cmd)
	for line in disk.runCommand():
	    print line

