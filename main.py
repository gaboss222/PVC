from math import sqrt, pow
import random
import pygame

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

if __name__ == "__main__":
    #usage : python main.py [time limit] [maximum gen] [path]
    import sys
    import time
    problem = list()
    path = ""
    maxGen = int(sys.argv[2])

    timelimit = float(sys.argv[1])
    
    white = (255,255,255)
    circle_color = (100,200,200)
    (width, height) = (300, 300)
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

    mutation(problem)
    
    time.clock()
    nGen = 0
    while True:
        #Search happens there
        if time.clock() > timelimit or nGen is maxGen:
            break
        nGen+=1
        
        
