import os
import sys

leng = len(sys.argv)

if leng < 3:
    print("Not enough aruments!")
else:
    files = [f for f in os.listdir(sys.argv[1]) if os.path.isfile(os.path.join(sys.argv[1], f))]
    print(files)
    print(files[0].find("R"))
    i = 0
    
    name = sys.argv[2]
    print(len(name))
    for char in name:
        if char != "*":
            for j in range(i+1, len(name)):
                if name[j] != "*":
                    # break
                    for f in files:
                        if f.find(name[i+1:j]) < 0:
                            print(f)
                            files.remove(f)
        i += 1
    print(files)