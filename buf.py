import abstractComponent 
class Buf(AtomicComponent):
    def __init__(self):
        super().__init__(self, 0)
        self.liste_sortie.append(Evenement.REQ)
        self.liste_entree.append(Evenement.DONE)
        self.liste_entree.append(Evenement.JOB)
        q = 0

    def delta_int(self):
        super().delta_int()
        if self.etat_courant == 1:
            q = q - 1
            self.etat_suivant == 2
        self.etat_courant = self.etat_suivant

    def delta_ext(self, liste_entree):
        super().delta_ext(liste_entree)
        if (self.etat_courant == 0 or self.etat_courant == 1) and Evenement.JOB is in liste_entree:
            q = q + 1
            self.etat_suivant == 1
        elif self.etat_courant == 2 and Evenement.DONE is in liste_entree:
            if q > 0:
                self.etat_suivant = 1
            elif q == 0:
                self.etat_suivant = 0
            else:
                raise Exception("q >= 0")
        elif self.etat_courant == 2 and Evenement.JOB is in liste_entree:
            q = q + 1
            self.etat_suivant = 2
        self.etat_courant = self.etat_suivant

    def delta_con(self, liste_entree):
        super().delta_con(liste_entree)
        self.etat_courant = self.etat_suivant

    def f_lambda(self):
        super().f_lambda()
        return ([Evenement.REQ] if self.etat_courant == 1 else [])

    def get_ta(self):
        super().get_ta()
        if self.etat_courant == 0 or self.etat_courant == 2:
            return Inf
        else:
            return 0


