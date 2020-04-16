from NeuralNetUtil import buildExamplesFromCarData,buildExamplesFromPenData
from NeuralNet import buildNeuralNet
import cPickle 
from math import pow, sqrt

def average(argList):
    return sum(argList)/float(len(argList))

def stDeviation(argList):
    mean = average(argList)
    diffSq = [pow((val-mean),2) for val in argList]
    return sqrt(sum(diffSq)/len(argList))

penData = buildExamplesFromPenData() 
def testPenData(hiddenLayers = [24]):
    return buildNeuralNet(penData,maxItr = 200, hiddenLayerList =  hiddenLayers)

carData = buildExamplesFromCarData()
def testCarData(hiddenLayers = [16]):
    return buildNeuralNet(carData,maxItr = 200,hiddenLayerList =  hiddenLayers)

def test5a():
    pen = []
    for i in range(0,5):
        nnet, accuracy = testPenData()
        pen.append(accuracy)

    print "Max: ", max(pen)
    print "Average: ", average(pen)
    print "Standard Deviation: ", stDeviation(pen)

def test5b():
    car = []
    for i in range(0,5):
        nnet, accur = testCarData()
        car.append(accur)

    print "Max: ", max(car)
    print "Average: ", average(car)
    print "Standard Deviation: ", stDeviation(car)

def test6a():
    for layers in range(20, 41, 5):
        data = []
        for i in range(5):
            test = testPenData([layers])
            data.append(test[1])

        print "# Perceptrons: ", layers
        print "Max:", max(data)
        print "Average:", average(data)
        print "Standard Dev:", stDeviation(data)

def test6b():
    for layers in range(20, 41, 5):
        data = []
        for i in range(5):
            test = testCarData([layers])
            data.append(test[1])

        print "# Perceptrons: ", layers
        print "Max:", max(data)
        print "Average:", average(data)
        print "Standard Dev:", stDeviation(data)

#test5a()
#test6a()
#test5b()
#test6b()