import abstractComp
class Gen(AtomicComponent):
    def __init__(self):
        super().__init__(self, 0)
        self.liste_sortie.append(Evenement.JOB)

    def delta_int(self):
        super().delta_int()
        self.etat_courant = self.etat_courant

    def delta_ext(self, liste_entree):
        super().delta_ext(liste_entree)
        raise Exception("Cas impossible pour l'instant")
    
    def delta_con(self, liste_entree):
        super().delta_con(liste_entree)
        raise Exception("Cas impossible pour l'instant")
    
    def f_lambda(self):
        super().f_lambda()
        return [Evenement.JOB]
    
    def get_ta(self):
        super().get_ta()
        return 1
