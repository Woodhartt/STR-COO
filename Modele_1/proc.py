#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from abstractComp import AtomicComponent, Evenement
import math
class Proc(AtomicComponent):
    def __init__(self):
        super().__init__(0)
        self.liste_entree.append(Evenement.REQ)
        self.liste_sortie.append(Evenement.DONE)

    def delta_int(self):
        super().delta_int()
        if self.etat_courant == 1:
            self.etat_suivant = 0
            self.e = 0
        self.etat_courant = self.etat_suivant

    def delta_ext(self, liste_entree):
        super().delta_ext(liste_entree)
        if self.etat_courant == 0 and Evenement.REQ in liste_entree:
            self.etat_suivant = 1
            self.e = 0
        self.etat_courant = self.etat_suivant

    def delta_con(self, liste_entree):
        super().delta_con(liste_entree)
        self.etat_courant = self.etat_suivant

    def f_lambda(self):
        super().f_lambda()
        return ([Evenement.DONE] if self.etat_courant == 1 else [])

    def get_ta(self):
        super().get_ta()
        if self.etat_courant == 0:
            return math.inf
        elif self.etat_courant == 1:
            return 2-self.e
        else:
            raise Exception("Seulement 2 etats")
