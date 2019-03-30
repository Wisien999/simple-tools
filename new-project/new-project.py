import os
import sys
from distutils.dir_util import copy_tree

leng = len(sys.argv)

if leng < 3:
    print("Error: Not enough arguments!")
    exit()
elif leng == 3:
    temp = sys.argv[2].split("/")
    patternsPath = os.path.join(os.path.dirname(os.path.realpath(__file__)), "patterns/")
    if len(temp) == 1:
        projectName = temp[0]
        projectDir = os.path.expanduser("~/Dokumenty/Coding/")
        print("Project location", projectDir)
        print("Project name:", projectName)
    elif temp[0] == ".":
        projectName = temp[-1]
        temp.pop(0)
        temp.pop()
        projectDir = os.getcwd() + "/" + "/".join(temp)
        print("Project location", projectDir)
        print("Project name:", projectName)
    else:
        projectName = temp[-1]
        if temp[0] == "":
            temp.pop(0)
        temp.pop()
        projectDir = os.path.expanduser("~/Dokumenty/Coding/") + "/".join(temp)
        print("Project location", projectDir)
        print("Project name:", projectName)

if sys.argv[1].lower() == "cpp" or sys.argv[1].lower() == "c++":
    copy_tree(patternsPath + "/cpp/", os.path.join(projectDir, projectName))

