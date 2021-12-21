class Categoria:
    def __init__(self, nivel) -> None:
        self._nivel=nivel

    @property
    def nivel(self):
        return self._nivel
    
    @nivel.setter
    def nivel(self, nivel):
        self._nivel=nivel