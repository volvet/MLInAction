

from numpy import *
import operator
import matplotlib
import matplotlib.pyplot as plt

def datingType2Number(datingType):
	if datingType == 'didntLike':
		return 1
	if datingType == 'smallDoses':
		return 3
	if datingType == 'largeDoses':
		return 5
	print "Unknonw", datingType

def createDataSet():
	group = array( [[1.0, 1.1], [1.0, 1.0], [0, 0], [0, 0.1]] )
	labels = ['A', 'A', 'B', 'B']
	return group, labels


def classify0(inX, dataSet, labels, k):
	dataSetSize = dataSet.shape[0]
	diffMat = tile(inX, (dataSetSize, 1)) - dataSet
	sqDiffMat = diffMat ** 2
	sqDistances = sqDiffMat.sum(axis=1)
	distances = sqDistances ** 0.5
	sortedDistIndices = distances.argsort()
	classCount = {}
	for i in range(k):
		votelLabel = labels[sortedDistIndices[i]]
		classCount[votelLabel] = classCount.get(votelLabel,0) + 1
	sortedClassCount = sorted(classCount.iteritems(), key=operator.itemgetter(1), reverse=True)
	return sortedClassCount[0][0]

def file2matrix(filename):
	fr = open(filename)
	numberOfLines = len(fr.readlines())
	mat = zeros((numberOfLines, 3))
	labels = []
	index = 0
	fr = open(filename)
	for line in fr.readlines():
		#print line
		line = line.strip()
		listFromeLine = line.split('\t')
		mat[index,:] = listFromeLine[0:3]
		#print listFromeLine
		labels.append(datingType2Number(listFromeLine[-1]))
		index += 1
	return mat, labels

def autoNorm(dataSet):
	minVals = dataSet.min(0)
	maxVals = dataSet.max(0)
	ranges = maxVals - minVals
	normDataSet = zeros(shape(dataSet))
	m = dataSet.shape[0]
	normDataSet = dataSet - tile(minVals, (m, 1))
	normDataSet = normDataSet/tile(ranges, (m, 1))
	return normDataSet, ranges, minVals


if __name__ == '__main__':
    print "knn test"
    group, labels = createDataSet()
    print "group: \n", group
    print "labels: \n", labels
    print classify0([0, 0], group, labels, 3)

    print "dating test"
    hoRatio = 0.50
    mat, labels = file2matrix('datingTestSet.txt')

    normMat,  ranges, minVals = autoNorm(mat)
    print "ranges = ", ranges
    print "minVals = ", minVals
    #print mat.min(0)
    #print mat
    #fig = plt.figure()
    #ax = fig.add_subplot(111)
    #ax.scatter(mat[:,1], mat[:,2], 15.0*array(labels), 15.0*array(labels))
    #ax.set_ylabel("Icecream")
    #ax.set_xlabel("Game")
    #plt.show()

    #fig = plt.figure()
    #ax = fig.add_subplot(111)
    #ax.scatter(mat[:,0], mat[:,1], 15.0*array(labels), 15.0*array(labels))
    #ax.set_ylabel('Game')
    #ax.set_xlabel('flight')
    #plt.show()



    

