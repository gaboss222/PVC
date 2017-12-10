from math import sqrt, pow
import random
import pygame

white = (255,255,255)


#City class
class City:

    #City has name and coords (x,y)
    def __init__(self, n, x, y):
        self.n = n
        self.x = x
        self.y = y

    def __str__(self):
        return "name : {0} coords : ({1},{2})".format(self.n, self.x, self.y)

    #return dist between two cities
    def score(v1, v2):
        return sqrt(pow(v2.x - v1.x, 2)+pow(v2.y - v1.y, 2))

    def tailleProblem(self):
        return len(self.problem)


#Mutate
def mutate(solutions, chance_mutate):
    for sol in solutions:
        for pos1 in range(0, sol.getLength()-1):
            if random.random() < chance_mutate:
                pos2 = int(sol.getLength() * random.random())
                city1 = sol.getCity(pos1)
                city2 = sol.getCity(pos2)
                sol.setCity(pos1, city2)
                sol.setCity(pos2, city1)


def crossover(parcours1,parcours2):
    length = len(parcours1.sol)
    print("length : ", length)
    start = random.randint(0,length-1)
    stop = random.randint(start + 1,length)
    #print("start : {:d} stop : {:d}".format(start, stop))

    #Select cities between start and stop for each parcours
    selected_cities_y = parcours2.sol[start:stop]
    selected_cities_x = parcours1.sol[start:stop]


    print("start : {:d} stop : {:d}".format(start, stop))


    #diplay selected cities
    print("selected cities in parcours 1 : " )
    for s in selected_cities_x:
        print(s.n)
    print("selected cities in parcours 2 : " )
    for s in selected_cities_y:
        print(s.n)

    #Display cities
    print("\nParcours 1 ")
    parcours1.seq_print()
    print("\nParcours 2 ")
    parcours2.seq_print()

    indice_x = list()
    indice_y = list()
    #Parcou
    for i in range(0, len(parcours2.sol)):
        if parcours1.sol[i] in selected_cities_y:
            parcours1.selectedIndices.append(i)
            parcours1.sol[i] = None


    for i in range(0, len(parcours1.sol)):
        if parcours2.sol[i] in selected_cities_x:
            parcours2.selectedIndices.append(i)
            parcours2.sol[i] = None


    print('Indices selectionnées parcours 1 : ', parcours1.selectedIndices)
    print('Indices selectionnées parcours 2 : ', parcours2.selectedIndices)

    parcours1.seq_print()
    parcours2.seq_print()


    child = list()
    child2_l = [None] * len(parcours2.sol)

    #Parcours du point stop à la fin de la liste
    for c in parcours2.sol[stop:len(parcours2.sol)-1]:
        i = start
        if c is not None:
            child[i] = c.n
            i+=1

    for c in parcours2.sol[0:start-1]:
        i = 0
        if c is not None:
            print(c.n)
            child[i] = c.n
            i+=1
    return child



#Class for solution(List of cities visited)
class Solution:
    def __init__(self, problem = None, init = True):
        if (init):
            self.sol = random.sample(problem, len(problem))
        else:
            self.sol = list()
        self.selectedIndices = list()

#Return dist totale
    def distTotale(self):
        tot = 0
        for i in range(len(self.sol) - 1):
            tot+= City.score(self.sol[i], self.sol[i+1])
        return tot
#Set a city to a position
    def setCity(self, pos, city):
        self.sol[pos] = city

#Get city according to a position
    def getCity(self, pos):
        return self.sol[pos]

#Return length
    def getLength(self):
        return len(self.sol)

#Check if a city doesn't appear twice
    def legal(self):
        return len(self.sol) is len(set(self.sol))   #source : https://stackoverflow.com/questions/5278122/checking-if-all-elements-in-a-list-are-unique

#Draw distance
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

def ga_solve(file=None, gui=True, maxtime=0):
    #start searching
    time.clock()
    popSize = 2
    solutions = list()
    nGen = 0
    print("tets")
    #init
    for i in range(popSize * 2):
        solutions.append(Solution(problem))

    print(solutions)
    while True:
        #Selection
        solutions_sorted = sorted(solutions, key=lambda x : x.distTotale()) #elitiste
        #Crossover
        newSol = list()
        bestPool = solutions[popSize:] #Halves solution ary
        crossover(solutions[0], solutions[1])
        #Mutation
        nGen+=1
        if time.clock() >= timelimit or nGen == maxGen:
            break


    for i in range(2):
        print(solutions_sorted[i].distTotale())

    #pygame.display.flip()
    mutate(solutions_sorted)



    print("Search ended after {:f} seconds and {:d} generations".format(time.clock(), nGen))


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
        ga_solve(path, True, timelimit)


    else:
        running = True
        while running:
            #get data
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x,y = pygame.mouse.get_pos()
                    problem.append(City("v{:d}".format(len(problem)), x, y))

                if event.type is pygame.KEYDOWN and event.key is pygame.K_ESCAPE:
                    ga_solve(None, True, timelimit)

                if event.type == pygame.QUIT:
                    running = False

            for c in problem:
                pygame.draw.circle(screen, circle_color, (c.x, c.y), 10, 3)
            pygame.display.flip()
