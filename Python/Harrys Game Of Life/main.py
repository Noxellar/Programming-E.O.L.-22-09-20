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

from init import init


class Main(init):
    def __init__(self):
        super().__init__()

    def main(self):
        self.canvas.fill((100, 100, 100))
        for x in range(0, 1920, 40):
            pygame.draw.line(self.canvas, (255, 255, 255), (x, 0), (x, 1080))
        for y in range(0, 1080, 40):
            pygame.draw.line(self.canvas, (255, 255, 255), (0, y), (1920, y))

        for neighbour in self.universe:
            cells = [
                (neighbour[0] - 1, neighbour[1] - 1),
                (neighbour[0], neighbour[1] - 1),
                (neighbour[0] + 1, neighbour[1] - 1),
                (neighbour[0] - 1, neighbour[1]),
                (neighbour[0] + 1, neighbour[1]),
                (neighbour[0] - 1, neighbour[1] + 1),
                (neighbour[0], neighbour[1] + 1),
                (neighbour[0] + 1, neighbour[1] + 1)
            ]

            pass

        self.update()


if __name__ == "__main__":
    Main = Main()
    while True:
        Main.main()
