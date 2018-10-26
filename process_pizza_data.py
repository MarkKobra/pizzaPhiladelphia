import numpy as np
import matplotlib.pyplot as plt
from pizza_functions import *

dictColor= {'Fast':'r','UCity':'y','SPhilly':'g','Center':'b','NLib':'m','Frozen':'k'}
dictSize= {'Old':5,'New':8}
dictMarker= {1:'^',0:'o'}

with open("Pizza_Data_Oct3.csv") as xStringValues:
    lines= xStringValues.readlines()[1:]
    for line in lines:
        x=line.split(',')
        tempXVal=float(x[7])/float(x[6])
        tempScore=calculate_total_rating(float(x[1]),float(x[2]),float(x[3]),
                                         float(x[4]),float(x[5]),float(x[6]),float(x[7]))	
        plt.plot([1./tempXVal,1./tempXVal],[tempScore,tempScore],mfc=dictColor[x[8]],
                 mec=dictColor[x[8]],marker=dictMarker[int(round(tempScore-0.3))]
                 ,markersize=dictSize[x[9].strip('\n')])
        plt.annotate(x[0],xy=(1.01/tempXVal,tempScore),fontsize=10)
    
    plt.annotate('*Pizza by the Slice',[0.94,0.52])
    plt.plot([0.5,0.5],[-100,-100],'ro',label='Fast')
    plt.plot([0.5,0.5],[-100,-100],'yo',label='U City')
    plt.plot([0.5,0.5],[-100,-100],'go',label='S. Philly')
    plt.plot([0.5,0.5],[-100,-100],'bo',label='Center')
    plt.plot([0.5,0.5],[-100,-100],'mo',label='N. Lib')
    plt.plot([0.5,0.5],[-100,-100],'ko',label='Frozen')
    plt.xlabel(r'Price Factor ($\frac{Expected}{Actual}$)')
    plt.title('Final Undeniable Unbiased Rank')
    plt.ylabel('Score')
    plt.ylim(0.5,1)
    plt.xlim(0.5,1.1)
    plt.legend(loc=[1.05,0.5])

    fillPlotX= np.linspace(0.9,2.5,100)
    fillHighEnd= np.linspace(0.8,1.5,100)
    fillLowEnd= np.linspace(0,.8,100)
    fillUpperBound= [1 for j in range(100)]
    fillLowerBound= [0.8 for j in range(100)]
    plt.fill_between(fillHighEnd,fillLowerBound,fillUpperBound,color='lightgreen')
    plt.fill_between(fillLowEnd,fillLowerBound,fillUpperBound,color='lightgreen',alpha=0.5)
    plt.fill_between(fillLowEnd,fillLowerBound,color='salmon',alpha=0.8)
    plt.fill_between(fillHighEnd,fillLowerBound,color='salmon',alpha=0.3)
    
    plt.show()

