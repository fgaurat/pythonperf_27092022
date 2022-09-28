

class Rectangle:

    def __init__(self, longueur, largeur):
        print(f"def __init__(self,{longueur},{largeur}) -> None")
        self._longueur = longueur
        self._largeur = largeur

    def get_longueur(self):
        return self._longueur

    def get_largeur(self):
        return self._largeur

    def set_longueur(self, longueur):
        self._longueur = longueur

    def set_largeur(self, largeur):
        self._largeur = largeur

    def get_surface(self):
        return self._longueur*self._largeur
    

    def __str__(self) -> str:
        return f"{__class__.__name__} {self._longueur=} {self._largeur=}"

