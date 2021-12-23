###  PERTENECE A LA VISTA
import json
import os

from Concurso import Concurso
from Archivo import Archivo


class Inicio:

    def __init__(self) -> None:
        self._concurso = Concurso()

    @property
    def concurso(self):
        return self._concurso

    @concurso.setter
    def concurso(self, nombre, preguntas, respuestas):
        self._concurso

    ############################################################
    def inicio(self):

        while True:
            opci = self.menuPrincipal
            if opci == 4:
                break
    ###########################################################

    def _existeConcurso(self):
        if Archivo.checarExistenciaArchivo("concurso.json") and Archivo.checarExistenciaArchivo("preguntas.json") and Archivo.checarExistenciaArchivo("respuestas.json") and Archivo.checarExistenciaArchivo("historicos.json"):
            return True
        else:
            return False


    @property
    def menuPrincipal(self):
        # Si existen los archivos de un concurso anterior
        if self._existeConcurso():
            with open("concurso.json", 'r') as archi:
                self._concurso.nombre = list(json.load(archi))
            with open("proguntas.json", 'r') as archi:
                self._concurso.preguntas = list(json.load(archi))
            with open("respuestas.json", 'r') as archi:
                self._concurso.respuestas = list(json.load(archi))
            with open("historicos.json", 'r') as archi:
                self._concurso.nombre = list(json.load(archi))

            try:
                print(f'CONCURSO PROGUNTAS Y RESPUESTAS'.center(50, "-"))
                op = int(input(
                    f'1 -> Crear Concurso Nuevo\n2 -> Ver Historicos\n3 -> Jugar Concurso\n4 -> Salir\n\nDigite Opción ==> '))
                if op == 1:
                    self.crearConcurso
                elif op == 2:
                    self.verHistoricos()
                elif op == 3:
                    self.jugarConcurso()
                elif op == 4:
                    self.salir()
                else:
                    print(f'DEBE INGRESAR UNA OPCIÓN entre 1 y 4 !!!')
                    input()
                return op
            except:
                print(f'ASEGURECE DE DIGITAR UNA OPCIÓN VÁLIDA!!! XD')
                input()
                return 0  # valor por defecto si hubo un error en lo digitado por el usuario
        else:
            print(f'NO EXISTE CONCURSO... CREELO A CONTINUACIÓN...')
            input()
            self.crearConcurso

    #####################################################################

    @property
    def crearConcurso(self):
        #Si ya existe un Concurso avisar que lo va a borrar y pedir confirmación
        if self._existeConcurso():
            o=int(input(f'SE VA A ELIMINAR UN CONCURSO YA CREADO (1:SI / 2:NO): '))
            if o == 1:
                os.remove("concurso.json")
                os.remove("preguntas.json")
                os.remove("respuestas.json")
                os.remove("historicos.json")

                # Como No Existe un Concurso Crear uno nuevo
                nombreConcurso = input(f'Nombre del Concurso: ')
                preguntas = list()
                listaOpciones = list()
                for i in range(25):
                    preguntas.append(input(f'Escriba Pregunta {i + 1}: '))
                    # Guardar en PERSITENCIA
                    opciones = list()
                    validas = list()
                    for j in range(4):
                        opciones.append(input(f'Opción {j + 1}: '))
                        swValida=input(f'Esla Correcta? (1:SI / 2:NO): ')
                        if swValida == 1:
                            validas.append(True)
                        else:
                            validas.append(False)
                    listaOpciones.append(opciones)

                print(preguntas)
                print(listaOpciones)
                print(validas)
                
            else:
                print(f'OK REGRESANDO AL MENÚ PRINCIPAL Presione ENTER para continuar...')
                input()
        else:


    def verHistoricos(self):
        pass

    def jugarConcurso(self):
        pass

    def salir(self):
        pass


####################PRUEBA################
if __name__ == '__main__':
    ini = Inicio()
    ini.inicio()
