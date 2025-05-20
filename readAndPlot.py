import os
import pandas as pd
import matplotlib.pyplot as plt
import subprocess

#configuring where the directories are
spa_path='./spa2txt/build/spa2txt'
main_folder='/Users/burtmacklinslaptop/onedrive/lab_etc/NH3H2O'
output_folder=os.path.join(main_folder,'converted')
plot_folder=os.path.join(main_folder,'plots')


#root is current folder, dirs is list of subdirs in root, files is list of files in cur root
for root,dirs,files in os.walk(main_folder):
    for file in files:
        if file.endswith('.spa'):
            full_spafile_path=os.path.join(root,file)
            #running an external command for the spa2txt github, stdout is normal output and stderr is errors
            result=subprocess.run([spa_path,full_spafile_path],capture_output=True)

            raw_txt_path=full_spafile_path + '.txt'
            #keep track of where this file is in folder tree
            rel_subfolder=os.path.relpath(root,main_folder)

            txt_output_folder=os.path.join(output_folder,rel_subfolder)
            plot_output_folder=os.path.join(plot_folder,rel_subfolder)


            #creating the subfolders in the directories
            os.makedirs(output_folder, exist_ok=True)
            os.makedirs(plot_folder, exist_ok=True)