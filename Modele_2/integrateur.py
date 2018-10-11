#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  5 16:06:25 2018

@author: florian
"""
from abstractComp import AtomicComponent
class Integrateur(AtomicComponent):
    def __init__(self, liste_entree, liste_sortie, h=10e-4):
        if len(liste_sortie) == 0:
            raise Exception("Taille de la liste de sorties infèrieure à ce qui est nécessaire")
        if len(liste_entree) == 0:
            raise Exception("Taille de la liste d'entrées infèrieure à ce qui est nécessaire")
        super().__init__()
        self.liste_entree += liste_entree
        self.liste_sortie += liste_sortie
        self.h = h
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
        if self.etat_courant == 0 and self.liste_entree[0] in liste_entree:
            self.x = self.x + self.e*self.x_point
            self.x_point = liste_entree[self.liste_entree[0]][0]
            self.etat_suivant = 0
            self.e = 0
        self.etat_courant = self.etat_suivant
        
    def delta_con(self, liste_entree):
        super().delta_con(liste_entree)
        self.etat_courant = self.etat_suivant
    
    def f_lambda(self):
        super().f_lambda()
        return {self.liste_sortie[0] : [self.x+self.h*self.x_point]}
    
    def get_ta(self):
        super().get_ta()
        return self.h - self.e 