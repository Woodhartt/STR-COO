#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from step import Step
from adder import Adder
from integrateur import Integrateur
from abstractComp import Evenement
# import matplotlib.pyplot as plt

temps = 0
temps_fin = 10
liste_comp = [Step(1, 1, 3, 0.65), Step(2, 0, 1, 0.35), Step(3, 0, 1, 1), Step(4, 0, 4, 1.5), Adder(), Integrateur()]

while(temps <= temps_fin):
    ta_min = liste_comp[0].get_ta()
    for i in range(1, len(liste_comp)):
        tmp = liste_comp[i].get_ta()
        if ta_min > tmp:
            ta_min = tmp
                
    imminent = []
    for comp in liste_comp:
        if comp.get_ta()  == ta_min:
            imminent.append(comp)
    liste_ev_im = {}
    for im in imminent:
        evenement = im.f_lambda()
        if Evenement.XV in liste_ev_im:
            liste_ev_im[Evenement.XV] += evenement[Evenement.XV]
        else:
            liste_ev_im.update(evenement)
    for comp in liste_comp:
        if (comp in imminent) and not [evenement for evenement in comp.liste_entree if evenement in liste_ev_im]:
            comp.delta_int()
        elif (comp not in imminent) and [evenement for evenement in comp.liste_entree if evenement in liste_ev_im]:
            comp.delta_ext(liste_ev_im)
        elif (comp in imminent) and [evenement for evenement in comp.liste_entree if evenement in liste_ev_im]:
            comp.delta_con(liste_ev_im)
        else:
            comp.e = comp.e + ta_min
    print(liste_ev_im)
    temps = temps+ta_min