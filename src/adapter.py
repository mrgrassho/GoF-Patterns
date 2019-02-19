#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "mrgrassho"

"""
Propósito:

Este patrón tiene el propósito de traducir la interfaz de una clase en
otra interfaz. Estó hace posible que dos clases trabajen juntas que de otra
manera no seria posible.

Nota: Como su nombre lo indica funciona como Adaptador de clases
"""

from abc import ABC, abstractmethod
from datetime import datetime
from time import sleep

class Log(object):
    def __init__(self, timestamp, msg, user, path):
        self.timestamp = timestamp
        self.msg = msg
        self.user = user
        self.path = path

    def __str__(self):
        return "{0} - {3}@{2} - {1}".format(self.timestamp, self.msg, self.user, self.path)


class absLog(ABC):
    @abstractmethod
    def show_log(self):
        pass

class SimpleLog(absLog, Log):
    def __init__(self, msg):
        super(SimpleLog, self).__init__(str(datetime.now()), msg, "admin", "/log/simple.log")

    def show_log(self):
        return super(SimpleLog, self).__str__()

l = []
l.append(SimpleLog("All fine"))
l.append(SimpleLog("All fine"))
l.append(SimpleLog("A rainbow disappear in Bangok"))
sleep(4)
l.append(SimpleLog("Wow, You've been hacked!"))
for i in l:
    print(i.show_log())
