# -*- coding: utf-8 -*-
"""
Created on Sat Aug 10 21:53:52 2024

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



def Custom_grapher(filenames,title,xlimits,ylimits,txt,legend,gridlines,xlabel,ylabel1,ylabel2,customDelimiter,xcolumn,ycolumn1,ycolumn2): #txt is true if dealing with a txt file, and false if dealing with a csv
    #xlimits and ylimits set custom limits. Set to None if you want autoscaling.
    #legend is True if there is a legend.
    #gridlines is True if there are gridlines
    #xcolumn and ycolumn specify the columns which hold the relevant data
    
    params={'axes.labelsize': 'xx-large',   #set text size
         'axes.titlesize':'xx-large',
         'xtick.labelsize':'xx-large',
         'ytick.labelsize':'xx-large',
         'legend.fontsize':'xx-large'}
    pylab.rcParams.update(params)

    fig = plt.figure(figsize=(8, 6))    # Create a graph 'fig' which has 4 inches in width and 6 inches in height.
    ax = fig.add_subplot(111)           # Create a subplot 'ax' in the figure 'fig'. 

    ax.set_ylabel(ylabel1,color='green')   # set the label of the x-axis
    ax.set_xlabel(xlabel) # set the label of the y-axis
    
    X1 = []
    X2 = []
    X3 = []
    X4 = []
    X5 = []
    X6 = []
    X7 = []
    X8 = []
    X9 = []
    X10 = []
    X11 = []
    Y1 = []
    Y2 = []
    Y3 = []
    Y4 = []
    Y5 = []
    Y6 = []
    Y7 = []
    Y8 = []
    Y9 = []
    Y10 = []
    Y11 = []
    C1 = []
    C2 = []
    C3 = []
    C4 = []
    C5 = []
    C6 = []
    C7 = []
    C8 = []
    C9 = []
    C10 = []
    C11 = []
    colorlist=['g','b','r','y','k','c','m']
    datalistX=[X1,X2,X3,X4,X5,X6,X7,X8,X9,X10,X11]
    datalistY1=[Y1,Y2,Y3,Y4,Y5,Y6,Y7,Y8,Y9,Y10,Y11]
    datalistY2=[C1,C2,C3,C4,C5,C6,C7,C8,C9,C10,C11]
    i=0
    while(i < len(filenames)):
        if txt == False:
            datalistX[i],datalistY1[i],datalistY2[i]=np.loadtxt(fname="C:/Users/isaac/OneDrive/Documents/Electrochemistry Program/Lab 2/Project 1/Week 2/" + filenames[i] + ".csv", skiprows=1, unpack=True,delimiter=',',
                                                     usecols=(0,1,2))

        elif txt == True:
            datalistX[i],datalistY1[i],datalistY2[i]=np.loadtxt(fname=r"C:\Users\isaac\OneDrive\Documents\aluminum substituted hematite reduction project\Electrochemical tests\custom_txt\8_5"+'/' + filenames[i] + ".txt", skiprows=1, unpack=True,delimiter=customDelimiter
                ,usecols=(xcolumn,ycolumn1,ycolumn2))
            
        ax.plot(datalistX[i], datalistY1[i], '.', color=colorlist[i],label=filenames[i])
        ax2 =ax.twinx()
        ax2.plot(datalistX[i],datalistY2[i], '.', color=colorlist[i+1])
        ax2.set_ylabel(ylabel2,color=colorlist[i+1])
        i = i + 1
        
    
    # make a plot 'ax', with markers and lines, color=red
    if xlimits != None:
        ax.set_xlim(xlimits[0],xlimits[1])   # set the range of the x-axis of plot 'ax'
    if ylimits != None:
        ax.set_ylim(ylimits[0],ylimits[1])   # set the range of the y-axis
    #ax.set_xlabel('Potential, V')   # set the label of the x-axis
    #ax.set_ylabel('Current, mA/cm^2') # set the label of the y-axis
    if legend == True:
        ax.legend(loc='upper right')       # place the legend at the 'upper left'
    if gridlines == True:
        ax.xaxis.set_minor_locator(MultipleLocator(10))   # add minor ticks for the x-axis
        ax.yaxis.set_minor_locator(AutoMinorLocator())    # add minor ticks for the y-axis
        ax.xaxis.grid(True, which='both') # add grids to the x-axis for both major and minor ticks
    if title != None:
        ax.set_title(title)

    plt.show()   # display 'ax'