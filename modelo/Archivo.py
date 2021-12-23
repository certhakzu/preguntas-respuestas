class Archivo:


    @staticmethod
    def checarExistenciaArchivo(nombreArchivo):
        try:
            with open(nombreArchivo, 'r') as archivo:
                return True
        except FileNotFoundError as excepcion:
            return False
        except IOError as excepcion:
            return False