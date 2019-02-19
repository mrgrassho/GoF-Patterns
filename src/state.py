#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "mrgrassho"


"""
Propósito:

Este patrón permite alterar el comportamiento de un objeto cuando su estado
interno cambia. Utilizando herencia y permitiendo a las subclases representar
diferentes estados y funcionalidad que puede ser cambiada en runtime. Puede ser
usado como una forma de cambiar parcialmente el tipo de un objeto en runtime
"""

from abc import ABC, abstractmethod

class State(ABC):
    def write_something(self, context, msj):
        pass

class ConcreteState1(State):
    def write_something(self, context, msj):
        print(msj.center(23))
        context.state = ConcreteState2()

class ConcreteState2(State):
    def write_something(self, context, msj):
        print(msj.title())
        context.state = ConcreteState1()

class StateContext():
    def __init__(self):
        self.state = ConcreteState1()

    def write_something(self, msj):
        self.state.write_something(self, msj)

f = StateContext()
f.write_something("you fail")
f.write_something("you win")
f.write_something("you swim")
f.write_something("you fix")
