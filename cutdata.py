# -*- coding: utf-8 -*-
"""
@author: hzy
"""

import pickle
import matplotlib.pyplot as plt

import numpy as np
with open("E:\keras\RML2016.10a_dict.dat",'rb') as xd1:

    Xd = pickle.load(xd1,encoding='latin1')
snrs,mods = map(lambda j: sorted(list(set(map(lambda x: x[j], Xd.keys())))), [1,0])
X = []  
lbl = []
for mod in mods:
    for snr in snrs:
        X.append(Xd[(mod,snr)])
        for i in range(Xd[(mod,snr)].shape[0]):  lbl.append((mod,snr))
X = np.vstack(X)
#%%
q = 11000 #在22000个样本中随机选取一片
y = X[q,0,:]
z = X[q,1,:]
x = np.linspace(1,128,128)

plt.plot(x,y,label="$sin(x)$",color="red",linewidth=2)
plt.plot(x,z,label="$cos(x^2)$",color="blue")
plt.show()