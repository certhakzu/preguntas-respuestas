import Categoria


class Pregunta:
    def __init__(self, descripcion, dificultad, opciones) -> None:
        self._descripcion=descripcion
        self._dificultad=Categoria(dificultad)
        self._opciones=list(opciones)

    @property
    def descripcion(self):
        return self._descripcion
    
    @property
    def dificultad(self):
        return self._dificultad
    
    @property
    def opciones(self):
        return self._opciones

    @descripcion.setter
    def descripcion(self, descripcion):
        self._descripcion=descripcion

    @dificultad.setter
    def dificultad(self, dificultad):
        self._dificultad=dificultad

    @opciones.setter
    def opciones(self, opciones):
        self._opciones=opciones