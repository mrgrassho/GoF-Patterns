#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "mrgrassho"

"""
Propósito:

Este patrón estructural actua de intermediario hacia un objeto con el objetivo
de controlar su acceso.
"""

from abc import ABC, abstractmethod

class AbstractProd(ABC):
    @abstractmethod
    def __str__(self):
        pass

class Producto(AbstractProd):
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def __str__(self):
        return "{} - {}".format(self.nombre, self.precio)

class ProxyProd(AbstractProd):
    def __init__(self, nombre, precio):

        if not isinstance(precio, (int, float)):
            precio = 0.0
        if (0 > precio):
            precio = 0.0
        if not isinstance(nombre, str):
            nombre = "Null"
        self.prod = Producto(nombre, precio)

    def __str__(self):
        return self.prod.__str__()

proxy = ProxyProd(23, -1)
print(proxy)
proxy2 = ProxyProd("AIWA Stereo", 100300.00)
print(proxy2)
