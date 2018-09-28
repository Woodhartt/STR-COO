from abc import ABC, abstractmethod
from enum import Enum
class Evenement(Enum):
    JOB = 1
    REQ = 2
    DONE = 3

class AtomicComponent(ABC):
    def __init__(self, etat_courant):
        self.etat_courant = etat_courant
        self.etat_suivant = etat_courant
        self.liste_entree = []
        self.liste_sortie = []
        self.e = 0
        super().__init__
    
    @abstractmethod
    def delta_int(self):
        pass

    @abstractmethod
    def delta_ext(self, liste_entree):
        pass

    @abstractmethod
    def delta_con(self, liste_entree):
        pass

    @abstractmethod
    def f_lambda(self):
        pass

    @abstractmethod
    def get_ta(self):
        pass
    
    #@abstractmethod
    #def calcul_e(self):
        #pass

