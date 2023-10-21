import pygame
from pygame.locals import *
from components import *

def game_loop():
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
        game.clock.tick(6)
    game.running = True
    game.end_screen()



if __name__ == "__main__":
    game_loop()