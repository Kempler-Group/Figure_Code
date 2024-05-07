# -*- coding: utf-8 -*-
"""
Created on Mon May  6 10:28:59 2024

@author: isaac
"""

import pandas as pd
import numpy as np  # Numpy is a useful module for scientific computing (similar language to MATLAB)
import matplotlib.pyplot as plt  # import the module for plotting data
import math  # import the module containing mathematical functions
from matplotlib.ticker import (MultipleLocator, AutoMinorLocator)     # Configure tick location and format
import matplotlib.pylab as pylab #for qol features, in this case text size manipulation
#Make sure to replace my file path with your own.
#same general layout as XRD grapher. Make sure to replace my file path with your own.


def Tafel_Grapher(const #Normalizing constant to turn current input into current density output if desired
               ,filenames,title,xlimits,yunits,ylimits,Ru,vs,pboundsV,pboundsj): #Ru in Ohms, Y data in mA, vs is correction for overpotential
    fig = plt.figure(figsize=(8, 6))    # Create a graph 'fig' which has 4 inches in width and 6 inches in height.
    ax = fig.add_subplot(111)           # Create a subplot 'ax' in the figure 'fig'. 
    ax.set_ylabel('Overpotential (V)')   # set the label of the x-axis
    ax.set_xlabel('log|j| (' + yunits + ')') # set the label of the y-axis
    
    params={'axes.labelsize': 'xx-large',   #set text size
         'axes.titlesize':'xx-large',
         'xtick.labelsize':'xx-large',
         'ytick.labelsize':'xx-large',
         'legend.fontsize':'xx-large'}
    pylab.rcParams.update(params)
    
    X1 = []
    X2 = []
    X3 = []
    X4 = []
    Y1 = []
    Y2 = []
    Y3 = []
    Y4 = []
    colorlist=['g','b','r','y']
    datalistX=[X1,X2,X3,X4]
    datalistY=[Y1,Y2,Y3,Y4]
    i=0
    while(i < len(filenames)):
        datalistX[i],datalistY[i]=np.loadtxt(fname=r"C:\Users\isaac\OneDrive\Documents\aluminum substituted hematite reduction project\Electrochemical tests\txt files\5_1 and 5_2 CVs"+"/" + filenames[i]+'.txt', #delimiter = ',', 
                                             skiprows=1, unpack=True,
                   usecols=(0,1))
                     # Read data from a file scan1.csv and skip the first row.  
        #ax.plot(datalistX[i], datalistY[i]/const, '.', color=colorlist[i],label=filenames[i])
        i=i+1
        
    V_corrected = datalistX
    logi = datalistY
    
    i = 0
    
    while(i < len(datalistX)):
        
        n = 0
        
        while(n < len(datalistX[i])):
            V_corrected[i][n] = datalistX[i][n] - datalistY[i][n]*Ru/1000 + vs
            logi[i][n] = np.log(np.abs(datalistY[i][n]/1000)/const)
            n = n + 1
            
        ax.plot(logi[i], (V_corrected[i]), '.', color=colorlist[i],
                label=filenames[i])
        if datalistX[i+1] != []:
            i = i + 1
        else:
            i = len(datalistX)
     
    i = 0
    
    x = []
    y = []
    
    while(i < len(V_corrected[0])):
        if V_corrected[0][i] > pboundsV[0] and V_corrected[0][i] < pboundsV[1]:
            if pboundsj == None:
                y = np.append(y,V_corrected[0][i])
                x = np.append(x,logi[0][i])
            elif logi[0][i] > pboundsj[0] and logi[0][i] < pboundsj[1]:
                y = np.append(y,V_corrected[0][i])
                x = np.append(x,logi[0][i])
        i = i + 1
    
    z = np.polyfit(x,y,1)
    
    xp = np.linspace(-10,10,10000)
    
    zp = xp*z[0] + z[1]
    
    ax.plot(xp, zp, '--', color = 'b', label = 'Tafel line')
    
    if xlimits != None:
        ax.set_xlim(xlimits[0],xlimits[1])   # set the range of the x-axis of plot 'ax'
    if ylimits != None:
        ax.set_ylim(ylimits[0],ylimits[1])   # set the range of the y-axis
    #ax.set_xlabel('Potential, V')   # set the label of the x-axis
    #ax.set_ylabel('Current, mA/cm^2') # set the label of the y-axis
    ax.legend(loc='lower right')       # place the legend at the 'upper left'
    ax.xaxis.set_minor_locator(MultipleLocator(10))   # add minor ticks for the x-axis
    ax.yaxis.set_minor_locator(AutoMinorLocator())    # add minor ticks for the y-axis
    ax.xaxis.grid(True, which='both') # add grids to the x-axis for both major and minor ticks
    ax.set_title(title)

    plt.show()   # display 'ax'
    return z