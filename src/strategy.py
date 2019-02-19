#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "mrgrassho"

"""
Propósito:

Permite utilizar familia de algoritmos, encapsularlas y hacerlas
intercambiables. Strategy permite al algoritmo variar indepientemente hacia
el cliente que lo utiliza.

Nota: Patrones relacionados -> State, Flyweight, Decorator, Composite.
"""

from abc import ABC, abstractmethod

class Strategy(ABC):
    @abstractmethod
    def div_entera(self, a, b):
        pass

class DivisionComun(Strategy):
    def div_entera(self, a, b):
        return a // b

class DivisionAzteca(Strategy):
    def div_entera(self, a, b):
        c = 0
        while (a >= b):
            c += 1
            a -= b
        return c

class Contexto(object):
    def __init__(self, strat):
        self.strat = strat

    def div_entera(self, a, b):
        return self.strat.div_entera(a, b)

azteca = DivisionAzteca()
comun = DivisionComun()
c = Contexto(azteca)
print(c.div_entera(18, 4))
c.strat = comun
print(c.div_entera(18, 4))
