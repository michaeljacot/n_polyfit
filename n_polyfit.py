# -*- coding: utf-8 -*-
"""
Created on Fri Jan  1 15:42:34 2021

@author: Michael


take in a dataset of closes, run polyfit on it with n = 1-10. See what it looks like

edit: i forgot that polyfit doesnt return the actual plottable numbers, it returns the coeffs for the respective polynomial. Good thing numpy
has a sick function polyval that does that for you.


"""


import yfinance as yf
import matplotlib.pyplot as plt
import numpy as np
import random 

data = random.sample(range(10, 300), 100)

time = np.arange(0,len(data))


plt.plot(data)
plt.title("Raw")
plt.show()





#loop through each value for n and run polyfit with that value of n
for i in range(1,25):
    
    thisPoly = np.polyfit(time,data,i)
    thisPoly = np.polyval(thisPoly,time)
    
    plt.plot(thisPoly)
    plt.title("Polyfit where n =" + str(i))
    plt.show()
    
    
    