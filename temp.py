import numpy as np
from matplotlib import pyplot as pp

# 1) open file
# 2) read file 
# 3) close file

filename = 'fism_201709.dat'
f = open(filename,'r')

f.readline()
date = [] 
flux = [] 
for line in f: 
    temp = line.split()
    date.append([int(t) for t in temp[0:6]])
    flux.append([float(t) for t in temp[6:]])
    breakpoint()
f.close()
flux = np.array(flux)
pp.plot(flux[:,56])
pp.show()
