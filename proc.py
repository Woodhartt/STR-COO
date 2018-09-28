import abstractComp
class Proc(AtomicComponent):
    def __init__(self):
        super().__init__(self, 0)
        self.liste_entree.append(Evenement.REQ)
        self.liste_sortie.append(Evenement.DONE)

    def delta_int(self):
        super().delta_int()
        if self.etat_courant == 0:
            etat_suivant = 1
        etat_courant = etat_suivant

    def delta_ext(self, liste_entree):
        super().delta_ext(liste_entree)
        if self.etat_courant == 0 and Evenement.REQ is in liste_entree:
            self.etat_suivant = 1
        self.etat_courant = self.etat_suivant

    def delta_con(self, liste_entree):
        super().delta_con(liste_entree)
        etat_courant = etat_suivant

    def f_lambda(self):
        super().f_lambda()
        return ([Evenement.DONE] if self.etat_courant == 1 else [])

    def get_ta(self):
        super().get_ta()
        if self.etat_courant == 0:
            return Inf
        elif self.etat_courant == 1:
            return 2
        else:
            raise Exception("Seulement 2 etats")
