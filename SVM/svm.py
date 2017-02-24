
from numpy import *

def loadDataSet(fileName):
    dataMat = []; labelMat = []
    fr = open(fileName)
    for line in fr.readlines():
    	lineArr = line.strip().split('\t')
    	dataMat.append([float(lineArr[0]), float(lineArr[1])])
        labelMat.append(float(lineArr[2]))
    return dataMat, labelMat


def selectJrand(i,m):
    j=i
    while( j==i ):
        j = int(random.uniform(0, m))
    return j

def clipAlpha(aj, H, L):
	if aj > H:
		aj = H
	if aj < L:
		aj = L
	return aj


def smoSimple(dataMatIn, classLabels, C, toler, maxIter):
	dataMatrix = mat(dataMatIn)
	labelMat = mat(classLabels).transpose()
	b = 0
	m, n = shape(dataMatIn)
	alphas = mat(zeros((m, 1)))

	#print labelMat
	#print alphas
	iter = 0
	while( iter < maxIter ):
		alphaPairsChanged = 0
		for i in range(m):
		    fXi = float(multiply(alphas, labelMat).T * (dataMatrix * dataMatrix[i,:].T)) + b
		    print fXi
		    Ei = fXi - float(labelMat[i])
		    if (labelMat[i]*Ei < -toler) and (alphas[i] < C) or ( (labelMat[i]*Ei > toler) and (alphas[i] > 0) ):
		    	j = selectJrand(i, m)

		iter = maxIter


if __name__ == '__main__':
    dataMat, labelMat = loadDataSet('testSet.txt')
    #print dataMat
    #print labelMat

    smoSimple(dataMat, labelMat, 0.6, 0.001, 40)