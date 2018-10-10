#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from abstractComp import AtomicComponent, Evenement

class Gen(AtomicComponent):
    def __init__(self, liste_sortie):
        if len(liste_sortie) == 0:
            raise Exception("Taille de la liste de sorties infèrieure à ce qui est nécessaire")
        super().__init__()
        #self.liste_sortie.append(Evenement.JOB)
        self.liste_sortie += liste_sortie

    def delta_int(self):
        super().delta_int()
        self.etat_courant = self.etat_courant
        self.e = 0

    def delta_ext(self, liste_entree):
        super().delta_ext(liste_entree)
        raise Exception("Cas impossible pour l'instant")
    
    def delta_con(self, liste_entree):
        super().delta_con(liste_entree)
        raise Exception("Cas impossible pour l'instant")
    
    def f_lambda(self):
        super().f_lambda()
        return {Evenement.JOB : [0]}
    
    def get_ta(self):
        super().get_ta()
        return 2-self.e
