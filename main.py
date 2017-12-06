from math import sqrt, pow
import random
import pygame

white = (255,255,255)


class City:
    def __init__(self, n, x, y):
        self.n = n
        self.x = x
        self.y = y

    def __str__(self):
        return "name : {0} coords : ({1},{2})".format(self.n, self.x, self.y)

    '''static func to return dist between two cities '''
    def score(v1, v2):
        return sqrt(pow(v2.x - v1.x, 2)+pow(v2.y - v1.y, 2))

    def tailleProblem(self):
        return len(self.problem)

def mutation(solutions, chance_mutate):
    for sol in solutions:
        for pos1 in range(0, sol.getLength()-1):
            if random.random() < chance_mutate:
                pos2 = int(sol.getLength() * random.random())
                city1 = sol.getCity(pos1)
                city2 = sol.getCity(pos2)
                sol.setCity(pos1, city2)
                sol.setCity(pos2, city1)

def crossover(s1,s2):
    length = len(s1.sol)
    start = random.randint(0,length-1)
    stop = random.randint(start + 1,length)
    #print("start : {:d} stop : {:d}".format(start, stop))

    selected_cities_y = s2.sol[start:stop]
    selected_cities_x = s1.sol[start:stop]

    print("start : {:d} stop : {:d}".format(start, stop))


    print("selected cities in x : " )
    for s in selected_cities_x:
        print(s.n)
    print("selected cities in y : " )
    for s in selected_cities_y:
        print(s.n)

    s1.seq_print()
    s2.seq_print()

    for i in range(0, len(s2.sol)):
        if s1.sol[i] in selected_cities_y:
            s1.selectedIndices.append(i)
            s1.sol[i] = None

    for i in range(0, len(s1.sol)):
        if s2.sol[i] in selected_cities_x:
            s2.selectedIndices.append(i)
            s2.sol[i] = None

    print(s1.selectedIndices)
    print(s2.selectedIndices)

    s1.seq_print()
    s2.seq_print()

    child1_l = [None] * len(s1.sol)
    child2_l = [None] * len(s2.sol)

    for c in s2.sol[stop:-1]:
        i = start
        if c is not None:
            child2_l[i] = c
            i+=1

    for c in s2.sol[0:start-1]:
        i = 0
        if c is not None:
            child2_l[i] = c
            i+=1




class Solution:
    def __init__(self, problem = None, init = True):
        if (init):
            self.sol = random.sample(problem, len(problem))
        else:
            self.sol = list()
        self.selectedIndices = list()

    def score(self):
        tot = 0
        for i in range(len(self.sol) - 1):
            tot+= City.score(self.sol[i], self.sol[i+1])
        return tot

    def setCity(self, pos, city):
        self.sol[pos] = city

    def getCity(self, pos):
        return self.sol[pos]

    def getLength(self):
        return len(self.sol)

    def legal(self):
        return len(self.sol) is len(set(self.sol))   #source : https://stackoverflow.com/questions/5278122/checking-if-all-elements-in-a-list-are-unique

    def screenPrint(self, screen):
        for i in range(len(self.sol) -1):
            pygame.draw.line(screen, white, (self.sol[i].x, self.sol[i].y), (self.sol[i+1].x, self.sol[i+1].y), 2)

    def seq_print(self):
        string = ""
        for e in self.sol:
            if e is None:
                string+= "* "
            else:
                string+= e.n + " "

        string += "\n"
        print(string)



'''
    def crossover(s1, s2):
        children = []
        length = len(s1.sol)
        start = random.randint(0,length-1)
        stop = random.randint(start + 1,length)
        for i in range(start, stop):
            if i > start and i < stop:
                child1 = s1[i]
'''


if __name__ == "__main__":
    #usage : python main.py [time limit] [maximum gen] [path]
    import sys
    import time
    problem = list()
    path = ""
    maxGen = int(sys.argv[2])

    timelimit = float(sys.argv[1])
    print("maxGen : {:d}".format(maxGen))


    circle_color = (100,200,200)
    (width, height) = (500, 500)
    screen = pygame.display.set_mode((width, height))

    if len(sys.argv) is 4:
        path = sys.argv[3]
        with open(path) as f:
            for line in f:
                #get data from file
                words = line.split()
                problem.append(City(words[0], int(words[1]), int(words[2])))
            for e in problem:
                #print city on screen
                pygame.draw.circle(screen, circle_color, (e.x, e.y), 30, 3)
                pygame.display.flip()


    else:
        running = True
        while running:
            #get data
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x,y = pygame.mouse.get_pos()
                    problem.append(City("v{:d}".format(len(problem)), x, y))

                #if event.type is pygame.KEYDOWN and event.key is pygame.K_ESCAPE:
                    #Run gen. Algo

                if event.type == pygame.QUIT:
                    running = False

            for c in problem:
                pygame.draw.circle(screen, circle_color, (c.x, c.y), 10, 3)
            pygame.display.flip()

    #start searching

    time.clock()
    popSize = 2
    solutions = list()
    nGen = 0
    #init
    for i in range(popSize * 2):
        solutions.append(Solution(problem))
    while True:
        #Selection
        solutions = sorted(solutions, key=lambda x : x.score()) #elitiste
        #Crossover
        newSol = list()
        bestPool = solutions[popSize:] #Halves solution ary
        crossover(solutions[0], solutions[1])
        #Mutation
        nGen+=1
        if time.clock() >= timelimit or nGen == maxGen:
            break






    #for i in range(10):
    #    print(solutions_sorted[i].score())

    #pygame.display.flip()
    #mutation(solutions_sorted)




    print("Search ended after {:f} seconds and {:d} generations".format(time.clock(), nGen))
