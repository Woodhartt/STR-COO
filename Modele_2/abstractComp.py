#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from abc import ABC, abstractmethod
from enum import Enum
class Evenement(Enum):
    XI = 1
    XF = 2
    X_POINT = 3
    RES = 4

class AtomicComponent(ABC):
    def __init__(self):
        self.etat_courant = 0
        self.etat_suivant = 0
        self.liste_entree = dict()
        self.liste_sortie = dict()
        self.e = 0
        super().__init__
    
    @abstractmethod
    def delta_int(self):
        pass

    @abstractmethod
    def delta_ext(self, liste_entree):
        pass

    @abstractmethod
    def delta_con(self, liste_entree):
        pass

    @abstractmethod
    def f_lambda(self):
        pass

    @abstractmethod
    def get_ta(self):
        pass


