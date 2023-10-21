import pygame

class Text():
    def __init__(self,text,x,y,size,color):
        pygame.font.init()
        self.text = text
        self.x = x
        self.y = y
        self.color = color
        self.font = pygame.font.SysFont('swis721wgl4',int(size),)
        self.txt = self.font.render(self.text,True,self.color)
        self.rect = self.txt.get_rect()
        self.rect.center = (self.x,self.y) 



class Button():
    def __init__(self,size,text,pos):
        self.text = text
        self.size = (4*size//8,size//8)
        self.pos = pos
        self.text = text
        self.txt = Text(self.text,*self.pos,size/16,(0,0,0))
        self.rect = pygame.rect.Rect(0,0,*self.size)
        self.rect.center = self.pos
    
    def draw_self(self,surface):
        pygame.draw.rect(surface,(255,255,255),self.rect)
        surface.blit(self.txt.txt,self.txt.rect)

    def pressed(self,event):
        if self.rect.collidepoint(event.pos):
            return True
        else:
            return False