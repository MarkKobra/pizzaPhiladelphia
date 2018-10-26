import numpy as np

def crust_coefficient(crustRating,plotDistribution=0):
    #Abs value of the difference presents a sharper drop off from ideal
    #Crust is the dominating factor in the pizza experience after all
    #Not too thick, not too chewy, light and crisp without being burnt	
    #Check the distribution here at www. it's right below you	
    if plotDistribution==1:	
        import matplotlib.pyplot as plt
        tempx= np.linspace(0,2,100)
        tempy= [np.e**((-1./0.4)*abs(x-1)) for x in tempx]
        plt.plot(tempx,tempy)
        plt.show()
    if crustRating !=0:	
        return np.e**((-1./0.4)*abs(crustRating-1))
    else:
        return 0

def cheese_coefficient(cheeseRating, plotDistribution=0):
    #Normal cheese distribution allows for lower quality to regress towards the mean
    #It doesn't have to be good cheese to be enjoyable cheese
    #Ref. Cheeze Whiz
    #That last line of comment had too (two) many z's for talking about cheese
    if plotDistribution==1:
        import matplotlib.pyplot as plt
        tempx= np.linspace(0,1,100)
        tempy= [np.e**((-1./1.1)*(x-1)**2) for x in tempx]
        plt.plot(tempx,tempy)
        plt.show()
    if cheeseRating!=0:
        return np.e**((-1./1.1)*(cheeseRating-1)**2)
    else:
        return 0

def sauce_coefficient(sauceRating,plotDistribution=0):
    #Sauce is just cheese made from tomato milk
    #I tend to air on the side of sweet/acidic sauced	
    if plotDistribution==1:	
        import matplotlib.pyplot as plt
        tempx= np.linspace(0,1,100)
        tempy= [np.e**((-1./1.1)*(x-1)**2) for x in tempx]
        plt.plot(tempx,tempy)
        plt.show()
        if sauceRating!=0:
            return np.e**((-1./1.1)*(sauceRating-1)**2)
        else:
            return 0

def cheese_bread_ratio_coefficient(cbrRating,plotDistribution=0):
    #Smooth transition to 0 return values.
    #Much like cheese quality, the ratio can be rather forgiving
    if plotDistribution==1:
        import matplotlib.pyplot as plt
        tempx= np.linspace(0,2,30)
        tempy= [1-abs((x-1))**3 for x in tempx]
        plt.plot(tempx,tempy)
        plt.show()
    if abs(cbrRating)<2:
        return 1-abs((cbrRating-1))**3
    else:
        return 0

def sauce_bread_ratio_coefficient(sbrRating,plotDistribution=0):
    if plotDistribution==1:
        import matplotlib.pyplot as plt
        tempx1= np.linspace(0,1,15)
        tempy1= [1-abs((x-1))**2 for x in tempx1]
        tempx2= np.linspace(1,2,15)
        tempy2= [1-abs((x-1))**.8 for x in tempx2]
        tempx= np.concatenate((tempx1,tempx2))
        tempy= np.concatenate((tempy1,tempy2))
        plt.plot(tempx,tempy)
        plt.show()			
    if 1<sbrRating<2:
        return 1-abs((sbrRating-1))**.8
    elif 0<sbrRating<1:
        return 1-abs((sbrRating-1))**2	
    else:
        return 0

def price_coefficient(priceExpected,priceCost,plotDistribution=0):
    #Price doesn't play a huge impact, the distribution is rather flat
    #This is partly to minimize my cheapness
    if plotDistribution==1:
        import matplotlib.pyplot as plt
        tempx1= np.linspace(1.8,6,10)
        tempy1= [((x/float(2))**-0.03) for x in tempx1]
        tempx2= np.linspace(6,12,10)
        tempy2= 10*[0.1]
        tempx= np.concatenate((tempx1,tempx2))
        tempy= tempy1+tempy2
        plt.plot(tempx,tempy,label="Expected $2usd")
        plt.legend(loc=3)
        plt.show()		
    if float(priceCost)/float(priceExpected)<3:
        return ((float(priceCost)/float(priceExpected))**-0.03)
    else:
        return 0.1

def calculate_total_rating(tempcr,tempch,temps,tempcbr,tempsbr,temppe,temppc):
    #Geometric mean is evaluated to address small outliers
    #If something is 0 it is all 0
    cr= crust_coefficient(tempcr)
    ch= cheese_coefficient(tempch)
    s= sauce_coefficient(temps)
    cbr= cheese_bread_ratio_coefficient(tempcbr)
    sbr= sauce_bread_ratio_coefficient(tempsbr)
    p= price_coefficient(temppe,temppc)
    finalCoef= (cr*ch*cbr*sbr*p)**(1./6)
    if finalCoef<1:
        return finalCoef
    else:
        return 1.