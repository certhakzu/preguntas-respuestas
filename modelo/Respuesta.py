class Respuesta:
    def __init__(self, descripcion, valida) -> None:
        self._descripcion=descripcion
        self._valida=valida

    @property
    def descripcion(self):
        return self._descripcion
    
    @property
    def valida(self):
        return self._valida

    @descripcion.setter
    def descripcion(self, descripcion):
        self._descripcion=descripcion

    @valida.setter
    def valida(self, valida):
        self._valida=valida