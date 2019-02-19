#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "mrgrassho"

"""
Propósito:

Es un patrón estructural que permite publicar y subscribir funcionalidad. Esto
se logra a traves de un objeto autonomo, publisher es el que permite a otros
objetos subscribir o desubcribirse.
"""
from abc import abstractmethod, ABC

class Observer(ABC):
    @abstractmethod
    def update(self, state):
        pass


class ConcreteObserver1(Observer):
    def __init__(self):
        self.state = ""

    def update(self, state):
        self.state = state
        print("Auto cambió a estado \'" + str(state) + "\'")


class ConcreteObserver2(Observer):
    def __init__(self):
        self.state = ""

    def update(self, state):
        self.state = state
        print("Cesped cambió a estado \'" + str(state) + "\'")


class Observable(object):
    def __init__(self):
        self.obs = set()

    def add_observer(self, o):
        if isinstance(o, Observer):
            self.obs |= set([o])

    def rmv_observer(self, o):
        if isinstance(o, Observer):
            self.obs -= set([o])

    def notify_observer(self, state):
        for i in self.obs:
            i.update(state)


co1 = ConcreteObserver1()
co2 = ConcreteObserver2()
obs = Observable()
obs.add_observer(co1)
obs.add_observer(co2)
obs.notify_observer("Humedo")
obs.rmv_observer(co2)
obs.notify_observer("Seco")
