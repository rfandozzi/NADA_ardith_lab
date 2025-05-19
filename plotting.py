import matplotlib
import os

matplotlib.use('Agg')       # to avoid warnings if using ssh
import matplotlib.pyplot as plt

with open('/Users/burtmacklinslaptop/onedrive/lab_etc/NH3H2O/11-10-2006/nAHu0212.spa.txt', "r") as f:
    data = f.readlines()[1:]  #skip the first row


wavenumber=[]
absorbance=[]

for dat in data:
    values = dat.split()  
    wavenumber.append(float(values[0]))  
    absorbance.append(float(values[1]))    

plt.plot(wavenumber[0:len(wavenumber)], absorbance[0:len(wavenumber)])
plt.grid(True)
plt.xlabel("wavenumber")
plt.ylabel("absorabnce")
plt.savefig(f'trial.png')