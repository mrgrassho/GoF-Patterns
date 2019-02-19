#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "mrgrassho"

"""
Propósito:

Patrón utilizado para crear objetos que representan acciones y eventos dentro
de una aplicación. El objeto Command encapsula una acción o evento y contiene
información para entender que pasó exactamente.
"""
from abc import ABC, abstractmethod

class Invoker(object):

    def __init__(self):
        self.cmds = []

    def add(self, cmd):
        self.cmds.append(cmd)

    def execute_all(self):
        for i in self.cmds:
            i.execute()


# Receptor
class Parlante(object):
    def action1(self):
        print("Volumen 100%")

    def action2(self):
        print("Volumen 50%")

    def action3(self):
        print("Volumen 10%")

class Cmd(ABC):
    @abstractmethod
    def execute(self):
        pass

class VolMax(Cmd):
    def __init__(self, parlante):
        self.parlante = parlante

    def execute(self):
        self.parlante.action1()

class VolMed(Cmd):
    def __init__(self, parlante):
        self.parlante = parlante

    def execute(self):
        self.parlante.action2()

class VolMin(Cmd):
    def __init__(self, parlante):
        self.parlante = parlante

    def execute(self):
        self.parlante.action3()


p = Parlante()
i = Invoker()
i.add(VolMax(p))
i.add(VolMed(p))
i.add(VolMin(p))
i.execute_all()
