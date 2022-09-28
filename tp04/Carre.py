
from Rectangle import Rectangle



class Carre(Rectangle):


    def __init__(self, cote):
        # super().__init__(cote, cote)
        self._cote = cote

    @property
    def cote(self):
        return self._cote

    @cote.setter
    def cote(self,cote):
        self._cote=cote

