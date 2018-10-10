#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  5 16:06:25 2018

@author: florian
"""


from abstractComp import AtomicComponent
import math
class Qss(AtomicComponent):
    def __init__(self, v, liste_ev_entree, liste_ev_sortie):
        super().__init__()
        self.liste_entree += liste_ev_entree
        self.liste_sortie += liste_ev_sortie
        self.delta_v = 10e-4
        self.delta_t = math.inf
        self.v_point = 0
        self.v = v
    
    def delta_int(self):
        super().delta_int()
        if self.etat_courant == 0:
            self.v = self.v + self.delta_v*( 1 if self.v_point >=0 else -1)
            if self.v_point == 0:
                self.delta_t = math.inf
            else:
                self.delta_t = self.delta_v/abs(self.v_point)
            self.etat_suivant = 0
            self.e = 0
        self.etat_courant = self.etat_suivant
    
    def delta_ext(self, liste_entree):
        super().delta_ext(liste_entree)
        if self.etat_courant == 0:
            keys = [key for key in liste_entree]
            self.traitement_integrale(liste_entree, keys)
        self.etat_courant = self.etat_suivant
        
    def delta_con(self, liste_entree):
        super().delta_con(liste_entree)
        self.etat_courant = self.etat_suivant
    
    def f_lambda(self):
        super().f_lambda()
        if self.v+self.delta_v*(1 if self.v_point >=0 else -1) <= 0:
            retour = {self.liste_sortie[0] : self.v}
        else:
            retour = {self.liste_sortie[0] : self.v+self.delta_v*(1 if self.v_point >=0 else -1)}
        return retour
    
    def get_ta(self):
        super().get_ta()
        return self.delta_t - self.e 
    
    def traitement_integrale(self, liste_entree, keys):
        if self.liste_entree[0] in keys:
            vl = self.v
            self.v = self.v + self.e*self.v_point
            self.v_point = liste_entree[self.liste_entree[0]]
            if self.v_point == 0:
                self.delta_t = math.inf
            else:
                self.delta_t = (self.delta_v-abs(self.v-vl))/abs(self.v_point)
            self.etat_suivant = 0
            self.e = 0