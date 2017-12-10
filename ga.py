import sys
import time
import random
import pygame
from math import sqrt

cities = list()

random.seed(1337)
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

class Solution:
    def __init__(self, init = True):
        self.ary = list()
        if init:
            indices = range(0, len(cities))
            self.ary = random.sample(indices, len(indices))


    def score(self):
        sum = 0
        for i in range(0, len(cities)-1):
            sum += City.score(cities[self.ary[i]], cities[self.ary[i+1]])
        return sum

    def crossover(s1, s2):
        length = len(cities)
        start = random.randint(0,length-1)
        stop = random.randint(start + 1,length)

        #on stocke les indices qu'on doit changer
        indices_selectionnes_x = s1.ary[start:stop]
        indices_selectionnes_y = s2.ary[start:stop]

        #preparation
        for i,n in enumerate(s1.ary):
            if n in indices_selectionnes_y:
                s1.ary[i] = "*"

        for i,n in enumerate(s2.ary):
            if n in indices_selectionnes_x:
                s2.ary[i] = "*"

        #print(indices_selectionnes_x)
        #print(indices_selectionnes_y)

        #print("s1 : ", s1.ary)
        #print("s2 : ", s2.ary)
        #tassement
        Solution.compress(s1.ary, start, stop)
        Solution.compress(s2.ary, start, stop)

        #echange
        s1.ary[start:stop] = indices_selectionnes_y
        s2.ary[start:stop] = indices_selectionnes_x

        childx = Solution(False)
        childy = Solution(False)

        childx.ary = s1.ary
        childy.ary = s2.ary
        #print("child 1",  childx.ary)
        #print("child 2", childy.ary)
        return childx, childy

    def compress(ary, start, stop):
        temp = list()
        for i in range(stop, len(ary)):
            if ary[i] != "*":
                temp.append(ary[i])


        for i in range(0, stop):
            if ary[i] != "*":
                temp.append(ary[i])

        temp.reverse()

        for i in range(stop, len(ary)):
            ary[i] = temp.pop()

        for i in range(0, start):
            ary[i] = temp.pop()

        for i in range(start, stop):
            ary[i] = "*"

        return ary

def ga_solve(file = None, gui=True, maxTime=0):
    circle_color = (100,200,200)
    line_color = (200,200,200)
    red = (255, 0, 0)
    (width, height) = (500, 500)

    if file == None:
        screen = pygame.display.set_mode((width, height))
        running = True
        while running:
            #get data
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x,y = pygame.mouse.get_pos()
                    cities.append(City("v{:d}".format(len(cities)), x, y))

                if event.type is pygame.KEYDOWN and event.key is pygame.K_ESCAPE:
                    ga_solve(None, True, maxTime)

                if event.type == pygame.QUIT:
                    running = False

            for c in cities:
                pygame.draw.circle(screen, circle_color, (c.x, c.y), 10, 3)
            pygame.display.flip()
    else:
        with open(file) as f:
            for line in f:
                #get data from file
                words = line.split()
                cities.append(City(words[0], int(words[1]), int(words[2])))
                screen = pygame.display.set_mode((width, height))

    time.clock()
    popSize = 4
    solutions = list()
    nGen = 0
    for i in range(popSize):
        solutions.append(Solution(True))

    bestScore = solutions[0].score()
    bestPath = solutions[0].ary
    while True:
        #pour l'instant on croise la meilleure moitié du tableau et l'autre moitié on refait random, c'est pas terrible faudrait revoir ça ..
        #ptêtre c'est précisé dans le pdf, je sais pas trop comment faire
        #selection
        solutions = sorted(solutions, key=lambda x : x.score()) #elitiste
        if solutions[0].score() < bestScore:
            bestScore = solutions[0].score()
            bestPath = solutions[0].ary
        #mutation
        #ça faut faire
        #crossover

        #première partie du tableau remplacée par les enfants
        for i in range(int((len(solutions)/2))-1):
            c1, c2 = Solution.crossover(solutions[i], solutions[i+1])
            solutions[i] = c1
            solutions[i+1] = c2
        #deuxième partie du tableau random
        for i in range(int(len(solutions)/2), len(solutions)):
            solutions[i] = Solution(True)
        print("Best score : ", bestScore)
        nGen+=1
        print("gen number : ", nGen)
        #affichage
        if gui:
            #clear le screen
            screen.fill((0, 0, 0))
            points = None
            points = list()
            bestpoints = None
            bestpoints = list()
            #on rajoute tout le parcours dans une liste de points
            for i in range(len(solutions[0].ary)):
                points.append((cities[solutions[0].ary[i]].x,cities[solutions[0].ary[i]].y))
                bestpoints.append((cities[bestPath[i]].x, cities[bestPath[i]].y))
            #on affiche les points
            pygame.draw.lines(screen, line_color, False, points, 1)
            pygame.draw.lines(screen, red, False, bestpoints, 1)

            #on ajoute des cercles pour les villess
            for c in cities:
                pygame.draw.circle(screen, circle_color, (c.x, c.y), 10, 3)
            #et on display le tout
            pygame.display.flip()

        #fin affichage
        if time.clock() >= maxTime:
            break
