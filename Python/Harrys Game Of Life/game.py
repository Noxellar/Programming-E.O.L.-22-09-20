#!/bin/python3

import pygame as pygame


class Game():
    def __init__(self):
        pygame.init()

        # Height of the window
        self.width = 1920
        self.height = 1080

        # Height of the scaled canvas
        self.image_width = self.width
        self.image_height = self.height

        # Space between the edges of the window and the image
        self.padding_width = 0
        self.padding_height = 0

        # Initialising the window
        self.window = pygame.display.set_mode(
            (self.width, self.height), pygame.RESIZABLE | pygame.DOUBLEBUF | pygame.HWSURFACE)
        # Initialising the canvas/dummy surface (always at 16:9 resolution)
        self.canvas = pygame.Surface(
            (1920, 1080), pygame.DOUBLEBUF | pygame.HWSURFACE)
        # Initialising the image that is shown in the window
        self.image = pygame.transform.scale(
            self.canvas, (self.width, self.height))

        # Title of the window
        pygame.display.set_caption("Harry's Game Of Life")

        # Setting framerate
        self.fps = 60
        self.fps_clock = pygame.time.Clock()

        # Resizing display for other configurations (HAVE TO ADD MORE LATER SO THAT IT MAKES MORE SENSE)
        w, h = pygame.display.get_surface().get_size()

        display = {
            "size": (w, h),
            "w": w,
            "h": h
        }

        self.videoresize(pygame.event.Event(pygame.VIDEORESIZE, display))

    def update(self):
        for event in pygame.event.get():
            event_list = {
                pygame.QUIT: "quit",
                pygame.VIDEORESIZE: "videoresize",
            }

            method_name = event_list.get(event.type, lambda: "None")
            method = getattr(self, str(method_name), lambda *args: None)
            return method(event)

        self.image = pygame.transform.scale(
            self.canvas, (self.image_width, self.image_height))

        self.window.blit(
            self.image, (self.padding_width, self.padding_height))

        pygame.display.update()
        self.fps_clock.tick(self.fps)

    def quit(self, *args):
        pygame.quit()
        raise SystemExit()

    def videoresize(self, *args):
        event = args[0]

        width = event.w
        height = event.h

        self.width = width
        self.height = height

        if width < 640:
            width = 640

        if height < 360:
            height = 360

        if height <= (width / 16) * 9:
            self.image_width = (height // 9) * 16
            self.image_height = height
        else:
            self.image_width = width
            self.image_height = (width // 16) * 9

        self.window = pygame.display.set_mode(
            (width, height), pygame.RESIZABLE)

        self.padding_width = (width - self.image_width) / 2
        self.padding_height = (height - self.image_height) / 2


# CODE DUMP
"""
w, h = pygame.display.get_surface().get_size()
display = {
	"size": (w, h),
	"w": w,
	"h": h
}

pygame.event.post(pygame.event.Event(
	pygame.VIDEORESIZE, display))
"""
