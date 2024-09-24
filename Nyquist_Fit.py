# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 13:59:15 2024

@author: isaac
"""

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
    #colorlist=['g','b','r','y','k','c','m'] #green, blue, red, yellow, black, cyan, magenta
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
            datalistX[i],datalistY1[i],datalistY2[i]=np.loadtxt(fname=r"C:\Users\isaac\OneDrive\Documents\aluminum substituted hematite reduction project\Electrochemical tests\txt files\9_22\no ammonia"+"/" + filenames[i] + ".txt", skiprows=1, unpack=True,
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
        #ax.plot(datalistY1[i], datalistY2[i]/const, '.', color=colorlist[i],label=filenames[i])
        return([datalistX,datalistY1[i],datalistY2[i]])
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

def Nyquist(data,axes=None,title=None,linestyle='bx'):
    
    # Allow user to provide axes "axes" to plot to... else new figure
    if axes is None:
        newfig, axes = plt.subplots(1,1,figsize=(4,4)) # Subplots for OOP
        
    axes.plot(data["Re(Z)/Ohm"],data["-Im(Z)/Ohm"],linestyle)  # Plot real and imaginary impedance
    axes.set_xlabel("Z(Re) / $\Omega$")
    axes.set_ylabel("-Z(Im) / $\Omega$")
    
    xmax = max(data["Re(Z)/Ohm"])  # Scale y-data to prepare a semicircle
    axes.set_ylim([0, xmax*1.1])
    axes.set_xlim([0, xmax*1.1])
    
    if title is not None: axes.title.set_text(title)
    
    return(data)
    
def Bode(data,axes=None,title=None,linestyle='rx'):
    
    # Allow user to provide axes "axes" to plot to... else new figure
    if axes is None:
        newfig, axes = plt.subplots(constrained_layout=True)
    
    axes.plot(data["freq/Hz"],data["|Z|/Ohm"],'bx')
    secondaxis = axes.twinx()  # Generate a second y-axis for plotting phase
    secondaxis.plot(data["freq/Hz"],data["Phase(Z)/deg"],linestyle)  # Plot phase
    axes.set_xlabel('Frequency / Hz')
    axes.set_ylabel('|Z| / $\Omega$')
    secondaxis.set_ylabel('Phase / Hz')
    axes.set_xscale('log')  # Bode plot is log/log (not phase)
    axes.set_yscale('log')  
    
    if title is not None: axes.title.set_text(title)  # Add a title if available
    
    return
    
def Randles_Imp(w, R_ohm, R_ct, C_d, flagNyquist=False):
    
    '''w is a list or data frame column of frequencies, parameters are single valued. 
    flagNyquist returns Real/Imaginary components, else return |Z|'''
    
    # This is my result for a Randles circuit. Work up more complicated results in class?
    Z_Re = R_ohm + R_ct/(1+(w*C_d*R_ct)**2)
    Z_Im = w*C_d*R_ct**2/(1+(w*C_d*R_ct)**2)
    
    if flagNyquist:
        return Z_Re, Z_Im
    else:
        Zmag = np.abs(Z_Re+Z_Im*1j)
        return Zmag

def MultiRC_Imp(w, R_0=0, N=1, Rs=10, Cs=1e-6, flagNyquist=False):
    
    '''w is a list of frequencies, R_0 is the uncompensated resistance, N is the number of series RC circuits, 
    Rs is a list of resistors and Cs is a list of capacitors, both must be length=N 
    flagNyquist returns Real/Imaginary components, else return |Z|'''

    Z_Re = R_0
    Z_Im = 0
    
    for i in range(0,N):
        Z_Re += Rs[i]/(1+(w*Cs[i]*Rs[i])**2)
        Z_Im += w*Cs[i]*Rs[i]**2/(1+(w*Cs[i]*Rs[i])**2)
    
    if flagNyquist:
        return Z_Re, Z_Im
    else:
        Zmag = np.abs(Z_Re+Z_Im*1j)
        return Zmag
    
    
def plot_multiRC_sim(coeffs, wmin=2, wmax=7):
    '''Function for plotting the results from leastsq using function MultiRC_Imp'''
    '''Coeffs is a list with R_u, R1, C1, R2, C2, ...'''
    R_u = coeffs[0]
    Rs = coeffs[1::2]
    Cs = coeffs[2::2]
    N = int(len(Rs))
    ws = np.logspace(wmin,wmax)
    zre, zim = MultiRC_Imp(ws,R_u,N,Rs,Cs,flagNyquist=True)
    sim_data = pd.DataFrame({"Re(Z)/Ohm":zre,
                         "-Im(Z)/Ohm":zim,
                         "freq/Hz":ws,
                         "|Z|/Ohm":np.abs(zre-zim*1j),
                         "Phase(Z)/deg":np.arctan(-zim/zre)/(2*np.pi)*360})
    fig,axs = plt.subplots(1,2,figsize=(8,4))
    axs[0] = Nyquist(sim_data,axes=axs[0])
    axs[1] = Bode(sim_data,axes=axs[1])
    fig.tight_layout(pad=0.5) 
    
    
def plot_randles_sim(coeffs, wmin=2, wmax=7):
    '''Function for plotting the results from leastsq using function Randles_Imp'''
    '''coeffs is a list with R_u, Rct, Cdl'''
    R_u = coeffs[0]
    R_ct = coeffs[1]
    C_dl = coeffs[2]
    ws = np.logspace(wmin,wmax)
    zre, zim = Randles_Imp(ws,R_u,R_ct,C_dl,flagNyquist=True)
    sim_data = pd.DataFrame({"Re(Z)/Ohm":zre,
                             "-Im(Z)/Ohm":zim,
                             "freq/Hz":ws,
                             "|Z|/Ohm":np.abs(zre-zim*1j),
                             "Phase(Z)/deg":np.arctan(-zim/zre)/(2*np.pi)*360})
    #fig,axs = plt.subplots(1,2,figsize=(8,4))
    #axs[0] = Nyquist(sim_data,axes=axs[0])
    #axs[1] = Bode(sim_data,axes=axs[1])
    #fig.tight_layout(pad=0.5) 
    return(sim_data)
    
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
    
def Nyquist_fit(filename,coeffs):
    colorlist=['g','b','r','y','k','c','m'] #green, blue, red, yellow, black, cyan, magenta
    
    
    fig = plt.figure(figsize=(8, 6))    # Create a graph 'fig' which has 4 inches in width and 6 inches in height.
    ax = fig.add_subplot(111)           # Create a subplot 'ax' in the figure 'fig'. 
    ax.set_xlabel('Z real (Ohm)')   # set the label of the x-axis
    ax.set_ylabel('Z imaginary (Ohm)') # set the label of the y-axis
    ax.xaxis.set_major_locator(plt.MaxNLocator(3)) #set x-axis tick size
    ax.yaxis.set_major_locator(plt.MaxNLocator(3)) #set y-axis tick size
    
    empirical=Nyquist_grapher(1,[filename],None,None,'(Ohm)',None,True,False)
    
    ax.plot(empirical[1],empirical[2], '.', color=colorlist[0])
    data = plot_randles_sim(coeffs)
    #print(data)
    ax.plot(data["Re(Z)/Ohm"],data["-Im(Z)/Ohm"],'.',color=colorlist[1])
