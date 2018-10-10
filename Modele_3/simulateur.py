#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from cste import Constant
from qss import Qss
from qssspe import QssSpe
from rebond import Rebond
from abstractComp import Evenement
import matplotlib.pyplot as plt

temps = 0
temps_fin = 10
liste_comp = [Constant([Evenement.CSTE]), QssSpe(0,[Evenement.CSTE, Evenement.RESETV],[Evenement.V]),
              Qss(10,[Evenement.V],[Evenement.H]), Rebond([Evenement.H],[Evenement.RESETV])]
liste_rebond = []
liste_temp = []
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
        liste_ev_im.update(evenement)
        for key in evenement:
            if key == Evenement.H :
                liste_temp.append(temps)
                liste_rebond.append(evenement[key])
    
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
plt.step(liste_temp, liste_rebond, where='post')
plt.show()
