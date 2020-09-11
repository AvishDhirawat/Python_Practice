#!/usr/bin/env python3

import os
import shutil

folername = input("Enter folder from which you want to extract the files : ")
curr_path = os.getcwd()
next_path = os.getcwd()+"/"+folername
if os.path.exists(next_path):

    print("Destination Path : ", curr_path)
    print("Source Path : ", next_path)
    number = 0
    for file in os.listdir(next_path):
        if(file.endswith(".py")):
            shutil.move(str(next_path) + "/" + file, str(curr_path) + "/" + file)
            #print(file)
            number = number + 1
    print("[+] {} Files Moved".format(number))
else:
    print("Path doesn't exists")
