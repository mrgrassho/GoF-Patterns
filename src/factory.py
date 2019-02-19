#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "mrgrassho"

"""
Objetivo: Tener una clase (Factory) que fabrique los objetos que pidamos.

Ventajas
    [+] El cliente solo tiene que conocer la interfaz de Factory para crear un
    objecto o una familia de objetos.
    [+] Encapsula la creación de objetos. Lo que facilita el proceso de creación
    para objetos complejos.

Desventajas
    [-] No se puede cambiar una clase implementadora sin recompilar.
"""

from abc import ABC, abstractmethod
from copy import copy

class Personaje(ABC):
    """docstring for Producto."""
    @abstractmethod
    def __str__(self):
        pass

class PersonajeA(Personaje):
    def __init__(self, nombre, vida):
        self.nombre = nombre
        self.vida = vida

    def __str__(self):
        return "Personaje A -> Nombre: {}, vida: {}".format(self.nombre, self.vida)

class PersonajeB(Personaje):
    def __init__(self, nombre, vida):
        self.nombre = nombre
        self.vida = vida

    def __str__(self):
        return "Personaje B -> Nombre: {}, vida: {}".format(self.nombre, self.vida)

class FactoryPr(object):
    def __init__(self):
        pass

    def ConstruirPrA(self, nombre, vida):
        return PersonajeA(nombre, vida)

    def ConstruirPrB(self, nombre, vida):
        return PersonajeB(nombre, vida)

fctry = FactoryPr()
a = fctry.ConstruirPrA("Ghost Killer", 92.0)
b = fctry.ConstruirPrB("Cyber Cowboy", 88.0)
print(a)
