#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "mrgrassho"

"""
** Proposito:

Proveer una interfaz para clonar objetos. El proprosito de clonar un objeto
es reutilizar instancias existentes en lugar de crear nuevas.
"""

from copy import copy

class Product(object):

    def clone(self):
        return copy(self)

class ProductA(Product):
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return "nombre {}, precio {}".format(self.name, self.price)

    def clone(self):
        clone = super(ProductA, self).clone()
        return clone

class ProductB(Product):
    def __init__(self, name, price, medidas):
        self.name = name
        self.price = price

    def __str__(self):
        return "nombre {}, precio {}".format(name, price)


p = ProductA("Shampoo", 4500.33)
a = p.clone()
print(a)
