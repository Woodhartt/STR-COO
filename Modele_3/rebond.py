from abstractComp import AtomicComponent
import math
class Rebond(AtomicComponent):
    def __init__(self, liste_entree, liste_sortie):
        super().__init__()
        self.v = 0
        self.liste_entree += liste_entree
        self.liste_sortie += liste_sortie
        
    
    def delta_int(self):
        super().delta_int()
        if self.etat_courant == 1:
            self.etat_suivant = 0
            self.v = 0
            self.e = 0
        self.etat_courant = self.etat_suivant

    def delta_ext(self, liste_entree):
        super().delta_ext(liste_entree)
        if self.etat_courant == 0:
            keys = [key for key in liste_entree]
            for key in keys:
                if key in self.liste_entree:
                    if liste_entree[key] <= 0:
                        self.v = 1
                        self.e = 0
                        self.etat_suivant = 1
                    else:
                        self.etat_suivant = 0
        self.etat_courant = self.etat_suivant
    
    def delta_con(self, liste_entree):
        super().delta_con(liste_entree)
        raise Exception("Cas impossible pour l'instant")
    
    def f_lambda(self):
        super().f_lambda()
        return {self.liste_sortie[0] : self.v}
    
    def get_ta(self):
        super().get_ta()
        return (math.inf if self.etat_courant == 0 else 0)