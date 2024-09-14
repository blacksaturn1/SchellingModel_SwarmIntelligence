
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

    def setup(self):
        for x in range(self.__height):        
            for y in range(self.__width):
                isCellProbability = random.random()
                if isCellProbability<= self.density:
                    isCellX = random.random()
                    if isCellX <.5:
                        self.grid[x,y]='X'
                    else:
                        self.grid[x,y]='O'
    
    def countHappiness(self,x,y):
        happyCount = 0 
        for x_delta,y_delta in self.upRightDownLeft:
            if self.grid[x,y] == self.grid[x+x_delta,y+y_delta]:
                happyCount+=1
        return happyCount
    
    def move(self,x,y):
        return
        

    def run_sim(self):
        BLACK = (0, 0, 0)
        #global isX, counter, grid,isActive
        for y in range(self.__height):        
            for x in range(self.__width):
                print(self.grid[x,y])
                if self.grid[x,y] is None:
                    continue
                count = self.countHappiness(x,y)
                if count< self.happinessCount:
                    self.move(x,y)
        self.sim_runs+=1
        myFont = pygame.font.SysFont("Times New Roman", 18)

        randNumLabel = myFont.render("Simulation: ", 1, BLACK)
        ### pass a string to myFont.render
        diceDisplay = myFont.render(str( self.sim_runs), 1, BLACK)

        self.grid.screen.blit(randNumLabel, (10, 20))
        self.grid.screen.blit(diceDisplay, (10, 30))
        print("Simulation:",self.sim_runs)
    
    
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