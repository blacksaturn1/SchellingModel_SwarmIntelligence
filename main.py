from gridworld import Grid
import pygame
from functools import partial
from schellingmodel import SchellingModel
import math
import argparse
import json


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

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
                    prog='Schelling Model Simulator',
                    description='IMplements single move cell of Schelling Model'
                    )
    parser.add_argument('-happinessCount', required=False,help='happinessCount as dictionary')
    parser.add_argument('-populationDensity', required=False,help='populationDensity')

    args = parser.parse_args()
    happinessCount = json.loads(args.happinessCount)
    assert(len(happinessCount)>0 and len(happinessCount)<3) # we only want to allow 2 happinessCount
    populationDensity = float(args.populationDensity)
    isX=False
    counter=0
    isActive=False
    grid = Grid(50, 50, 17, 17, title='Schelling Model', margin=1,framerate=10)

    #grid = Grid(20, 20, 40, 40, title='Schelling Model', margin=1,framerate=10)
        # grid.set_cell_click_action(partial(cell_click, grid=grid))
        #grid.set_cell_click_action(cell_click)
    #grid.set_timer_action(partial(timer_action, grid,isX,counter))
    
    grid.set_drawaction('O', draw_O) # Green
    grid.set_drawaction('X', draw_X) # Red
    
    model = SchellingModel(grid,populationDensity,happinessCount=happinessCount)
    # grid.set_timer_action(model.timer_action)
    grid.set_timer_action(model.run_sim)

    model.setup()
    
    grid.run()

#pygame.display.flip()