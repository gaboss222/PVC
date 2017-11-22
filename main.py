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
        return "name : {0}\n coords : ({1},{2})".format(self.n, self.x, self.y)
    '''static func to return dist between two cities '''
    def score(v1, v2):
        return sqrt(pow(v2.x - v1.x, 2)+pow(v2.y - v1.y, 2))

    def tailleProblem(self):
        return len(self.problem)


def mutation(cities):
    for c in cities:
        #print(c)
        if random.random() < 0.015:
            c2 = int(len(cities) * random.random())




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

    def pyprint(self, screen):
        for i in range(len(self.sol) - 1):
            pygame.drawlline(screen, pink, (self.sol[i].x, self.sol[i].y), (self.sol[i+1].x, self.sol[i+1].y), width=1)

    def legal(self):
        return len(self.sol) is len(set(self.sol))   #source : https://stackoverflow.com/questions/5278122/checking-if-all-elements-in-a-list-are-unique

    def screenPrint(self, screen):
        for i in range(len(self.sol) -1):
            pygame.draw.line(screen, white, (self.sol[i].x, self.sol[i].y), (self.sol[i+1].x, self.sol[i+1].y), 2)


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
    solutions = list()
    time.clock()
    for i in range(1000):
        solutions.append(Solution(problem))

    solutions_sorted = sorted(solutions, key=lambda x : x.score())

    for i in range(10):
        print(solutions_sorted[i].score())
    pygame.display.flip()

    solutions_sorted[0].screenPrint(screen)

    pygame.display.flip()
    mutation(problem)


    nGen = 0
    while True:
        #Search happens there
        if time.clock() >= timelimit or nGen >= maxGen:
            break
        nGen+=1

    print("Search ended after {:f} seconds and {:d} generations".format(time.clock(), nGen))
