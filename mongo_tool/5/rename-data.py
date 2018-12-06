import subprocess

import os
path = '/home/administrator/mongodb'
dir = next(os.walk(path))[1]
for folder in dir:
    folder_path = str(os.path.join(path,folder))
    print(folder_path)
    for file in next(os.walk(folder_path))[1]:
        if 'data'==file:
            base_data_path = "%s/data/"%folder_path
            other_data_path = "%s/data1/"%folder_path
            print(base_data_path)
            print(other_data_path)
            process = subprocess.Popen("sudo -S mv %s %s && mkdir %s" %(base_data_path,other_data_path,base_data_path),
                                       stdin=subprocess.PIPE, stderr=subprocess.PIPE, stdout=subprocess.PIPE,
                                       universal_newlines=True, shell=True)
            stdout, stderr = process.communicate('dy781002!@#' + "\n")





