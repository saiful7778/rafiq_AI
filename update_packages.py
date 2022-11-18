import os, shutil
import time
from essential_function import dirlocation

rootdir = os.path.join(dirlocation(),"venv\\Lib\\site-packages")
rootpackage = ['main_function-0.0.0-py3.8.egg','features_function-0.0.0-py3.8.egg','essential_function-0.0.0-py3.8.egg','browser_control-0.0.0-py3.8.egg']
localdir = os.path.join(dirlocation(),"database")
localpackage = ['main_function.egg-info','features_function.egg-info','essential_function.egg-info','browser_control.egg-info','dist','build']

print("Enter the numder and press enter to execute command: \n \t1. Update all local packages \n \t2. Run training module \n \t3. Execute the both command")
userInput = int(input("\n \t>>>  "))

def updateAllpackage():
    # delete root folder package
    for package in rootpackage:
        allpackages = rootdir+"\\"+package
        if os.path.isfile(allpackages):
            os.remove(allpackages)
            print("File in deleted")
        else:
            print("File does not exist")
    # delete folder package
    for sublocalpackage in localpackage:
        allsubpackage = localdir+"\\"+sublocalpackage
        if os.path.isdir(allsubpackage):
            shutil.rmtree(allsubpackage)
            print("File in deleted")
        else:
            print("File does not exist")
    # install all package
    try:
        os.system('cmd /C "cd database & timeout 1 & python setup.py install"')
    except:
        pass
    print("         ")
    print("         ")
    print("Work is done")
    
def updatetrainfile():
    # delete trainning file
    filename = os.path.join(dirlocation(),"TrainData.pth")
    if os.path.isfile(filename):
        os.remove(filename)
        print("File in deleted")
    else:
        print("File does not exist")
    # run the tranning file
    try:
        os.system('cmd /C "cd database/main_function & timeout 1 & python train.py"')
    except:
        pass
    print("         ")
    print("         ")
    print("Work is done")

if userInput == 1:
    updateAllpackage()
elif userInput == 2:
    updatetrainfile()
elif userInput == 3:
    updateAllpackage()
    updatetrainfile()
else:
    pass