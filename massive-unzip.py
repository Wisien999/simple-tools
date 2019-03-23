from os import listdir
from os.path import isfile, join
import zipfile
import os
import sys


def unzip_and_delate(file):
    zip_ref = zipfile.ZipFile(file, 'r')
    zip_ref.extractall(eTo)
    zip_ref.close()
    os.remove(file)


leng = len(sys.argv)

if leng > 2:
    eFrom = sys.argv[1]
    eTo = sys.argv[2]
elif leng == 2:
    eFrom = sys.argv[1]
    eTo = sys.argv[1]
else:
    eFrom = os.getcwd()
    eTo = os.getcwd()

print("from:", eFrom)
print("to:", eTo)

for f in listdir(eFrom):
    filepath = join(eFrom, f)
    if isfile(filepath) and filepath.endswith(".zip"):
        print(f)
        unzip_and_delate(f)