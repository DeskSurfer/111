import os
import shutil

from_dir = "c:/Users/HP/Downloads"
to_dir = "D:/Coding/Class/Projects/111/Docs"

list_of_files = os.listdir(from_dir)

for file_name in list_of_files:
#    print(file_name)
    name, extension = os.path.splitext(file_name)
    print(name , extension)