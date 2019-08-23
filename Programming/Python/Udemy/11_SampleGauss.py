"""
Author: Rodrigo de Barros Vimieiro
Date: August, 2019
rodrigo.vimieiro@gmail.com
=========================================================================
"""
import numpy as np
import matplotlib.pyplot as plt


#%%

mean = 5
std = 10

array = std * np.random.randn(10000) + mean

plt.figure(1)
plt.hist(array,bins=100)





