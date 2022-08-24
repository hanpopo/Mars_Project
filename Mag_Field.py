# -*- coding: utf-8 -*-
"""
Created on Mon 15 at 12:38:17 2022

@author: hpopo
"""

import numpy as np
from matplotlib import pyplot as pp
#dipole values

filename = "MHDGEO_20150618_002000.dat"
f = open(filename, "r")

f.readline()
f.readline()
long = []
lat = []
alt = []
b_up = []
b_north = []
b_east = []
for line in f:
  f_new = line.split()
  long.append(float(f_new[0]))
  lat.append(float(f_new[1]))
  alt.append(int(f_new[2]))
  b_up.append(float(f_new[3]))
  b_north.append(float(f_new[4]))
  b_east.append(float(f_new[5]))

b_up = np.array(b_up)
b_north = np.array((b_north))
b_east = np.array((b_east))
#b_total = np.zeros((len(b_east), len(b_north), len(b_up)))


alt2 = list(set(alt))
alt2.sort()
print("{}".format(alt2))

user_alt = input("Choose an Altitude:")

if int(user_alt) in alt[:]:
    print('Value Accepted')
    pp.contourf((long, lat, b_up), levels = 25)

else:
    print("Invalid Altitude")
    
pp.xlabel("Longitude")
pp.ylabel("Latitude")
pp.title("B_Up with Respect to Longitude and Latitude")
pp.show


   
f.close()

    
        

