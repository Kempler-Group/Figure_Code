# -*- coding: utf-8 -*-
"""
Created on Sun May  5 17:33:43 2024

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

def blank_CV_grapher(blank, pconst, currentconst #Normalizing constant to turn current input into current density output if desired
               ,filenames,title,xlimits,yunits,ref,ylimits,txt,currentDependence,gridlines,cycle,legend): #txt is true if dealing with a txt file, and false if dealing with a csv
#currentDependence: True if current is on the y axis.   
#sample input: CV_grapher(1,['blank_CV'],None,None,'(mA)',None,True,True,False)

    fig = plt.figure(figsize=(8, 6))    # Create a graph 'fig' which has 4 inches in width and 6 inches in height.
    ax = fig.add_subplot(111)           # Create a subplot 'ax' in the figure 'fig'. 
    if currentDependence == True:
        ax.set_ylabel('Current ' + yunits)
        ax.set_xlabel('Potential (V) vs. ' + ref)
    else:
        ax.set_ylabel('Potential (V)')   # set the label of the x-axis
        ax.set_xlabel('Current ' + yunits) # set the label of the y-axis
    
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
    C1 = []
    C2 = []
    C3 = []
    C4 = []
    C5 = []
    C6 = []
    C7 = []
    colorlist=['g','b','r','y','k','c','m']
    datalistX=[X1,X2,X3,X4,X5,X6,X7]
    datalistY=[Y1,Y2,Y3,Y4,Y5,Y6,Y7]
    cycles=[C1,C2,C3,C4,C5,C6,C7]
    
    blankX,blankY,blankcycles=np.loadtxt(fname=r"C:\Users\isaac\OneDrive\Documents\aluminum substituted hematite reduction project\Electrochemical tests\txt files\5_1 and 5_2 CVs"+"/" + blank + ".txt", skiprows=1, unpack=True,
                                         usecols=(0,1,2))
    
    i2 = 0
    blankX2 = []
    blankY2 = []
    if cycle == None:
        blankX2 = blankX
        blankY2 = blankY
    else:
        while(i2<len(blankX)): #cycle selector functionality
            if blankcycles[i2] == cycle: #cycles[i][i2] < cycle+0.5 and cycles[i][i2]>cycle-0.5:
                blankX2 = np.append(blankX2,blankX[i2])
                blankY2 = np.append(blankY2,blankY[i2])
           
            i2 = i2 + 1
    
    i=0
    while(i < len(filenames)):
        if txt == False:
            if currentDependence == True:
                datalistX[i],datalistY[i]=np.loadtxt(fname="C:/Users/isaac/OneDrive/Documents/Electrochemistry Program/Lab 2/Project 1/Week 1/Data/CH693 Project 1 Week 1/CH693 Project 1 Week 1/" + filenames[i] + ".csv", delimiter = ',', skiprows=1, unpack=True,
                   usecols=(0,1))
            else:
                datalistY[i],datalistX[i]=np.loadtxt(fname="C:/Users/isaac/OneDrive/Documents/Electrochemistry Program/Echem Project/Data/txt files/Week 3/" + filenames[i] + ".csv", skiprows=1, unpack=True,
                                                     usecols=(0,1))
                     # Read data from a file scan1.csv and skip the first row.
        elif txt == True:
            if currentDependence == True:
                datalistX[i],datalistY[i],cycles[i]=np.loadtxt(fname=r"C:\Users\isaac\OneDrive\Documents\aluminum substituted hematite reduction project\Electrochemical tests\txt files\5_1 and 5_2 CVs"+"/" + filenames[i] + ".txt", skiprows=1, unpack=True,
                                                     usecols=(0,1,2))
            else:
                datalistY[i],datalistX[i]=np.loadtxt(fname="C:/Users/isaac/OneDrive/Documents/Electrochemistry Program/Echem Project/Data/txt files/Week 3/" + filenames[i] + ".txt", skiprows=1, unpack=True,
                                                     usecols=(0,1))
                
        i2 = 0
        disposableX = []
        disposableY = []
        if cycle == None:
            disposableX = datalistX[i]
            disposableY = datalistY[i]
        else:
            while(i2<len(datalistX[i])): #cycle selector functionality
                if cycles[i][i2] == cycle: #cycles[i][i2] < cycle+0.5 and cycles[i][i2]>cycle-0.5:
                    disposableX = np.append(disposableX,datalistX[i][i2])
                    disposableY = np.append(disposableY,datalistY[i][i2])
               
                i2 = i2 + 1
        #return disposableX
        """-(blankY2/currentconst)"""   
        
        if len(blankY2) != len(disposableY):
            if len(blankY2)<len(disposableY):
                i = np.abs(len(blankY2)-len(disposableY))
                i1 = 0
                while i1 < i:
                    blankY2 = np.append(blankY2,blankY2[len(blankY2)-1])
                    i1 = i1 + 1
            elif len(blankY2)>len(disposableY):
                i = np.abs(len(blankY2)-len(disposableY))
                i1 = 0
                while i1 < i:
                    disposableY = np.append(disposableY,disposableY[len(disposableY)-1])
                    disposableX = np.append(disposableX,disposableX[len(disposableX)-1])
                    i1 = i1 + 1
        
        print(len(disposableX))
        print(len(blankY2))
        i = 0
        ax.plot(disposableX+pconst, (disposableY/currentconst)-(blankY2/currentconst), '.', color=colorlist[i],label=filenames[i])
        i = i + 1
        #skiprows in np.loadtxt skips the number of rows specified. You may have to customize this to your own file.
        #you also might need to change usecols. The arrays to be read into correspond respectively to the inputs in usecols

    if xlimits != None:
        ax.set_xlim(xlimits[0],xlimits[1])   # set the range of the x-axis of plot 'ax'
    if ylimits != None:
        ax.set_ylim(ylimits[0],ylimits[1])   # set the range of the y-axis
    
    if legend == True:
        ax.legend(loc='lower right')       # place the legend at the 'upper left'
    if gridlines == True:
        ax.xaxis.set_minor_locator(MultipleLocator(10))   # add minor ticks for the x-axis
        ax.yaxis.set_minor_locator(AutoMinorLocator())    # add minor ticks for the y-axis
        ax.xaxis.grid(True, which='both') # add grids to the x-axis for both major and minor ticks
    ax.set_title(title)

    plt.show()   # display 'ax'
    #print(len(disposableX))
    #print(len(blankX))