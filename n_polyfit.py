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

def getData(stock,domain,window):
    
    tick = yf.Ticker(stock)
    data = tick.history(period = domain,interval = window)
    closes = data.Close.tolist()
    
    return closes,data



stock = "BTC-USD"
domain = "2y"
window = "1d"

closes,data = getData(stock,domain,window)
time = np.arange(0,len(closes))


plt.plot(closes)
plt.title(stock + " over the last " + domain + " using closes every " + window)
plt.show()




#loop through each value for n and run polyfit with that value of n
for i in range(1,25):
    
    thisPoly = np.polyfit(time,closes,i)
    thisPoly = np.polyval(thisPoly,time)
    
    plt.plot(thisPoly)
    plt.title("Polyfit where n =" + str(i))
    plt.show()
    
    
    