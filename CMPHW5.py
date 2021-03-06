#Ben Moreau

import numpy as np
import scipy as sp

def NonTrivial(i):
    return np.sin(i*np.pi)

ys= NonTrivial(np.linspace(0,1,100000))

from matplotlib import pyplot as plt

def f(i,mx):
    return np.exp(np.sqrt((.5-i)**2))*mx

fs=f(np.linspace(0,1,10000),max(ys))

def Prob(i,mx):
    return np.random.randint(0,10**6*np.exp(np.sqrt((.5-i)**2)))/10**6*mx


prob= Prob(np.linspace(0,1,10000),max(ys))
'''
def Prob2(i,mx):
    return np.random.randint(0,10**6*(-np.exp(np.sqrt((.5-i)**2))+np.exp(1)))/10**6*mx
    
prob2= Prob2(np.linspace(0,1,10000),max(ys))
'''
passes=0
total=0
x=0

greens=[]
greensx=[]
for i in range(len(prob)):
    if(prob[i]<np.sin(np.pi*x)):
        passes+=1
        greens.append(prob[i])
        greensx.append(x)
    total+=1

    

    
    x+=1/len(prob)

print("The amount of points that pass is ",passes," out of",total,"points, and the total area under our f is ",np.trapz(fs,np.linspace(0,1,10000)),"so the area of sin(pi*x) from zero to one is ", np.trapz(fs,np.linspace(0,1,10000))*passes/total)



plt.scatter(np.linspace(0,1,100000),ys,label="sin(x)")
plt.scatter(np.linspace(0,1,10000),fs,label="exp(np.sqrt((.5-x)**2))")
plt.scatter(np.linspace(0,1,10000),prob,alpha=.5,s=4,label="exp random points",color="red")
plt.scatter(greensx,greens,alpha=1,s=4,label="random points less than sin(pi*x)",color="green")

#plt.scatter(np.linspace(0,1,10000),prob2,alpha=.5,s=2,label="exp random points, lower at tails")
plt.legend()
plt.xlabel("x")
plt.ylabel("non normalized prob")
plt.show()
