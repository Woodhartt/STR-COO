#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from abstractComp import AtomicComponent, Evenement 
import math
class Adder(AtomicComponent):
    def __init__(self):
        super().__init__()
        self.liste_entree.append(Evenement.XV)
        self.liste_sortie.append(Evenement.X_POINT)
        self.liste_xi = []
        
    def delta_int(self):
        super().delta_int()
        if self.etat_courant == 1:
            self.etat_suivant = 0
            self.e = 0
        self.etat_courant = self.etat_suivant

    def delta_ext(self, liste_entree):
        super().delta_ext(liste_entree)
        if (self.etat_courant == 0 or self.etat_courant == 1) and Evenement.XV in liste_entree:
            liste_tmp = liste_entree[Evenement.XV]
            for x in liste_tmp:
                if x[0] in [var[0] for var in self.liste_xi]:
                    for var in self.liste_xi:
                        if var[0] == x[0]:
                            var = x
                else :
                    self.liste_xi.append(x)
            self.etat_suivant = 1
            self.e = 0
        self.etat_courant = self.etat_suivant

    def delta_con(self, liste_entree):
        super().delta_con(liste_entree)
        self.etat_courant = self.etat_suivant

    def f_lambda(self):
        super().f_lambda()
        somme=0
        for var in self.liste_xi:
            somme += var[1]
        return {Evenement.X_POINT : somme}

    def get_ta(self):
        super().get_ta()
        retour = 0
        if self.etat_courant == 0 :
            retour = math.inf
        else:
            retour = 0
        return retour