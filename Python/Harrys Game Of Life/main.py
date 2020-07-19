#!/bin/python3

"""
Harry's Game of Life:
TODO:
	* Make a way to bypass the "corner cursor event freeze"
	* USE THE MODULO (%) WHEN ADDING EDGE WARPING
    * COMPARE DIFFERENT LISTS OF NEIGHBOURS TO SEE WHICH "DEAD" CELLS HAVE 2-3 NEIGBOURS
"""

# Imports
import os as os
import sys as sys

root = os.path.dirname(os.path.realpath(__file__))

os.chdir(root)
sys.path.append(root + "/lib")

import pygame as pygame

# Modules
from gameinit import gameinit

# Global Variables
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h",
            "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]


class Cell():
    def __init__(self, universe, id, coords=()):
        self.universe = universe
        self.id = id

        self.coords = coords
        self.adjacent = [
            (self.coords[0] - 1, self.coords[1] - 1),
            (self.coords[0], self.coords[1] - 1),
            (self.coords[0] + 1, self.coords[1] - 1),
            (self.coords[0] - 1, self.coords[1]),
            (self.coords[0] + 1, self.coords[1]),
            (self.coords[0] - 1, self.coords[1] + 1),
            (self.coords[0], self.coords[1] + 1),
            (self.coords[0] + 1, self.coords[1] + 1)
        ]

        self.neighbours = []

    def update(self):
        for cell in self.universe:
            for adjacent in self.adjacent:
                if adjacent == cell.coords:
                    self.neighbours.append(cell.coords)

        if len(self.neighbours) < 2 or len(self.neighbours) > 3:
            del self.universe[self.id]


class Main(gameinit):
    def __init__(self):
        super().__init__()

        self.universe = {}

        self.universe = {
            "a": Cell(self.universe, "a", (10, 10)),
            "b": Cell(self.universe, "b", (10, 11)),
            "c": Cell(self.universe, "c", (10, 9))
        }

    def main(self):
        self.canvas.fill((0, 0, 0))
        for x in range(0, 1920, 40):
            pygame.draw.line(self.canvas, (255, 255, 255), (x, 0), (x, 1080))
        for y in range(0, 1080, 40):
            pygame.draw.line(self.canvas, (255, 255, 255), (0, y), (1920, y))

        for key in self.universe:
            self.universe[key].update()

        print(self.universe)

        self.update()


if __name__ == "__main__":
    Main = Main()
    while True:
        Main.main()
