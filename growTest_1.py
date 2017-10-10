#!/bin/python

#import matplotlib
#matplotlib.use('TkAgg')
#export DISPLAY=:0.0
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
#import pylab
import itertools
import time

#create a test class for neuron
class neuron:
    # init method creates the basic neuron attributes from the attribs list
    def __init__(self, cfgNeuron):
        self.name = cfgNeuron[0]
        self.size = cfgNeuron[1]
        self.nodeArray = np.zeros([1,3])
        self.nodeList = []
        self.branchList = []
        
    # make an array containing all the voxels that are within the soma
        #this is super slow
    def getSomaArray(self):
        self.somaVoxArray = np.fromiter(itertools.chain(*itertools.product(range(self.size),repeat=3)), dtype=int).reshape(-1,3)
        self.nodeArray=np.append(self.nodeArray,self.somaVoxArray,axis=0)
    
    #make a LIST with the voxels
        #this is way faster    
    def getSomaList(self):
        self.somaVoxList = list(itertools.product(range(self.size),repeat=3))
        self.nodeList.append(self.somaVoxList)
    #test functions; not functional. I guess it grows all branches
    def growNeuron(self):
        self.isGrowing=1
        self.isResting=0
    def restNeuron(self):
        self.isResting=1
        self.isGrowing=0
    def updateNeuron(self):
        #update the neuron voxlist so it includes the branches
        
    
    #For now, I'm going to define the neurite class within the neuron class
    class branch:
            def __init__(self, cfgBranch):
                self.name = cfgBranch[0]
                self.root = cfgBranch[1]
                self.growthRate = cfgBranch[2]
                self.tortuosity = cfgBranch[3]
                self.nodeList = []
            def growBranch(self):
                self.isGrowing=1
                self.isResting=0
            def restBranch(self):
                self.isResting=1
                self.isGrowing=0
                

#Time to initialize is essentially zero. Probably because we haven't made anything
startNeurGen=time.time()
startAttribs=("steve",10)
neur1 = neuron(startAttribs)
neur1.branch1 = neur1.branch(["steveBranch1",[11,11,11],1,1])
finishNeurGen=time.time()
print('neurGenTime=',finishNeurGen-startNeurGen)

#The array method is super slow.
startArray=time.time()
neur1.getSomaArray()
finishArray=time.time()
print('arrayTime=',finishArray-startArray)

#Manipulation of the list appears to be 5x-10x faster than then array
#I can also probably remove things faster there.
startList=time.time()
neur1.getSomaList()
finishList=time.time()
print('listTime=',finishList-startList)

#Plotting the array is way faster than plotting the list
def plotNeurArray(neur):
    startPlotArray=time.time()
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(neur.somaVoxArray[:,0],neur.somaVoxArray[:,1],neur.somaVoxArray[:,2])
    finishPlotArray=time.time()
    print('plotArray=',finishPlotArray-startPlotArray)

#This is much slower than the array method. I will try it with a list->array step
def plotNeurList(neur):
    startPlotList=time.time()
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter((zip(*neur.somaVoxList)[0]),(zip(*neur.somaVoxList)[1]),(zip(*neur.somaVoxList)[2]))
    finishPlotList=time.time()
    print('plotList=',finishPlotList-startPlotList)

#This is seemingly the FASTEST, but that should be checked with scaling.
def plotNeurList2Array(neur):
    startPlotList2Array=time.time()
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    tempArray=np.array(neur.somaVoxList)
    ax.scatter(tempArray[:,0],tempArray[:,1],tempArray[:,2])
    finishPlotList2Array=time.time()
    print('plotList=',finishPlotList2Array-startPlotList2Array)


#import code
#code.interact(local=locals())



######
# Need to do some basic testing to find out if it is faster to put my overall
# neuron voxel list in an array or in a list
######
