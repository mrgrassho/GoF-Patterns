#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "mrgrassho"

"""
Propósito:

Proveer una interfaz para acceder a los items de una colección de objetos sin
la necesidad de conocer la estructura interna de la misma.
"""
from abc import ABC, abstractmethod

class Iterator(ABC):
    def __init__(self, collection):
        self.collection = collection

    @abstractmethod
    def first(self):
        pass

    @abstractmethod
    def next_(self):
        pass

    @abstractmethod
    def has_next(self):
        pass


class IteratorList(Iterator):

    def __init__(self, collection):
        if isinstance(collection, list):
            super(IteratorList, self).__init__(collection)
            self.next = 0

    def first(self):
        return self.collection[0]

    def next_(self):
        self.next += 1
        return self.collection[self.next - 1]

    def has_next(self):
        return len(self.collection) > self.next


l = ['1', '2', 'uhuh', 'SAA', 'kkij', '2']
iter = IteratorList(l)
while(iter.has_next()):
    print(iter.next_())
