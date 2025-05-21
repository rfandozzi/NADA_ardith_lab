import os
import pandas as pd

import matplotlib
matplotlib.use('Agg')  # for SSH or headless environments
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
            os.makedirs(txt_output_folder, exist_ok=True)
            os.makedirs(plot_output_folder, exist_ok=True)

            target_txt_path = os.path.join(txt_output_folder, file + '.txt')
            os.rename(raw_txt_path, target_txt_path)
            
            with open(target_txt_path, "r") as f:
                lines = f.readlines()[1:]  #skipping header
            wavenumber = []
            absorbance = []
            
            for line in lines:
                data=line.strip().split()
                wavenumber.append(float(data[0]))
                absorbance.append(float(data[1]))

            plt.figure()
            plt.plot(wavenumber, absorbance)
            plt.grid(True)
            plt.xlabel("Wavenumber")
            plt.ylabel("Absorbance")
            plt.title(file)
            plot_path = os.path.join(plot_output_folder, file + '.png')
            plt.savefig(plot_path)
            plt.close()

