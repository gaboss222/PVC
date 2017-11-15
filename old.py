from math import sqrt, pow
import random

testmode = True


#classes
class City:
    def __init__(self, id, n, x, y):
        self.id = id
        self.n = n
        self.x = x
        self.y = y
    def __str__(self):
        return "name : {0}\n coords : ({1},{2})".format(self.n, self.x, self.y)
    '''static func to return dist between two cities '''
    def score(v1, v2):
        return sqrt(pow(v2.x - v1.x, 2)+pow(v2.y - v1.y, 2))

class Solution:
    def __init__(self, problem, init = True, input = None):
        if (init):
            self.sol = random.sample(problem, len(problem))
        elif input is None:
            self.sol = list()
        else:
            self.sol = input


    def score(self):
        tot = 0
        for i in range(len(self.sol) - 1):
            tot+= City.score(self.sol[i], self.sol[i+1])
        return tot

    def legal(self):
        return len(self.sol) is len(set(self.sol))   #source : https://stackoverflow.com/questions/5278122/checking-if-all-elements-in-a-list-are-unique

    def crossover(s1, s2):
        length = len(s1.sol)
        start = random.randint(0,length-1)
        start2 = random.randint(0, length-1)
        stop = random.randint(start + 1,length)
        stop2 = random.randint(start + 1, length)

        #print("{:d} : {:d}".format(start, stop))
        newSol = s1.sol[start:stop]
        left = length - len(newSol)

        newSol2 = s1.sol[start2:stop2]
        left = length - len(newSol2)

        for e in s2.sol:
            if e not in newSol:
                newSol.append(e)
            if e not in newSol2:
                newSol2.append(e)



        nS = Solution(problem, False, newSol)
        nS2 = Solution(problem, False, newSol2)
        return nS, nS2
        #print(nS.printPath())

    def printPath(self):
        for e in self.sol:
            print("{:s} ->".format(e.n), end = ' ')

'''
    def swap(self, sol1, sol2, index):
        temp = Solution(problem, False)
        for i in range(len(sol1.sol)):
            if i < index:
                temp.sol.append(sol1.sol[i])
            else:
                temp.sol.append(sol2.sol[i])
        return temp
'''


#populating our city list
problem = list()

with open('data/pb005.txt') as f:
    i = 0
    for line in f:
        words = line.split()
        problem.append(City(i, words[0], int(words[1]), int(words[2])))

sols = list()




















'''
   #print("generation #{:d}".format(i))
    sols.append(Solution(problem))
    sols.append(Solution(problem))
    #for f in sols:
    #    for e in f.sol:
    #        print(str(e))
    sols.sort(key=lambda sol : sol.score())
    #print("sol length", len(sols))
    print("Score : {:f}".format(sols[0].score()))
    if (random.randint(0, 100) < 10):
        newGen = Solution(problem)
        newGen2 = Solution(problem)
    else:
        newGen = Solution.crossover(sols[0], sols[1])
        newGen2 = Solution.crossover(sols[0], sols[1])
    sols.pop()
    sols.pop()
    print(len(sols))
    sols.append(newGen)
    sols.append(newGen2)

    #print("appending")
    #for f in sols:
    #    for e in f.sol:
    #        print(str(e))
'''
