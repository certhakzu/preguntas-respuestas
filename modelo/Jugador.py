import Premio

class Jugador:
    contadorID=0

    def __init__(self, nombres, apellidos, edad, CC, puntaje) -> None:
        self._nombres=nombres
        self._apellidos=apellidos
        self._edad=edad
        self._CC=CC
        self._puntaje=puntaje
        self._ID=Jugador._generarID()
        

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

    @property
    def ID(self):#Solo lectura
        return self.ID

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

    @classmethod
    def _generarID(cls):
        cls.contadorID=cls.contadorID+1

    def __str__(self) -> str:
        return f'{self._nombres} {self._apellidos} {self._CC} {self._edad} {self._puntaje}'

    def sumarPremio(self, premio):
        self._puntaje=self._puntaje + premio