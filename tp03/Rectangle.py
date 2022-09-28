

class Rectangle:

    def __init__(self, longueur, largeur):
        print(f"def __init__(self,{longueur},{largeur}) -> None")
        self._longueur = longueur
        self._largeur = largeur

    @property
    def longueur(self):
        return self._longueur
    
    @property
    def largeur(self):
        return self._largeur

    @longueur.setter
    def longueur(self, longueur):
        self._longueur = longueur

    @largeur.setter
    def largeur(self, largeur):
        self._largeur = largeur

    def get_surface(self):
        return self._longueur*self._largeur
    
    def __str__(self) -> str:
        return f"{__class__.__name__} {self._longueur=} {self._largeur=}"


    def __eq__(self,r)->bool:
        return self._longueur == r._longueur and self._largeur == r._largeur

