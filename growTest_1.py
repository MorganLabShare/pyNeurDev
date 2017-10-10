#!/bin/python

#import matplotlib
#matplotlib.use('TkAgg')
#export DISPLAY=:0.0
import matplotlib.pyplot as plt
#from mpl_toolkits.mplot3d import Axes3D
import numpy as np
#import pylab
import itertools
import time

#create a test class for neuron
class neuron:
    # init method creates the basic neuron attributes from the attribs list
    def __init__(self, attribs):
        self.name = attribs[0]
        self.size = attribs[1]
        self.nodeArray = np.zeros([1,3])
        self.nodeList = []
    # make an array containing all the voxels that are within the soma
    def getSomaArray(self):
        self.somaVoxArray = np.fromiter(itertools.chain(*itertools.product(range(self.size),repeat=3)), dtype=int).reshape(-1,3)
        self.nodeArray=np.append(self.nodeArray,self.somaVoxArray,axis=0)
    def getSomaList(self):
        self.somaVoxList = list(itertools.product(range(self.size),repeat=3))
        self.nodeList.append(self.somaVoxList)
    #test functions
    def grow(self):
        self.isGrowing=1
    def resting(self):
        self.isResting=1


startNeurGen=time.time()
startAttribs=("steve",20)
neur1 = neuron(startAttribs)
finishNeurGen=time.time()
print('neurGenTime=',finishNeurGen-startNeurGen)

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

def plotNeurArray(neur):
    startPlotArray=time.time()
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(neur.somaVoxArray[:,0],neur.somaVoxArray[:,1],neur.somaVoxArray[:,2])
    finishPlotArray=time.time()
    print('plotArray=',finishPlotArray-startPlotArray)

def plotNeurList(neur):
    startPlotList=time.time()
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter((zip(*neur.somaVoxList)[0]),(zip(*neur.somaVoxList)[1]),(zip(*neur.somaVoxList)[2]))
    finishPlotList=time.time()
    print('plotList=',finishPlotList-startPlotList)

#import code
#code.interact(local=locals())



######
# Need to do some basic testing to find out if it is faster to put my overall
# neuron voxel list in an array or in a list
######
