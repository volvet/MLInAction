
def loadDataSet(fileName):
    dataMat = []; labelMat = []
    fr = open(fileName)
    for line in fr.readlines():
    	lineArr = line.strip().split('\t')
    	dataMat.append([float(lineArr[0]), float(lineArr[1])])
        labelMat.append(float(lineArr[2]))
    return dataMat, labelMat




if __name__ == '__main__':
    dataMat, labelMat = loadDataSet('testSet.txt')
    print dataMat
    print labelMat