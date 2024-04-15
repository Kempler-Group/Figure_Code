# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 23:41:41 2024

@author: isaac
"""

import pandas as pd
import numpy as np  # Numpy is a useful module for scientific computing (similar language to MATLAB)
import matplotlib.pyplot as plt  # import the module for plotting data
import math  # import the module containing mathematical functions
from matplotlib.ticker import (MultipleLocator, AutoMinorLocator)     # Configure tick location and format
import matplotlib.pylab as pylab #for qol features, in this case text size manipulation
#Make sure to replace my file path with your own.

def XRD_grapher(filenames,title,xlimits,ylimits,txt,legend,gridlines,xlabel,ylabel,xcolumn,
                   ycolumn,cutoff,const,d_values): #txt is True if values are separated by ' ' and False if separated by ','
    #set title to None if you do not want a title
    #xlimits and ylimits set custom limits. Set to None if you want autoscaling.
    #legend is True if there is a legend.
    #gridlines is True if there are gridlines
    #xcolumn and ycolumn specify the columns which hold the relevant data
    #cutoff cuts the data off at a specific x value (for data manipulation - use xlimits and ylimits for graphing)
    #cutoff cuts off at an index, not a value
    #const is a normalizing constant for the y axis
    #multiple files can be plotted on top of each other (up to 7). filenames is an array-type object
    # if d_values is True, the x axis will be plotted as d values in nm using Cu Kalpha wavelength (0.15418 nm). If d_values
    #is False, XRD spectra will be plotted as 2 theta vs intensity
    
    #sample input: XRD_grapher(['iron oxide sample 1 test 2'],None,None,None,False,False,False,'$%s$'%'2 \\theta','intensity',0,1,None,1)

    fig = plt.figure(figsize=(8, 6))    # Create a graph 'fig' which has 4 inches in width and 6 inches in height.
    ax = fig.add_subplot(111)           # Create a subplot 'ax' in the figure 'fig'. 

    ax.set_ylabel(ylabel)   # set the label of the x-axis
    ax.set_xlabel(xlabel) # set the label of the y-axis
    
    params={'axes.labelsize': 'xx-large',   #set text size
         'axes.titlesize':'xx-large',
         'xtick.labelsize':'xx-large',
         'ytick.labelsize':'xx-large'}
    pylab.rcParams.update(params)
    
    X1 = []
    X2 = []
    X3 = []
    X4 = []
    X5 = []
    X6 = []
    X7 = []
    Y1 = []
    Y2 = []
    Y3 = []
    Y4 = []
    Y5 = []
    Y6 = []
    Y7 = []
    colorlist=['g','b','r','y','k','c','m']
    datalistX=[X1,X2,X3,X4,X5,X6,X7]
    datalistY=[Y1,Y2,Y3,Y4,Y5,Y6,Y7]

    i=0
    

    while(i < len(filenames)):
        if txt == False:
            datalistX[i],datalistY[i]=np.loadtxt(fname="C:/Users/isaac/OneDrive/Documents/Ironmaking Project/XRD/4_1 solution/" + filenames[i] + ".txt", skiprows=146, unpack=True,delimiter=',',
                                                     usecols=(xcolumn,ycolumn))

        elif txt == True:
            datalistX[i],datalistY[i]=np.loadtxt(fname="C:/Users/isaac/OneDrive/Documents/Electrochemistry Program/Echem Project/Data/txt files/3_1_24/" + filenames[i] + ".txt", skiprows=146, unpack=True
                ,usecols=(xcolumn,ycolumn))
            #replace filepaths with your own
            #you might have to customize skiprows for specific files
        if cutoff == None:
            cutoff = len(datalistX[i])
        
        if d_values == False:
            ax.plot(datalistX[i][0:cutoff], (datalistY[i][0:cutoff])/const, '.', color=colorlist[i],label=filenames[i])
        elif d_values == True:
            dValueArray = ((2*np.sin(0.0174532925199433*(datalistX[i][0:cutoff]/2)))**(-1))*0.15418  #Bragg law
            ax.plot(dValueArray, (datalistY[i][0:cutoff])/const, '.', color=colorlist[i],label=filenames[i])
        
        
        i = i + 1
        if cutoff != len(datalistX[i-1]):
            print(datalistX[i][cutoff])
    
    # make a plot 'ax', with markers and lines, color=red
    if xlimits != None:
        ax.set_xlim(xlimits[0],xlimits[1])   # set the range of the x-axis of plot 'ax'
    if ylimits != None:
        ax.set_ylim(ylimits[0],ylimits[1])   # set the range of the y-axis

    if legend == True:
        ax.legend(loc='upper left')       # place the legend at the 'upper left'
    if gridlines == True:
        ax.xaxis.set_minor_locator(MultipleLocator(10))   # add minor ticks for the x-axis
        ax.yaxis.set_minor_locator(AutoMinorLocator())    # add minor ticks for the y-axis
        ax.xaxis.grid(True, which='both') # add grids to the x-axis for both major and minor ticks
    if title != None:
        ax.set_title(title)

    plt.show()   # display 'ax'