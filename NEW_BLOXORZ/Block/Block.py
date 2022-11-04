import os
import random
import sys

from Square.Square import Square
dir =  os.getcwd()
sys.path.insert(0, dir+"/..")
import pygame

# class Block đại diện cho một khối bloxorz
class Block:

    color = pygame.Color(238, 82, 83)

    def __init__(self, xPosition, yPosition):
        
        self.currentSquare = [
            dict(xPosition = xPosition, yPosition = yPosition)
        ]
        self.color = pygame.Color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    def render(self, screen):
        for square in self.currentSquare:
            pygame.draw.rect(screen, self.color, pygame.rect.Rect(square["xPosition"]*Square.width, square["yPosition"]*Square.height, Square.width, Square.height))
            pygame.display.update(pygame.rect.Rect(square["xPosition"]*Square.width, square["yPosition"]*Square.height, Square.width, Square.height))