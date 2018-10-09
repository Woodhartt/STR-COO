#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from step import Step
from adder import Adder
from integrateur import Integrateur
from qss import Qss
from abstractComp import Evenement
import matplotlib.pyplot as plt

temps = 0
temps_fin = 10
liste_comp = [Step(1, 1, -3, 0.65), Step(2, 0, 1, 0.35), Step(3, 0, 1, 1), Step(4, 0, 4, 1.5), Adder(), Integrateur(),Qss() ]
liste_points = []
liste_qss = []
liste_temps1 = []
liste_temps2 = []
liste_temps3 = []
liste_adder = []
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
        for key in evenement.keys():
            if key in liste_ev_im.keys() and key == Evenement.XV:
                liste_ev_im[Evenement.XV] += evenement[Evenement.XV]
            else:
                liste_ev_im.update(evenement)
            if temps <= 2 and key == Evenement.X_POINT:
                liste_adder.append(evenement[key])
                liste_temps3.append(temps)
            if temps <= 2 and key == Evenement.QI:
                liste_temps1.append(temps)
                liste_qss.append(evenement[key])
            if temps <= 2 and key == Evenement.RES:
                liste_temps2.append(temps)
                liste_points.append(evenement[key])
            
    for comp in liste_comp:
        if (comp in imminent) and not [evenement for evenement in comp.liste_entree if evenement in liste_ev_im]:
            comp.delta_int()
        elif (comp not in imminent) and [evenement for evenement in comp.liste_entree if evenement in liste_ev_im]:
            comp.delta_ext(liste_ev_im)
        elif (comp in imminent) and [evenement for evenement in comp.liste_entree if evenement in liste_ev_im]:
            comp.delta_con(liste_ev_im)
        else:
            comp.e = comp.e + ta_min
    temps = temps+ta_min
    
plt.figure(1)
plt.step(liste_temps2, liste_points, where = 'post')
plt.figure(1)
plt.step(liste_temps1, liste_qss, where = 'post')
plt.figure(1)
plt.step(liste_temps3, liste_adder, where = 'post')
plt.show()
