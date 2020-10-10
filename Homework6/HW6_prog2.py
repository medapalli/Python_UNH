import os
import json
import shutil

PARENT_DIR = "quotes_output"

with open("quotes1.json") as quotes_file:
    data=json.load(quotes_file)

#if the parent directory already there, we will delete it
if os.path.exists(PARENT_DIR):
    shutil.rmtree(PARENT_DIR)

    
os.mkdir(PARENT_DIR) #parent directory
os.chdir(PARENT_DIR)
print("Parent directory created",PARENT_DIR)

for node in data:
    corrected_author=node["author"] if node["author"] is not None else "Unknown"
    dir_name=corrected_author.replace(" ","_")
    if not os.path.exists(dir_name):
        os.mkdir(dir_name)
        out=open(("quote.txt"),"w")
        out.write(node["text"])
        out.close()
    else:
        i=1
        out=open(("quote"+ str(i) +".txt"),"w")
        out.write(node["text"])
        i=i+1
        out.close()
       
          
        


    
