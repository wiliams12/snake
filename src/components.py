import pygame
from pygame.locals import *
import random
from pygame_assets import *

"""
Defeines the Game class.
"""

class Game():
    def __init__(self):
        """
        Sets up pygame and the game engine itself.

        The self.snake is a list of snake's parts and self.pos defines the position of the head of the snake

        *For correct pygame visualisation, it is important to set screen_size to be a multiplier of game_res
        """
        self.WHITE = (255,255,255)
        self.BLACK = (0,0,0)
        self.KEYS = [K_UP, K_DOWN, K_LEFT, K_RIGHT]
        self.running = True
        self.clock = pygame.time.Clock()
        self.screen_size = 750
        self.game_res = 15
        self.screen = pygame.display.set_mode((self.screen_size,self.screen_size))
        pygame.display.set_caption("snake")
        self.pos = (self.game_res//2,self.game_res//2)
        self.dir = (0,-1)
        self.snake = [(self.pos), None, None]
        self.square = self.screen_size//self.game_res
        self.is_blob = False
        #initilizing as (-1,-1) saves several checks for being a tuple or not.
        self.blob_loc = (-1,-1)
        self.mode = None

    def draw_screen(self):
        """
        Draws all the snake parts and the blob the snake eats to the screen
        """
        self.screen.fill(self.BLACK)
        snake_parts = []
        for i in self.snake:
            if i != None:
                snake_parts.append(pygame.rect.Rect(i[0]*self.square,i[1]*self.square,self.square,self.square))
        for i in snake_parts:
            pygame.draw.rect(self.screen, self.WHITE, i)
        pygame.draw.rect(self.screen, self.WHITE, pygame.rect.Rect(self.blob_loc[0]*self.square + self.square/4, self.blob_loc[1]*self.square + self.square/4, self.square/2, self.square/2))
        pygame.display.flip()

    def start_screen(self):
        """
        Defines the starting screen of the game where the player can choose between 2 gamemodes.
        """
        def draw_self():
            self.screen.fill(self.BLACK)
            for i in buttons:
                i.draw_self(self.screen)
            txt = Text("The Snake Game", self.screen_size//2, self.screen_size//4, self.screen_size//12, self.WHITE)
            self.screen.blit(txt.txt, txt.rect)
            pygame.display.flip()

        buttons = []
        buttons.append(Button(self.screen_size,"Endless mode", (self.screen_size//2,self.screen_size//2)))
        buttons.append(Button(self.screen_size,"Boxed mode", (self.screen_size//2,self.screen_size//4*3)))

        while self.running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.running = False
                elif event.type == MOUSEBUTTONDOWN:
                    for btn in buttons:
                        if btn.pressed(event):
                            if btn.text == "Endless mode":
                                self.mode = "endless"
                            if btn.text == "Boxed mode":
                                self.mode = "boxed"
                            self.running = False

            draw_self()
        self.running = True

    def end_screen(self):
        """
        Defines what show after the end of the game. It shows the final score which is the current length of the snake - it's starting length.
        """
        self.screen.fill(self.BLACK)
        txt = Text(f"Game over, score: {len(self.snake)-3}",self.screen_size//2,self.screen_size//2,60,self.WHITE)
        self.screen.blit(txt.txt,txt.rect)
        pygame.display.flip()
        while self.running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.running = False

    def change_direction(self, key):
        """
        Handles the user input. If the correct key is pressed, the direction vector is set accordingly. It also checks whether the snake turns in 90 degrees angles.
        """
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
        """
        Checks whether an action is needed in the current state. Checks whether the snake has eaten a blob and whether it crossed it's tale.

        Boxed mode: Checks whether the snake is still in the game grid. If not, it ends the game loop.
        Endless mode: Checkes whether the snake is in the game grid. If not, it moves the self.pos to to opposite side of the grid.
        """
        if self.pos == self.blob_loc:
            self.snake.append(None)
            self.is_blob = False

        if self.pos in self.snake[1:]:
            self.running = False

        if self.mode == "boxed":
            if self.pos[0] not in list(range(0,self.game_res)) or self.pos[1] not in list(range(0,self.game_res)):
                self.running = False

        if self.mode == "endless":
            if self.pos[0] < 0:
                self.pos = (self.game_res, self.pos[1])
                self.dir = (-1, 0)
            elif self.pos[0] >= self.game_res:
                self.pos = (-1, self.pos[1])
                self.dir = (1, 0)
            elif self.pos[1] >= self.game_res:
                self.pos = (self.pos[0], -1)
                self.dir = (0, 1)
            elif self.pos[1] < 0:
                self.pos = (self.pos[0], self.game_res)
                self.dir = (0, -1)

    def move(self):
        """
        This handles the moving of the snake. The head position as updated and then every part of the snake, except the head, get's the position of the next part further from the tale. The position of the head in the list is set to the self.pos value
        """
        self.pos = (self.pos[0] + self.dir[0], self.pos[1] + self.dir[1])
        if self.snake[-1]:
            self.shade = self.snake[-1]
        for i in range(len(self.snake)-1,-1,-1):
            if i != 0:
                self.snake[i] = self.snake[i-1]
            else:
                self.snake[i] = self.pos
            

    def blop(self):
        """
        Implements the random position of the blob. It randomly generates a position and the checks whether it is possible to place it there (It isn't part of the snake)
        """
        if not self.is_blob:
            while True:
                location = (random.randint(0,self.game_res-1),random.randint(0,self.game_res-1))
                if location not in self.snake:
                    self.is_blob = True
                    self.blob_loc = location
                    return 0
            

