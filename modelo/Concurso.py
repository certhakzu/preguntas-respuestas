from Jugador import Jugador


class Concurso:
    N_PREGUNTAS = 25

    def __init__(self) -> None:
        self._nombre = ""
        self._preguntas = list()
        self._repuestas = list()
        self._historico = list()

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def preguntas(self):
        return self._preguntas

    @preguntas.setter
    def preguntas(self, preguntas):
        self._preguntas = preguntas

    @property
    def respuestas(self):
        return self._repuestas

    @respuestas.setter
    def respuestas(self, respuestas):
        self._repuestas = respuestas

    # CONFIGURAR JUEGO
    def configurarJuego(self, nombre, preguntas, respuestas):
        self._nombre = nombre
        self._preguntas = list(preguntas)
        self._respuestas = list(respuestas)
