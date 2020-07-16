#!/bin/python3

"""
Harry's Game of Life:
TODO:
	* Make a way to bypass the "corner cursor event freeze"
"""

# Imports
import sys as sys
import os as os

root = os.path.dirname(os.path.realpath(__file__))

os.chdir(root)
sys.path.append(root + "/lib")

import pygame as pygame

from game import Game


class Main(Game):
    def __init__(self):
        super().__init__()
        self.x = 0

    def main(self):
        self.canvas.fill((100, 100, 100))
        for x in range(0, 1920, 40):
            pygame.draw.line(self.canvas, (255, 255, 255), (x, 0), (x, 1080))
        for y in range(0, 1080, 40):
            pygame.draw.line(self.canvas, (255, 255, 255), (0, y), (1920, y))
        self.x += 1

        self.update()


if __name__ == "__main__":
    Main = Main()
    while True:
        Main.main()
