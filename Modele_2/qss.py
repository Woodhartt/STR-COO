#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  9 14:01:40 2018

@author: florian
"""

from abstractComp import AtomicComponent
import math
class Qss(AtomicComponent):
    def __init__(self, liste_entree, liste_sortie, delta_q=10e-4):
        if len(liste_sortie) == 0:
            raise Exception("Taille de la liste de sorties infèrieure à ce qui est nécessaire")
        if len(liste_entree) == 0:
            raise Exception("Taille de la liste d'entrées infèrieure à ce qui est nécessaire")
        super().__init__()
        #self.liste_entree.append(Evenement.X_POINT)
        #self.liste_sortie.append(Evenement.QI)
        self.liste_sortie += liste_sortie
        self.liste_entree += liste_entree
        self.delta_q = delta_q
        self.delta_t = 0
        self.q_point = 0
        self.q = 0
    
    def delta_int(self):
        super().delta_int()
        if self.etat_courant == 0:
            self.q = self.q + self.delta_q* (1 if self.q_point >= 0 else -1)
            if self.q_point == 0:
                self.delta_t = math.inf
            else :
                self.delta_t = self.delta_q/abs(self.q_point)
            self.e = 0
        self.etat_courant = self.etat_suivant
    
    def delta_ext(self, liste_entree):
        super().delta_ext(liste_entree)
        if self.etat_courant == 0 and self.liste_entree[0] in liste_entree:
            ql = self.q
            self.q = self.q+self.e*self.q_point
            self.q_point = liste_entree[self.liste_entree[0]][0]
            if self.q_point == 0:
                self.delta_t = math.inf
            else:
                self.delta_t = (self.delta_q-abs(self.q - ql))/abs(self.q_point)
            self.e = 0
        self.etat_courant = self.etat_suivant
        
    def delta_con(self, liste_entree):
        super().delta_con(liste_entree)
        self.etat_courant = self.etat_suivant
    
    def f_lambda(self):
        super().f_lambda()
        return {self.liste_sortie[0] : [self.q+self.delta_q*(1 if self.q_point >= 0 else -1)]}
    
    def get_ta(self):
        super().get_ta()
        return self.delta_t - self.e 