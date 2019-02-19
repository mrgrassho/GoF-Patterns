#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "mrgrassho"

class Analizador(object):
    def scannear():
        print("Scaneando...")
        print("Limpio sin Virus!")

class Firewall(object):
    def activar(self):
        print("Firewall Activado.")

class MineroBTC(object):
    def buscar(self):
        print("Buscando mineros de Bitcoin...")
        print("Limpio. Matamos 15 mineros, estas a salvo ahora.")

class Facade(object):
    def analizis_completo(self):
        analizador = Analizador()
        firewall = Firewall()
        mineroBTC = MineroBTC()
        analizador.scannear()
        firewall.activar()
        mineroBTC.buscar()

f = Facade()
f.analizis_completo()
