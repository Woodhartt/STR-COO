#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  5 14:57:06 2018

@author: florian
"""

from abstractComp import AtomicComponent
import math
class Step(AtomicComponent):
    def __init__(self, num, xi, xf, ts, liste_sortie):
        if len(liste_sortie) == 0:
            raise Exception("Taille de la liste de sorties infèrieure à ce qui est nécessaire")
        super().__init__()
        self.num = num
        self.xi = xi
        self.xf = xf
        self.ts = ts
        self.liste_sortie += liste_sortie
    
    def delta_int(self):
        super().delta_int()
        if self.etat_courant == 0:
            self.etat_suivant = 1
            self.e = 0
        elif self.etat_courant == 1:
            self.etat_suivant = 2
            self.e = 0
        self.etat_courant = self.etat_suivant
    
    def delta_ext(self, liste_entree):
        super().delta_ext(liste_entree)
        raise Exception("Cas impossible")
        
    def delta_con(self, liste_entree):
        super().delta_con(liste_entree)
        raise Exception("Cas impossible")
    
    def f_lambda(self):
        super().f_lambda()
        retour = dict()
        if self.etat_courant == 0:
            retour[self.liste_sortie[0]] = [(self.num, self.xi)]
        elif self.etat_courant == 1:
            retour[self.liste_sortie[0]] = [(self.num, self.xf)]
        return retour
    
    def get_ta(self):
        super().get_ta
        retour = 0
        if self.etat_courant == 1:
            retour = self.ts - self.e
        elif self.etat_courant == 2:
            retour = math.inf
        return retour