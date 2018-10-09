#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from abc import ABC, abstractmethod
from enum import Enum
class Evenement(Enum):
    CSTE = 1
    V = 2
    H = 3

class AtomicComponent(ABC):
    def __init__(self):
        self.etat_courant = 0
        self.etat_suivant = 0
        self.liste_entree = []
        self.liste_sortie = []
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


