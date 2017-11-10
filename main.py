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
    def score(v1, v2):
        return sqrt(pow(v2.x - v1.x, 2)+pow(v2.y - v1.y, 2))

class Solution:
    def __init__(self, problem, init = True):
        if (init):
            self.sol = random.sample(problem, len(problem))
        else:
            self.sol = list()

    def score(self):
        tot = 0
        for i in range(len(self.sol) - 1):
            tot+= City.score(self.sol[i], self.sol[i+1])
        return tot

    def legal(self):
        return len(self.sol) is len(set(self.sol))   #https://stackoverflow.com/questions/5278122/checking-if-all-elements-in-a-list-are-unique

    def crossover(self, s1, s2):
        child = None
        #todo

    def swap(sol1, sol2, index):
        temp = Solution(problem, False)
        for i in range(len(sol1.sol)):
            if i < index:
                temp.sol.append(sol1.sol[i])
            else:
                temp.sol.append(sol2.sol[i])
        return temp



#populating our city list
problem = list()

with open('data/pb005.txt') as f:
    for line in f:
        words = line.split()
        problem.append(City(words[0], int(words[1]), int(words[2])))

sols = list()
for i in range(0, 1000):
    sols.append(Solution(problem))

sols.sort(key=lambda sol : sol.score())

print(sols[0].score())
for e in sols[0].sol:
    print(e.n)
