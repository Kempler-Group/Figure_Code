# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 23:19:08 2024

@author: isaac
"""

import pandas as pd
import numpy as np  # Numpy is a useful module for scientific computing (similar language to MATLAB)
import matplotlib.pyplot as plt  # import the module for plotting data
import math  # import the module containing mathematical functions
from matplotlib.ticker import (MultipleLocator, AutoMinorLocator)     # Configure tick location and format

#For a file with two columns, the first being voltage and the second current in mA(not mA/cm^2)

def Nyquist_grapher(const #Normalizing constant to turn current input into current density output if desired
               ,filenames,title,xlimits,yunits,ylimits,txt,gridlines):
    
    fig = plt.figure(figsize=(8, 6))    # Create a graph 'fig' which has 4 inches in width and 6 inches in height.
    ax = fig.add_subplot(111)           # Create a subplot 'ax' in the figure 'fig'. 
    ax.set_xlabel('Z real (Ohm)')   # set the label of the x-axis
    ax.set_ylabel('Z imaginary ' + yunits) # set the label of the y-axis
    ax.xaxis.set_major_locator(plt.MaxNLocator(3)) #set x-axis tick size
    ax.yaxis.set_major_locator(plt.MaxNLocator(3)) #set y-axis tick size
    
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
    #empty lists for larger lists so that the while function below can graph multiple data sets
    colorlist=['g','b','r','y','k','c','m'] #green, blue, red, yellow, black, cyan, magenta
    datalistX=[X1,X2,X3,X4,X5,X6,X7]
    datalistY1=[Y1,Y2,Y3,Y4,Y5,Y6,Y7]
    datalistY2=[Z1,Z2,Z3,Z4,Z5,Z6,Z7]
    cycles=[C1,C2,C3,C4,C5,C6,C7]
    #meta lists
    i=0
    while(i < len(filenames)):
        if txt == False:
            datalistX[i],datalistY1[i]=np.loadtxt(fname=r"C:\Users\isaac\OneDrive\Documents\Electrochemistry Program\Lab 2\Project 1\Week 1\Data" + filenames[i] + ".csv", delimiter = ',', skiprows=1, unpack=True,
                   usecols=(0,1,2,5))
                     # Read data from a file scan1.csv and skip the first row.
        elif txt == True:
            datalistX[i],datalistY1[i],datalistY2[i]=np.loadtxt(fname=r"C:\Users\isaac\OneDrive\Documents\aluminum substituted hematite reduction project\Electrochemical tests\txt files\5_1 PEIS"+"/" + filenames[i] + ".txt", skiprows=1, unpack=True,
                   usecols=(0,1,2))
        """i2 = 0
        disposableX = []
        disposableY1 = []
        disposableY2 = []
        while(i2<len(datalistX[i])): #cycle selector functionality
            if cycles[i][i2] == cycle: #cycles[i][i2] < cycle+0.5 and cycles[i][i2]>cycle-0.5:
                disposableX = np.append(disposableX,datalistX[i][i2])
                disposableY1 = np.append(disposableY1,datalistY1[i][i2])
                disposableY2 = np.append(disposableY2,datalistY2[i][i2])
            i2 = i2 + 1"""
        ax.plot(datalistY1[i], datalistY2[i]/const, '.', color=colorlist[i],label=filenames[i])
        i = i + 1
        
        #the if statement exists to easily read either csv or txt
        
    #fig = plt.figure(figsize=(8, 6))    # Create a graph 'fig' which has 4 inches in width and 6 inches in height.
    #ax = fig.add_subplot(111)           # Create a subplot 'ax' in the figure 'fig'. 
    # subplot(abc): divide 'fig' into a (row)* b (column) sub-plots, 'ax' will be at the c-th sub-panel.
    #ax.plot(data_X, data_Y/0.0314159265358, '.', color='r')  
    # make a plot 'ax', with markers and lines, color=red
    if xlimits != None:
        ax.set_xlim(xlimits[0],xlimits[1])   # set the range of the x-axis of plot 'ax'
    if ylimits != None:
        ax.set_ylim(ylimits[0],ylimits[1])   # set the range of the y-axis
    #ax.set_xlabel('Potential, V')   # set the label of the x-axis
    #ax.set_ylabel('Current, mA/cm^2') # set the label of the y-axis
    #ax.legend(loc='upper left')       # place the legend at the 'upper left'
    if gridlines == True:
        ax.xaxis.set_minor_locator(MultipleLocator(10))   # add minor ticks for the x-axis
        ax.yaxis.set_minor_locator(AutoMinorLocator())    # add minor ticks for the y-axis
        ax.xaxis.grid(True, which='both') # add grids to the x-axis for both major and minor ticks
    ax.set_title(title)

    plt.show()   # display 'ax'
    
# example of function call:
    """
    Nyquist_grapher(1 normalizing factor for y data
                    ,['SPEIS_1300mV_1700mV_after_C01'], filename(s)
               'after conducting electrolysis' graph name
               , None xlimits
               , '(Ohm)' y unit label
               ,None ylimits
               ,True) 'True' if txt file, 'False' if csv file
    """