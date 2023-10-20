import pygame
from pygame.locals import *
import random

class Game():
    def __init__(self):
        self.KEYS = [K_UP, K_DOWN, K_LEFT, K_RIGHT]
        self.running = True
        self.clock = pygame.time.Clock()
        self.screen_size = 700
        self.game_res = 15
        self.screen = pygame.display.set_mode((self.screen_size,self.screen_size))
        pygame.display.set_caption("snake")
        self.pos = (self.game_res//2,self.game_res//2)  #(x,y)
        self.dir = (0,-1)
        self.snake = [(self.pos), None, None]
        self.square = self.screen_size//self.game_res
        self.is_blob = False
        self.blob_loc = (-1,-1) #initilizing as (0,0) saves several checks for not beig None

    def draw_screen(self):
        self.screen.fill((0,0,0))
        snake_parts = []
        for i in self.snake:
            if i != None:
                snake_parts.append(pygame.rect.Rect(i[0]*self.square,i[1]*self.square,self.square,self.square))
        for i in snake_parts:
            pygame.draw.rect(self.screen, (255,255,255), i)
        pygame.draw.rect(self.screen, (255,255,255), pygame.rect.Rect(self.blob_loc[0]*self.square + self.square/4, self.blob_loc[1]*self.square + self.square/4, self.square/2, self.square/2))
        pygame.display.flip()

    def start_screen(self):
        ...
        #Classic mode
        #Boxed mode

        #Option to chnage the size

    def end_screen(self):
        ...

    def change_direction(self, key):
        if key == K_UP and self.dir != (0,1):
            self.dir = (0,-1)
            return True
        elif key == K_RIGHT and self.dir != (-1,0):
            self.dir = (1,0)
            return True
        elif key == K_LEFT and self.dir != (1,0):
            self.dir = (-1,0)
            return True
        elif key == K_DOWN and self.dir != (0,-1):
            self.dir = (0,1)
            return True
        else:
            return False

    def evaluate(self):
        #TODO: Add border (depends on game mode)
        if self.pos == self.blob_loc:
            self.snake.append(None)
            self.is_blob = False
        if self.pos in self.snake[1:]:
            self.running = False

    def move(self):
        self.pos = (self.pos[0] + self.dir[0], self.pos[1] + self.dir[1])
        for i in range(len(self.snake)-1,-1,-1):
            if i != 0:
                self.snake[i] = self.snake[i-1]
            else:
                self.snake[i] = self.pos

    def blop(self):
        if not self.is_blob:
            while True:
                location = (random.randint(0,self.game_res-1),random.randint(0,self.game_res-1))
                if location not in self.snake:
                    self.is_blob = True
                    self.blob_loc = location
                    return 0
            
