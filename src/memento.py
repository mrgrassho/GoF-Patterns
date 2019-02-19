#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "mrgrassho"

class Memento():
    def __init__(self, state):
        self.state = state


class Creador(object):
    def __init__(self):
        self.state = None

    def __set__(self, state, s):
        print("Originator: Setting state to " + str(s))
        self.state = s

    def save_to_memento(self):
        print("Creador: Saving to Memento.");
        return Memento(self.state)

    def restore_from_memento(self, m):
        if (isinstance(m, Memento)):
            memento = m;
            state = memento.state
            print("Creador: State after restoring from Memento: " + self.state);


class Guardian():
    def __init__(self):
        self.saved_states = []

    def add_memento(self, m):
        self.saved_states.append(m)


g = Guardian()
c = Creador()
c.state = "State1"
c.state = "State2"
g.add_memento(c.save_to_memento());
c.state = "State3"
g.add_memento(c.save_to_memento());
c.state = "State4"
c.restore_from_memento(g.saved_states[0].state);
for i in g.saved_states:
    print(i.state)
print(g.saved_states[0].state)
