#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  9 15:54:23 2018

@author: florian
"""
from abstractComp import AtomicComponent, Evenement
import math
class Constant(AtomicComponent):
    def __init__(self, liste_sortie):
        super().__init__()
        self.cste = -9.81
        self.liste_sortie += liste_sortie
    
    def delta_int(self):
        super().delta_int()
        self.etat_suivant = 1
        self.e = 0
        self.etat_courant = self.etat_suivant

    def delta_ext(self, liste_entree):
        super().delta_ext(liste_entree)
        raise Exception("Cas impossible pour l'instant")
    
    def delta_con(self, liste_entree):
        super().delta_con(liste_entree)
        raise Exception("Cas impossible pour l'instant")
    
    def f_lambda(self):
        super().f_lambda()
        return {self.liste_sortie[0] : self.cste}
    
    def get_ta(self):
        super().get_ta()
        return (0 if self.etat_courant == 0 else math.inf)