import pygame
from pygame.locals import *
from components import Game

"""
Imports pygame and the Game class from a module
"""

def game_loop():
    """
    The game loop uses the Game class. Check components.py for the implementation if needed
    """
    game = Game()
    game.start_screen()
    while game.running:
        for event in pygame.event.get():
            if event.type == QUIT:
                game.running = False
            elif event.type == KEYDOWN:
                if game.change_direction(event.key):
                    break
        game.draw_screen()
        game.evaluate()
        game.move()
        game.blop()
        #Limits the fps to 6 per second
        game.clock.tick(6)
    game.running = True
    game.end_screen()



if __name__ == "__main__":
    game_loop()