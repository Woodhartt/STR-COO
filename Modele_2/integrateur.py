#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  5 16:06:25 2018

@author: florian
"""


from abstractComp import AtomicComponent, Evenement
class Integrateur(AtomicComponent):
    def __init__(self):
        super().__init__()
        self.liste_entree.append(Evenement.X_POINT)
        self.liste_sortie.append(Evenement.RES)
        self.h = 10e-4
        self.x_point = 0
        self.x = 0
    
    def delta_int(self):
        super().delta_int()
        if self.etat_courant == 0:
            self.x = self.x + self.h*self.x_point
            self.etat_suivant = 0
            self.e = 0
        self.etat_courant = self.etat_suivant
    
    def delta_ext(self, liste_entree):
        super().delta_ext(liste_entree)
        if self.etat_courant == 0 and Evenement.X_POINT in liste_entree:
            self.x = self.x + self.e*self.x_point
            self.x_point = liste_entree[Evenement.X_POINT]
            self.etat_suivant = 0
            self.e = 0
        self.etat_courant = self.etat_suivant
        
    def delta_con(self, liste_entree):
        super().delta_con(liste_entree)
        self.etat_courant = self.etat_suivant
    
    def f_lambda(self):
        super().f_lambda()
        return {Evenement.RES : self.x+self.h*self.x_point}
    
    def get_ta(self):
        super().get_ta()
        return self.h - self.e 