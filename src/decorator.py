#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "mrgrassho"

"""
Propósito:

Permite agregar responsabilidad y modificar funcionalidad dinamicamente. Provee
una alternativa flexible a la herencia, utilizando la composición como herra-
mienta para extender funcionalidad.
"""

from abc import ABC, abstractmethod

class ArmaBase(ABC):
    """Docstring for Producto."""
    @abstractmethod
    def __str__(self):
        pass

class Sniper(ArmaBase):
    def __str__(self):
        return "Sniper"

class Escopeta(ArmaBase):
    def __str__(self):
        return "Escopeta"

class DecoradorArmaBase(ArmaBase):
    """Docstring for Personaje."""
    def __init__(self, arma):
        self.arma = arma

    def __str__(self):
        return self.arma.__str__()

class Silenciador(DecoradorArmaBase):
    def __init__(self, arma):
        super(Silenciador, self).__init__(arma)

    def __str__(self):
        return self.arma.__str__() + " + Silenciador"

class MiraLaser(DecoradorArmaBase):
    def __init__(self, arma):
        super(MiraLaser, self).__init__(arma)

    def __str__(self):
        return self.arma.__str__() + " + MiraLaser"


sniper = Sniper()
silence = Silenciador(sniper)
escopeta = Escopeta()
miralaser = MiraLaser(escopeta)
print(silence)
print(miralaser)
miralaser = MiraLaser(silence)
print(miralaser)
