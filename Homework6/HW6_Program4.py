import os
import fnmatch

start_dir = "C:\Python_UNH\Assignment"


for dirpath, dirs, files in os.walk(start_dir):
    for single_file in files:
        if fnmatch.fnmatch(single_file, "test31.txt"):
            fileNamePath = str(os.path.join(dirpath,single_file))
            print("Full directry path of file is\n")
            print(fileNamePath)



