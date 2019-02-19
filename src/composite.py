#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "mrgrassho"

"""
Propósito:

Ayuda a crear estructuras de arbol de objetos sin la necesidad de forzar a los
clientes a diferenciar entre ramas u hojas.
"""

from abc import ABC, abstractmethod

class AbstractFile(ABC):
    """docstring for AbstractFile."""
    @abstractmethod
    def ls(self):
        pass

class File(AbstractFile):
    """docstring for AbstractFile."""
    def __init__(self, name, indent):
        self.name = name
        self.indent = indent

    def ls(self):
        print(self.indent.__str__() + self.name)

class Dir(AbstractFile):
    """docstring for AbstractFile."""
    def __init__(self, name, indent):
        self.name = name
        self.indent = indent
        self.files = []

    def add(self, absfile):
        self.files.append(absfile)

    def ls(self):
        print(str(self.indent) + self.name)
        self.indent.increase()
        for i in self.files:
            i.ls()
        self.indent.decrease()


class Ident(object):
    def __init__(self):
        self.ident = 0

    def increase(self):
        self.ident += 1

    def decrease(self):
        self.ident -= 1

    def __str__(self):
        return self.ident * "\t"


ind = Ident()
f1 = File("Libro1.pdf", ind)
f2 = File("Libro2.pdf", ind)
f3 = File("Route66.mp3", ind)
f4 = File("Data.pdf", ind)
d1 = Dir("Libros", ind)
d2 = Dir("Documentos", ind)
d3 = Dir("Musica", ind)
d1.add(f1)
d1.add(f2)
d3.add(f3)
d2.add(f4)
d2.add(d1)
d2.add(d3)
d2.ls()
