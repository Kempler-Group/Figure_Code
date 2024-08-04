# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 15:48:42 2024

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

# Returns Tafel slope as a function of overpotential
def Tafel_Grapher_slopes_vs_voltage(const #Normalizing constant to turn current input into current density output if desired
               ,filenames,title,xlimits,ylimits,Ru,vs,legend): #Ru in Ohms, Y data in mA, vs is correction for overpotential
    fig = plt.figure(figsize=(8, 6))    # Create a graph 'fig' which has 4 inches in width and 6 inches in height.
    ax = fig.add_subplot(111)           # Create a subplot 'ax' in the figure 'fig'. 
    ax.set_ylabel('Tafel slope (mV/dec)')   # set the label of the x-axis
    ax.set_xlabel('Overpotential (V)') # set the label of the y-axis
    
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
        datalistX[i],datalistY[i]=np.loadtxt(fname=r"C:\Users\isaac\OneDrive\Documents\aluminum substituted hematite reduction project\Electrochemical tests\custom_txt\7_22 Vcorrected"+"/" + filenames[i], #delimiter = ',', 
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
        print(V_corrected[i])
        print(logi[i])
        #smooth
        window_size = 10
        
        logipd = pd.Series(logi[i])
        V_correctedpd = pd.Series(V_corrected[i])  
        df = pd.DataFrame({"logi":logipd,"overpotential":V_correctedpd})
        
        #df = pd.DataFrame({logi[i],V_corrected[i]}) #,columns=['logi','V_corrected'])
        df['overpotential_smooth'] = df["overpotential"].rolling(window=window_size).mean()
        
        #Tafel slope (mV/dec)
        n = 0
        
        Slopes = np.array([])
        
        while(n<(len(df['logi'])-20)):  #20 is the length of data used to acquire the derivative
            Slopes = np.append(Slopes,1000*(df['overpotential_smooth'][n+20]-df['overpotential_smooth'][n])/(df["logi"][n+20]-df["logi"][n]))
            #1000 converts V/dec to mV/dec
            n = n + 1
            
        
        w = 1
        while(w < 21):
            Slopes = np.append(Slopes,Slopes[n-1])
            w = w + 1
        df['Tafel slope (mV/dec)'] = Slopes
        
        #print(df)
        ax.plot(df['overpotential_smooth'],df['Tafel slope (mV/dec)'], '.', color=colorlist[i],
                label=filenames[i])
        ax.set_ylabel('Tafel slope (mV/dec)', color = 'green')
        ax2 = ax.twinx()
        ax2.plot(df['overpotential_smooth'],df['logi'], '.', color=colorlist[i+1])
        ax2.set_ylabel('logi (logA)',color = 'blue')
        """ax.plot(df['overpotential_smooth'],df['logi'], '.', color=colorlist[i],
                label=filenames[i])""" #normal Tafel
        
        if datalistX[i+1] != []:
            i = i + 1
        else:
            i = len(datalistX)
     

    
    
    
    if xlimits != None:
        ax.set_xlim(xlimits[0],xlimits[1])   # set the range of the x-axis of plot 'ax'
    if ylimits != None:
        ax.set_ylim(ylimits[0],ylimits[1])   # set the range of the y-axis
    #ax.set_xlabel('Potential, V')   # set the label of the x-axis
    #ax.set_ylabel('Current, mA/cm^2') # set the label of the y-axis
    if legend ==True:
        ax.legend(loc='lower right')       # place the legend at the 'upper left'
    ax.xaxis.set_minor_locator(MultipleLocator(10))   # add minor ticks for the x-axis
    ax.yaxis.set_minor_locator(AutoMinorLocator())    # add minor ticks for the y-axis
    ax.xaxis.grid(True, which='both') # add grids to the x-axis for both major and minor ticks
    ax.set_title(title)

    plt.show()   # display 'ax'
    #np.savetxt('df',df)