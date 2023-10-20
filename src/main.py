import pygame
from pygame.locals import *
from components import *

def game_loop():
    game = Game()
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
        game.clock.tick(6)



if __name__ == "__main__":
    game_loop()