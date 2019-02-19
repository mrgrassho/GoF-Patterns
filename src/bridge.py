#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "mrgrassho"

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def draw(self):
        pass
    @abstractmethod
    def resize(self, n):
        pass

class Circle(Shape):
    """docstring for Circle."""
    def __init__(self, x, y, radius, drawingAPI):
        self.x = x
        self.y = y
        self.radius = radius
        self.drawingAPI = drawingAPI

    def draw(self):
        self.drawingAPI.drawCircle(self.x, self.y, self.radius)

    def resize(self, n):
        self.radius *= n

class drawingAPI(ABC):
    @abstractmethod
    def drawCircle(self, x, y, radius):
        pass

class drawingAPI1(drawingAPI):
    def drawCircle(self, x, y, radius):
        print("API1 - x: {}, y: {}, radius: {}".format(x, y, radius))

class drawingAPI2(drawingAPI):
    def drawCircle(self, x, y, radius):
        print("API2 - x: {}, y: {}, radius: {}".format(x, y, radius))

c = Circle(1, 2, 3, drawingAPI1())
d = Circle(1, 2, 3, drawingAPI2())
c.draw()
d.draw()
