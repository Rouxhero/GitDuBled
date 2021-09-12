from Function import *
from tkinter.filedialog import *

clear()

print("""
  #####                 ######               ######                          
 #     #  #  #####      #     #  #    #      #     #  #       ######  #####  
 #        #    #        #     #  #    #      #     #  #       #       #    # 
 #  ####  #    #        #     #  #    #      ######   #       #####   #    # 
 #     #  #    #        #     #  #    #      #     #  #       #       #    # 
 #     #  #    #        #     #  #    #      #     #  #       #       #    # 
  #####   #    #        ######    ####       ######   ######  ######  #####  

""")



def helps():
  pass

def startWatcher():
  path = askdirectory() 


command = {
  "help":helps,
  "startWatch":startWatcher
}
