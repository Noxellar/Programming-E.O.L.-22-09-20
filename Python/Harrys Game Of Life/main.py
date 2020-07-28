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
from game import Game

# Global Variables
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h",
            "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]


class Cell():
    # Static variable for all empty and adjecent spaces
    _empty_adjacent = []

    def __init__(self, id, coords=()):
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

    def update(self, universe, delete_queue):
        neighbours = []

        for cell in universe:
            for adjacent in self.adjacent:
                if adjacent == universe[cell].coords:
                    # Add neighbours' coordinates to list
                    neighbours.append(universe[cell].coords)

        empty_adjacent = [x for x in self.adjacent if x not in neighbours]
        self._empty_adjacent.append(empty_adjacent)

        # If underpopulated or overpopulated
        #   Removed coordinates from static variable
        #   Add self to delete queue
        if len(neighbours) != 2 and len(neighbours) != 3:
            delete_queue.append(self.id)


class MasterCell(Cell):
    def __init__(self):
        pass

    def reproduce(self):
        for coords in self._empty_adjacent:
            frequency = self._empty_adjacent.count(coords)

            if frequency == 2 or frequency == 3:
                while coords in self._empty_adjacent:
                    self._empty_adjacent.remove(coords)


class Main(Game):
    def __init__(self):
        super().__init__()

        self.master = MasterCell()

        self.universe = {}

        self.universe = {
            "a": Cell("a", (10, 10)),
            "b": Cell("b", (10, 11)),
            "c": Cell("c", (10, 9))
        }

        self.delete_queue = []

    def main(self):
        self.canvas.fill((0, 0, 0))
        for x in range(0, 1920, 40):
            pygame.draw.line(self.canvas, (255, 255, 255), (x, 0), (x, 1080))
        for y in range(0, 1080, 40):
            pygame.draw.line(self.canvas, (255, 255, 255), (0, y), (1920, y))

        for key in self.universe:
            self.universe[key].update(self.universe, self.delete_queue)

        self.master.reproduce()

        for id in self.delete_queue:
            del self.universe[id]
        self.delete_queue = []

        self.update()


if __name__ == "__main__":
    Main = Main()
    while True:
        Main.main()
