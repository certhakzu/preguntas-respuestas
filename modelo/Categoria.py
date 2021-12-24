import Premio


class Categoria:
    def __init__(self, nivel, premio) -> None:
        self._nivel=nivel
        self._premio= Premio.valor

    @property
    def nivel(self):
        return self._nivel
    
    @nivel.setter
    def nivel(self, nivel):
        self._nivel = nivel