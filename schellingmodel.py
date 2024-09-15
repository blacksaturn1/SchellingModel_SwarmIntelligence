
from gridworld import Grid
import random
import pygame

class SchellingModel:
    def __init__(self, grid:Grid,population_density,happinessCount):
        self.__width = grid.height  # Width and height in number of cells
        self.__height = grid.width
        self.grid = grid
        self.density = population_density
        self.isX = True
        self.sim_runs=0
        self.happinessCount=happinessCount
        self.upRightDownLeft = [ [0,-1],
                        [0,1],
                        [-1,0],
                        [1,0]
                      ]
        self.upRightDownLeft = [ [-1,-1],[0,-1],[1,-1],
                                 [-1,0],         [1,0],
                                 [-1,1], [0,1], [1,1]]     

    def setup(self):
        for y in range(self.__height):        
            for x in range(self.__width):
                isCellProbability = random.random()
                if isCellProbability<= self.density:
                    isCellX = random.random()
                    if isCellX <=.5:
                        self.grid[x,y]='X'
                    else:
                        self.grid[x,y]='O'
        self.printStats()

    def printStats(self):    
        xCount=0
        oCount=0
        total=0
        for y in range(self.__height):        
            for x in range(self.__width):
                total+=1
                if self.grid[x,y]=='X':
                    xCount+=1
                if self.grid[x,y]=='O':
                    oCount+=1
        print("total:",total)
        print("X %:",xCount/total*100)

        print("O %:",oCount/total*100)

                    
    
    def countHappiness(self,x,y):
        happyCount = 0 
        for x_delta,y_delta in self.upRightDownLeft:
            if self.grid[x,y] == self.grid[x+x_delta,y+y_delta]:
                happyCount+=1
        return happyCount
    
    def move(self,x,y):
        for x_delta,y_delta in self.upRightDownLeft:
            char = self.grid[x,y]
            if x+x_delta>=0 and x+x_delta<self.__width and y+y_delta>=0 and y+y_delta<self.__height and self.grid[x+x_delta,y+y_delta] is None:
                self.grid[x+x_delta,y+y_delta]=char
                self.grid[x,y] = None
                break
        return
    
    def move2(self,x,y):
        openLocations = []
        char = self.grid[x,y]
        for x_delta,y_delta in self.upRightDownLeft:
            neighborX = x+x_delta
            neighborY = y+y_delta
            if neighborX>=0 and neighborX<self.__width and y+y_delta>=0 and y+y_delta<self.__height and self.grid[x+x_delta,y+y_delta] is None:
                openLocations.append([x+x_delta,y+y_delta])

        if len(openLocations)>0:    
            toMove = random.choice(openLocations)
            self.grid[toMove[0],toMove[1]]=char
            self.grid[x,y] = None

        return    

    def run_sim(self):
        BLACK = (0, 0, 0)

        if self.sim_runs==1000:
            return
        #global isX, counter, grid,isActive
        for y in range(self.__height):        
            for x in range(self.__width):
                #print(self.grid[x,y])
                if self.grid[x,y] is None:
                    continue
                count = self.countHappiness(x,y)
                if count< self.happinessCount:
                    self.move2(x,y)
        self.sim_runs+=1
        myFont = pygame.font.SysFont("Times New Roman", 14)

        randNumLabel = myFont.render("Simulation: ", 1, BLACK)
        ### pass a string to myFont.render
        diceDisplay = myFont.render(str( self.sim_runs), 1, BLACK)

        self.grid.screen.blit(randNumLabel, (10, 20))
        self.grid.screen.blit(diceDisplay, (10, 40))
        print("Simulation:",self.sim_runs)
        if self.sim_runs==1000:
            self.printStats()
    
    
    def timer_action(self):
        #global isX, counter, grid,isActive
        
        if self.isX:
            char='X'
        else:
            char='O'
        self.grid[self.sim_runs, self.sim_runs] = char
        
        self.isX = False if self.isX else True
        self.sim_runs+=1
        print("Simulation:",self.sim_runs)