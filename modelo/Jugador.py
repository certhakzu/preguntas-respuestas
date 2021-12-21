class Jugador:
    """
    Jugador
    """
    def __init__(self, nombres, apellidos, edad, CC, puntaje) -> None:
        #Valores por defecto
        self._nombres=nombres
        self._apellidos=apellidos
        self._edad=edad
        self._CC=CC
        self._puntaje=puntaje

        @property
        def nombres(self):
            return self._nombres
        
        @property
        def apellidos(self):
            return self._apellidos

        @property
        def edad(self):
            return self._edad

        @property
        def CC(self):
            return self._CC
            
        @property
        def puntaje(self):
            return self._puntaje

        @nombres.setter
        def nombres(self, nombres):
            self._nombres=nombres

        @apellidos.setter
        def apellidos(self, apellidos):
            self._apellidos=apellidos

        @edad.setter
        def edad(self, edad):
            self._edad=edad

        @CC.setter
        def CC(self, CC):
            self._CC=CC

        @puntaje.setter
        def puntaje(self, puntaje):
            self._puntaje=puntaje