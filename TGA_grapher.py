# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 11:48:09 2024

@author: isaac
"""

import pandas as pd
import numpy as np  # Numpy is a useful module for scientific computing (similar language to MATLAB)
import matplotlib.pyplot as plt  # import the module for plotting data
import math  # import the module containing mathematical functions
from matplotlib.ticker import (MultipleLocator, AutoMinorLocator)     # Configure tick location and format
import matplotlib.pylab as pylab #for qol features, in this case text size manipulation
#Make sure to replace my file path with your own.

def TGA_grapher(const #Normalizing constant
               ,filenames,title,xlimits,ylimits,txt,gridlines): #txt is true if dealing with a txt file, and false if dealing with a csv
    
    fig = plt.figure(figsize=(8, 6))    # Create a graph 'fig' which has 4 inches in width and 6 inches in height.
    ax = fig.add_subplot(111)           # Create a subplot 'ax' in the figure 'fig'. 
    ax.set_xlabel('temperature '+ '$%s$'%'(\\degree C)')   # set the label of the x-axis
    #sample input: TGA_grapher(1,['4_1 sample test 1plot signals'],None,[0,586],[80,100],True,None)
    #you will have to convert files to utf-8 encoding and save as txt files before using this function
    
    

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
    Z1 = []
    Z2 = []
    Z3 = []
    Z4 = []
    Z5 = []
    Z6 = []
    Z7 = []
    C1 = []
    C2 = []
    C3 = []
    C4 = []
    C5 = []
    C6 = []
    C7 = []
    colorlist=['g','b','r','y','k','c','m']
    datalistX=[X1,X2,X3,X4,X5,X6,X7]
    datalistY1=[Y1,Y2,Y3,Y4,Y5,Y6,Y7]
    datalistY2=[Z1,Z2,Z3,Z4,Z5,Z6,Z7]
    wtpercent=[C1,C2,C3,C4,C5,C6,C7]
    i=0
    while(i < len(filenames)):
        if txt == False:
            datalistX[i],datalistY1[i]=np.loadtxt(fname="C:/Users/isaac/OneDrive/Documents/Electrochemistry Program/Lab/Project 5/Data Files/" + filenames[i] + ".csv", delimiter = ',', skiprows=1, unpack=True,
                   usecols=(0,1,2))
                     # Read data from a file scan1.csv and skip the first row.
        elif txt == True:
            datalistX[i],datalistY1[i],datalistY2[i]=np.loadtxt(fname=r"C:\Users\isaac\OneDrive\Documents\aluminum substituted hematite reduction project\Isaac TGA\txt files"+'/' + filenames[i]+'.txt', skiprows=42, unpack=True,
                   usecols=(1,2,3))
            
        wtpercent[i] = 100*(datalistY1[i]/datalistY1[i][0])

        ax.plot(datalistX[i],wtpercent[i], '.', color='green')
        ax.set_ylabel('wt. %', color = 'green')
        ax2 = ax.twinx()
        ax2.plot(datalistX[i],datalistY2[i], '.', color=colorlist[i+1])
        ax2.set_ylabel('deriv. wt. (%/'+'$%s$'%'\\degree C)',color = 'blue')
        i = i + 1
        
    
    if xlimits != None:
        ax.set_xlim(xlimits[0],xlimits[1])   # set the range of the x-axis of plot 'ax'
    if ylimits != None:
        ax.set_ylim(ylimits[0],ylimits[1])   # set the range of the y-axis
  
    if gridlines == True:
        ax.xaxis.set_minor_locator(MultipleLocator(10))   # add minor ticks for the x-axis
        ax.yaxis.set_minor_locator(AutoMinorLocator())    # add minor ticks for the y-axis
        ax.xaxis.grid(True, which='both') # add grids to the x-axis for both major and minor ticks
    if title != None:
        ax.set_title(title)

    plt.show()   # display 'ax'