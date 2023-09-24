import os
import sys
from pathlib import Path

#function for argument check

def check_args(args):
    if len(args) < 2:
        print("Please provide the application name to start")
        return False
    elif args[1] == "--help":
        print(" --- here's an example of it python TorStart.py <application name> ---  ")
        return False
       
    else:
        return True


#add the new path of the file here!

TOR_PATH = "AZ/tor-browser-linux64-12.5.4_ALL/tor-browser"



#function for starting the application
def startTor():
    #print(Path.home())
    os.chdir(Path.home().joinpath(f"{TOR_PATH}"))
    
    FinalPath = Path.cwd()
    #print(FinalPath)
    os.system(f"{FinalPath}/start-tor-browser.desktop")




if __name__ == "__main__":
    print("to start any new application write the name of the application after the command TorStart.py in smallcase"
            "for helps use --help as a flag"
          )
#get the arguments provided
    current_args = sys.argv
    #print(current_args)

#start the application
    if check_args(current_args):
        name = current_args[1]
        print('starting the application ',name)
        startTor()
        sys.exit(1)
    
#end it
    else:
        raise Exception("please provide the application name to start")
        
    



    