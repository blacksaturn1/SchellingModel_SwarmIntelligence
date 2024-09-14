from .gridworld import Grid
import pygame

grid = Grid(50, 50, 16, 16, title='Schelling Model', margin=1)
    # grid.set_cell_click_action(partial(cell_click, grid=grid))
    #grid.set_cell_click_action(cell_click)



grid.run()

