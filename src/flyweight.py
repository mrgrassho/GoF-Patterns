#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "mrgrassho"

"""
Propósito:

Provee un mecanismo que evita la creación innecesaria de objetos, por medio
de la reutilización de instancias.
"""
from abc import ABC, abstractmethod

class FlyweightFactory(object):
    def __init__(self):
        self.flyweigth_list = []

    def get_flyweigth(self, i):
        if (len(self.flyweigth_list) <= i):
            self.flyweigth_list.append(ConcreteFlyweight(i))
        return self.flyweigth_list[i]

class Flyweight(ABC):
    @abstractmethod
    def sum(self, i):
        pass

class ConcreteFlyweight(Flyweight):
    def __init__(self, i):
        self.i = i

    def sum(self, j):
        return self.i + j

f = FlyweightFactory()
for i in range(8):
    for j in range(8):
        k = f.get_flyweigth(i)
        print(k.sum(j))
