#!/usr/bin/env python3

__author__ = "mrgrassho"

"""
Tipo: Creación
Propósito: Separar la construcción de un objeto complejo de su representación.
"""

from abc import ABC, abstractmethod

class KnifeBuilder(ABC):
    @abstractmethod
    def build_blade(self):
        pass

    @abstractmethod
    def build_handle(self):
        pass

class GoldKnifeBuilder(KnifeBuilder):
    def build_blade(self):
        return "Hoja de Oro construida."

    def build_handle(self):
        return "Empuñadura bañada en Oro construida."

class SteelKnifeBuilder(KnifeBuilder):
    def build_blade(self):
        return "Hoja de Acero construida."

    def build_handle(self):
        return "Empuñadura de madera construida."

class KnifeDirector():
    def construct_knife(self, builder):
        print("Forjando la cuchilla...")
        print(builder.build_blade())
        print("Asentando la empuñadura...")
        print(builder.build_handle())

kd = KnifeDirector()
kd.construct_knife(GoldKnifeBuilder())
kd.construct_knife(SteelKnifeBuilder())
