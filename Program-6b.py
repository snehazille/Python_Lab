#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import sys
import pathlib
import zipfile

dirName = input("Enter Directory name that you want to backup: ")

if not os.path.isdir(dirName):
    print("Directory", dirName, "doesn't exist")
    sys.exit(1)

curDirectory = pathlib.Path(dirName)

with zipfile.ZipFile("myZip.zip", mode="w", compression=zipfile.ZIP_DEFLATED) as archive:
    for file_path in curDirectory.rglob("*"):
        archive.write(file_path, arcname=file_path.relative_to(curDirectory))

if os.path.isfile("myZip.zip"):
    print("Archive myZip.zip created successfully")
else:
    print("Error in creating zip archive")


# In[ ]:




