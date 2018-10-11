#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from buf import Buf
from gen import Gen
from proc import Proc
from evenement import Evenement
import matplotlib.pyplot as plt

temps = 0
temps_fin = 10
liste_comp = [Buf([Evenement.JOB, Evenement.DONE], [Evenement.REQ]),
              Gen([Evenement.JOB]), Proc([Evenement.REQ], [Evenement.DONE])]
liste_temps = []
liste_q = []

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
        for key in evenement:
            if key in liste_ev_im:
                liste_ev_im[key] += evenement[key]
            else:
                liste_ev_im.update(evenement)
        # Zone de print
        if Evenement.JOB in liste_ev_im or Evenement.REQ in liste_ev_im:
            liste_temps.append(temps)
            liste_q.append(liste_comp[0].q)
        # -------
 
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
plt.step(liste_temps, liste_q, where='pre')
plt.show()