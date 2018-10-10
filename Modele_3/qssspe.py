#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 13:27:22 2018

@author: florian
"""

from qss import Qss
import math
class QssSpe(Qss):
    def __init__(self, v, liste_ev_entree, liste_ev_sortie):
        if len(liste_ev_entree) < 2:
            raise Exception("Taille de la liste d'entrées infèrieure à ce qui est nécessaire")
        super().__init__(v, liste_ev_entree, liste_ev_sortie)
        self.delta_v = 10e-2
    
    def delta_int(self):
        super().delta_int()
    
    def delta_ext(self, liste_entree):
        super().delta_ext(liste_entree)
        
    def delta_con(self, liste_entree):
        super().delta_con(liste_entree)
    
    def f_lambda(self):
        return super().f_lambda()
    
    def get_ta(self):
        return super().get_ta()
    
    def traitement_integrale(self, liste_entree):
        if self.liste_entree[0] in liste_entree:
            vl = self.v
            self.v = self.v + self.e*self.v_point
            self.v_point = liste_entree[self.liste_entree[0]][0]
            if self.v_point == 0:
                self.delta_t = math.inf
            else:
                self.delta_t = (self.delta_v-abs(self.v-vl))/abs(self.v_point)
            self.etat_suivant = 0
            self.e = 0
        elif self.liste_entree[1] in liste_entree:
            self.v *= -0.8
            self.delta_t = 0
            self.etat_suivant = 0
            self.e = 0
