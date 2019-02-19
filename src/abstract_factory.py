#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "mrgrassho"

"""
Propósito:

Proporcionar una interfaz para crear familia de objetos relacionados
o  dependientes sin especificar una clases concreta. Es una versión acomplejizada
de factory

Dado el ejercicio planteado en factory, proponemos realizar una mejora para:crear
un personaje acompañado de su mascota. Para la cual es unica por cada personaje
pero es independiente de cada uno.

Ventajas:
    [+] Aisla a los clientes de clases concretas de implementación.
    [+] Facilita el intercambio de familia de Clases (en este caso Personjes)

Desventajas:
    [-] Estructura Compleja.
    [-] Dificultad de soportar nuevos personajes en este contexto.
"""

from abc import ABC, abstractmethod

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

class Mascota(ABC):
    """docstring for Producto."""
    @abstractmethod
    def __str__(self):
        pass

class MascotaA(Mascota):
    def __init__(self, nombre, vida):
        self.nombre = nombre
        self.vida = vida

    def __str__(self):
        return "Mascota A -> Nombre: {}, vida: {}".format(self.nombre, self.vida)

class MascotaB(Mascota):
    def __init__(self, nombre, vida):
        self.nombre = nombre
        self.vida = vida

    def __str__(self):
        return "Mascota B -> Nombre: {}, vida: {}".format(self.nombre, self.vida)

class FactoryAbs(ABC):
    @abstractmethod
    def ConstruirPr(self, nombre, vida):
        pass

    @abstractmethod
    def ConstruirMs(self, nombre, vida):
        pass

class FactoryA(FactoryAbs):
    def ConstruirPr(self, nombre, vida):
        return PersonajeA(nombre, vida)

    def ConstruirMs(self, nombre, vida):
        return MascotaA(nombre, vida * 0.1)

class FactoryB(FactoryAbs):
    def ConstruirPr(self, nombre, vida):
        return PersonajeB(nombre, vida)

    def ConstruirMs(self, nombre, vida):
        return MascotaB(nombre, vida * 0.2)

fca = FactoryA()
l = []
l.append(fca.ConstruirPr("Ghost Killer", 92.0))
l.append(fca.ConstruirMs("Dog Killer", 92.0))
[print(i) for i in l]

fcb = FactoryB()
l = []
l.append(fcb.ConstruirPr("Cyber Cowboy", 88.0))
l.append(fcb.ConstruirMs("Cyber Metal Horse", 88.0))
[print(i) for i in l]
