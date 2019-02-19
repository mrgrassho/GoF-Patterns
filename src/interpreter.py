#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "mrgrassho"

from abc import ABC, abstractmethod

class Contexto(object):

    def __init__(self, contexto):
        self.contexto = contexto
        self.salida = 0

    def sumar(self, salida):
        self.salida += salida


class Expresion(object):

    @abstractmethod
    def uno(self):
        pass

    @abstractmethod
    def cuatro(self):
        pass

    @abstractmethod
    def cinco(self):
        pass

    @abstractmethod
    def nueve(self):
        pass

    @abstractmethod
    def multiplicador(self): pass

    def interpretar(self, c):
        if (c.contexto.startswith(self.nueve())):
            c.sumar(9 * self.multiplicador())
            c.contexto = c.contexto[2:]
        elif(c.contexto.startswith(self.cuatro())):
            c.sumar(4 * self.multiplicador())
            c.contexto = c.contexto[2:]
        elif(c.contexto.startswith(self.cinco())):
            c.sumar(5 * self.multiplicador())
            c.contexto = c.contexto[1:]

        while (c.contexto.startswith(self.uno())):
            c.sumar(1 * self.multiplicador())
            c.contexto = c.contexto[1:]


class ExpresionUno(Expresion):
    def uno(self):
        return "I"
    def cuatro(self):
        return "IV"
    def cinco(self):
        return "V"
    def nueve(self):
        return "IX"
    def multiplicador(self):
        return 1


class ExpresionDiez(Expresion):
    def uno(self):
        return "X"
    def cuatro(self):
        return "XL"
    def cinco(self):
        return "L"
    def nueve(self):
        return "XC"
    def multiplicador(self):
        return 10


class ExpresionCien(Expresion):
    def uno(self):
        return "C"
    def cuatro(self):
        return "CD"
    def cinco(self):
        return "D"
    def nueve(self):
        return "CM"
    def multiplicador(self):
        return 100


class ExpresionMil(Expresion):
    def uno(self):
        return "M"
    def cuatro(self):
        return " "
    def cinco(self):
        return " "
    def nueve(self):
        return " "
    def multiplicador(self):
        return 1000


class Convertidor(object):

    def __init__(self, romano):
        self.expresiones = []
        self.expresiones.append(ExpresionMil())
        self.expresiones.append(ExpresionCien())
        self.expresiones.append(ExpresionDiez())
        self.expresiones.append(ExpresionUno())
        self.contexto = Contexto(romano) # romano = Roman String Nbr

    def convertir(self):
        for ex in self.expresiones:
            ex.interpretar(self.contexto)
        return self.contexto.salida

c = Convertidor("XL");
print("XL -> " + str(c.convertir()))
c = Convertidor("MCIII");
print("MCIII -> " + str(c.convertir()))
