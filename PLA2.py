############################# Machine Learning Foundation 1-16 ##############################

#encoding: utf-8
# visting the sample randomly
# recursion PLA 2000

import numpy
import random

class NaiveCyclePLA(object):
    # dimension: row
    # count: column
    def __init__(self, dimension, count):
        self.dimension = dimension
        self.count = count

    def train_matrix(self, path):
        training_set = open(path)
        training_set2 = []
        
################## here #############################
        # random example
        for line in training_set:
            training_set2.append(line)
        random.shuffle(training_set2)

        x_train = numpy.zeros((self.count, self.dimension))
        y_train = numpy.zeros((self.count, 1))
        x_count = 0
        for line in training_set2:
            x = []
            x.append(1)    # x0 = 1
            for str in line.split(' '):
                if len(str.split('\t')) == 1:    # x data
                    x.append(float(str))
                else:                            # y value
                    x.append(float(str.split('\t')[0]))
                    y_train[x_count, 0] = int(str.split('\t')[1].strip())
            x_train[x_count, :] = x
            x_count += 1
        return x_train, y_train

    def iteration_count(self, path):
        count = 0
        x_train, y_train = self.train_matrix(path)
        w = numpy.zeros((self.dimension, 1))    # initial w0 = 0
        while True:
            flag = 0
            for i in range(self.count):
                if numpy.dot(x_train[i,:], w) * y_train[i] <= 0:    # x*W*y <= 0 need to correct
                    w += y_train[i, :] * x_train[i, :].reshape(5, 1)    # w(t + 1) = w(t) + x(i) * y(i)
                    count += 1
                    flag = 1
            if flag == 0:
                break
        return count

# calculat the count in data
f = open('/Users/mileszero/Documents/py/test/data.txt')
num = 0
for line in f:
    num += 1

# create e NavieCyclePLA class
p = NaiveCyclePLA(5, num)

c = 0
# call th efunction to calculate the count in NavieCyclePLA class
for i in range(2000):
    c += p.iteration_count('/Users/mileszero/Documents/py/test/data.txt')
print c/2000



































