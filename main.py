from math import sqrt, pow
import random

testmode = True


#classes
class City:
    def __init__(self, n, x, y):
        self.n = n
        self.x = x
        self.y = y
    def __str__(self):
        return "name : {0}\n coords : ({1},{2})".format(self.n, self.x, self.y)
    '''static func to return dist between two cities '''
    def dist(v1, v2):
        return sqrt(pow(v2.x - v1.x, 2)+pow(v2.y - v1.y, 2))

class Solution:
    def __init__(self, problem):
        self.sol = random.sample(problem, len(problem))
        for s in self.sol:
            print(str(s))

    def getTotalDistance(self):
        tot = 0
        for i in range(len(self.sol) - 1):
            tot+= City.dist(self.sol[i], self.sol[i+1])
        return tot


#populating our city list
problem = list()

with open('data/pb005.txt') as f:
    for line in f:
        words = line.split()
        problem.append(City(words[0], int(words[1]), int(words[2])))

s = Solution(problem)
print("Distance totale : {:f}".format(s.getTotalDistance()))
