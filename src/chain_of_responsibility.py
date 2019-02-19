#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "mrgrassho"

"""
Tipo: Patrón de Comportamiento

Propósito:

Este patrón permite a mas de un objeto manejar una request sin mutuo
conocimiento. Evitamos acoplamiento entre el emisor de una request y
los posibles receptores. Ponemos todos los receptores en una cadena,
la cual permite a los objetos pasar la request hasta que alguno de los
objetos pueda manejarla.
"""

from abc import abstractmethod
from random import randrange

class Handler(object):

    def __init__(self):
        self.next = None

    @abstractmethod
    def handle(self):
        pass

    def add(self, next):
        if (self.next == None):
            self.next = next
        else:
            self.next.add(next)

    def wrap_around(self, root):
        self.add(root)


class ConcreteHandler(Handler):

    def __init__(self, name):
        super(ConcreteHandler, self).__init__()
        self.name = name

    def handle(self):
        if (randrange(4) != 3):
            print(self.name + " is Busy.")
            self.next.handle()
        else:
            print(self.name + " put some hands on. It's done!")

root = ConcreteHandler("H1")
root.add(ConcreteHandler("H2"))
root.add(ConcreteHandler("H3"))
root.add(ConcreteHandler("H4"))
root.add(ConcreteHandler("H5"))
root.wrap_around(root)
root.handle()
