from gridworld import Grid
import pygame
from functools import partial
from schellingmodel import SchellingModel
import math




#global isX, counter, grid

    #pygame.display.flip()

def draw_O(grid, cell_dimensions):
    
    LIGHTGRAY = (192, 192, 192)
    GRAY = (128, 128, 128)
    DARKGRAY = (45, 45, 45)
    BROWN= (150, 75, 0)
    GREEN= (0, 255, 0)
    RED= (255, 0, 0)
    # Background
    pygame.draw.rect(grid.screen, LIGHTGRAY, cell_dimensions)
    
    # Circle
    x, y, w, h = cell_dimensions
    center = (x + math.floor(w/2), y + math.floor(h/2))
    pygame.draw.circle(grid.screen, GREEN, center, w*2/5 )

def draw_X(grid, cell_dimensions):
    LIGHTGRAY = (192, 192, 192)
    GRAY = (128, 128, 128)
    DARKGRAY = (45, 45, 45)
    BROWN= (150, 75, 0)
    GREEN= (0, 255, 0)
    RED= (255, 0, 0)

    # Background
    pygame.draw.rect(grid.screen, LIGHTGRAY, cell_dimensions)
    
    # Circle
    x, y, w, h = cell_dimensions
    center = (x + math.floor(w/2), y + math.floor(h/2))
    pygame.draw.circle(grid.screen, RED, center, w*2/5 )
#pygame.draw.circle(screen, color, (400,300), 75)
if __name__ == '__main__':
    
    isX=False
    counter=0
    isActive=False
    grid = Grid(50, 50, 17, 17, title='Schelling Model', margin=1,framerate=10)
        # grid.set_cell_click_action(partial(cell_click, grid=grid))
        #grid.set_cell_click_action(cell_click)
    #grid.set_timer_action(partial(timer_action, grid,isX,counter))
    
    grid.set_drawaction('O', draw_O)
    grid.set_drawaction('X', draw_X)
    
    model = SchellingModel(grid,.8,happinessCount=3)
    # grid.set_timer_action(model.timer_action)
    grid.set_timer_action(model.run_sim)

    model.setup()
    
    grid.run()

#pygame.display.flip()