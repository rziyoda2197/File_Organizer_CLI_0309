import os
import shutil

folder = input("Folder path: ")

for file in os.listdir(folder):
    path = os.path.join(folder,file)

    if os.path.isfile(path):
        ext = file.split(".")[-1]

        new_folder = os.path.join(folder,ext)

        os.makedirs(new_folder,exist_ok=True)

        shutil.move(path,os.path.join(new_folder,file))
