class Premio:

    def __init__(self, valor):
        self._valor = valor
        # self._tipo = tipo

    @property
    def valor(self):
        return self._valor

    # @property
    # def tipo(self):
    #     return self._tipo

    @valor.setter
    def valor(self, valor):
        self._valor=valor

    # @tipo.setter
    # def tipo(self, tipo):
    #     self._tipo=tipo


if __name__ == '__main__':
    premio0 = Premio(23)
    print(premio0)
