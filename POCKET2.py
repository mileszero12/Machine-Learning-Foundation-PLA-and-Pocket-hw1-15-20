################################ Machine Learnning Foundation 1-20 ###################################

# encoding: utf-8

import numpy
import random
import copy

class POCKET(object):
    # dimension is the col numbers of data
    # count is the row numbers of data
    # tDimension is the col numbers of test
    # tCount is the row numbers of test
    # train_count is the limited number by using POCKET
    def __init__(self, dimension, count, tDimension, tCount, train_count):
        self.dimension = dimension
        self.count = count
        self.tDimension = tDimension
        self.tCount = tCount
        self.train_count = train_count
    
    
    # get the formal data of x and y from the training data set
    def data(self, path):
        dat = open(path)
        dat2 = []
        
        for line in dat:
            dat2.append(line)
        random.shuffle(dat2)
        
        
        xdat = numpy.zeros((self.count, self.dimension))
        ydat = numpy.zeros((self.count, 1))
        count = 0
        
        for line in dat2:
            temp = []
            temp.append(1)
            
            for str in line.split(' '):
                if len(str.split('\t')) == 1:
                    temp.append(float(str))
                else:
                    temp.append(float(str.split('\t')[0]))
                    ydat[count, 0] = int(str.split('\t')[1].strip())
            xdat[count, :] = temp
            count += 1
        return xdat, ydat
            
            
            
            # get formal data of x and y from testing data set
    def test(self, path2):
        test = open(path2)
        
        xtest = numpy.zeros((self.tCount, self.tDimension))
        ytest = numpy.zeros((self.tCount, 1))
        count = 0
        
        for line in test:
            temp = []
            temp.append(1)
            
            for str in line.split(' '):
                if len(str.split('\t')) == 1:
                    temp.append(float(str))
                else:
                    temp.append(float(str.split('\t')[0]))
                    ytest[count, 0] = int(str.split('\t')[1].strip())
            xtest[count, :] = temp
            count += 1
        return xtest, ytest
            
            
            
            # using POCKET PLA to calculate best w
    def countW(self, path, path2):
        countNum = 0
        num_Best = self.train_count
        xdat, ydat = self.data(path)
        w = numpy.zeros((self.dimension, 1))
        w_best = numpy.zeros((self.dimension, 1))
        xtest, ytest = self.test(path2)

        for i in range(self.count):
            if numpy.dot(xdat[i, :], w) * ydat[i,:] <= 0:
                w += 0.5 * ydat[i,:] * xdat[i,:].reshape(5, 1)
                countNum += 1
                
                # test whether the new w is a good one by counting it mistakes(in tset data set)
                numErr = 0
                for j in range(self.tCount):
                    if numpy.dot(xtest[j, :], w) * ytest[j,:] <= 0:
                        numErr += 1
            
                if numErr < num_Best:    # if new w makes fewer mistake, replace w by the new one
                    num_Best = numErr
                    w_best = copy.deepcopy(w)

            if countNum == self.train_count:    # if there is already enough time, we should halt
                break
        return w_best



    # using test data to check the error rate under the best w
    def CalError(self, path, path2):
        xtest, ytest = self.test(path2)
        w = self.countW(path, path2)
        
        errorNum = 0.0    # point!!!!! float, because it need to divide
        for i in range(self.tCount):
            if numpy.dot(xtest[i, :], w) * ytest[i, :] <= 0:
                errorNum += 1
        return errorNum / self.tCount

f = open('/Users/mileszero/Documents/py/test/train2.txt')
num1 = 0
for line in f:
    num1 += 1

f2 = open('/Users/mileszero/Documents/py/test/test2.txt')
num2 = 0
for line in f2:
    num2 += 1


c = 0.0000
# call th efunction to calculate the count in NavieCyclePLA class
for i in range(2000):
    print i
    # create e NavieCyclePLA class
    p = POCKET(5, num1, 5, num2, 100)
    c += p.CalError('/Users/mileszero/Documents/py/test/train2.txt', '/Users/mileszero/Documents/py/test/test2.txt')
print c/2000
















