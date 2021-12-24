###  PERTENECE A LA VISTA
import json
import os

from Archivo import Archivo


class Inicio:

    def __int__(self):
        self._preguntas = list()
        self._respuestas = list()
        self._validas = list()
        self._historicos = list()

    @property
    def preguntas(self):
        return self._preguntas
    @preguntas.setter
    def preguntas(self, preguntas):
        self._preguntas = preguntas

    @property
    def respuestas(self):
        return self._respuestas

    @respuestas.setter
    def respuestas(self, respuestas):
        self._respuestas = respuestas

    @property
    def validas(self):
        return self._validas

    @validas.setter
    def validas(self, validas):
        self._validas

    @property
    def historicos(self):
        return self._historicos

    @historicos.setter
    def historicos(self, historicos):
        self._historicos = historicos

    ############################################################
    def inicio(self):
        while True:
            os.system("cls")
            opci = self.menuPrincipal
            if opci == 4:
                break
    ###########################################################

    def _existeConcurso(self):
        if Archivo.checarExistenciaArchivo("preguntas.json") and Archivo.checarExistenciaArchivo("respuestas.json") and Archivo.checarExistenciaArchivo("validas.json"):
            return True
        else:
            return False
    ############################################################

    @property
    def menuPrincipal(self):
        # Si existen los archivos de un concurso anterior
        if self._existeConcurso():
            # with open("preguntas.json", 'r') as archi:
            #     self._preguntas = list(json.load(archi))
            # with open("respuestas.json", 'r') as archi:
            #     self._respuestas = list(json.load(archi))
            # with open("validas.json", 'r') as archi:
            #     self._validas = list(json.load(archi))

            try:
                print(f'CONCURSO PROGUNTAS Y RESPUESTAS'.center(50, "-"))
                op = int(input(f'1 -> Crear Concurso Nuevo\n2 -> Ver Historicos\n3 -> Jugar Concurso\n4 -> Salir\n\nDigite Opción ==> '))
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
    def _llenarConcurso(self):
        preguntas = list()
        listaOpciones = list()
        listaValidas = list()

        for i in range(25):
            preguntas.append(input(f'Escriba Pregunta {i + 1}: '))
            opciones = list()
            validas = list()
            for j in range(4):
                opciones.append(input(f'Opción {j + 1}: '))
                swValida=int(input(f'Es la Correcta? (1:SI / 2:NO): '))
                if swValida == 1:
                    validas.append(True)
                else:
                    validas.append(False)
            listaOpciones.append(opciones)
            listaValidas.append(validas)

        # Guardar en PERSITENCIA ********
        self.guardarPreguntasRespuestas(preguntas, listaOpciones, listaValidas)

    #####################################################################

    def guardarPreguntasRespuestas(self, preguntas, opciones, validas):
        l_preguntas = list(preguntas)
        with open('preguntas.json', 'w') as archivo:
            json.dump(l_preguntas, archivo)
        l_opciones = list(opciones)
        with open('respuestas.json', 'w') as archivo:
            json.dump(l_opciones, archivo)
        l_validas = list(validas)
        with open('validas.json', 'w') as archivo:
            json.dump(l_validas, archivo)

    ###################################################################
    @property
    def crearConcurso(self):
        #Si ya existe un Concurso avisar que lo va a borrar y pedir confirmación
        if self._existeConcurso():
            o=int(input(f'SE VA A ELIMINAR El CONCURSO YA CREADO (1:SI / 2:NO): '))
            if o == 1:

                os.remove("preguntas.json")
                os.remove("respuestas.json")
                os.remove("validas.json")
                os.remove("historicos.json")

                # Como No Existe un Concurso Crear uno nuevo

                self._llenarConcurso

            elif o == 2:
                print(f'Regresando al Menú anterior...')
                input()
                return
        else:
            print(f'Creando Concurso')
            self._llenarConcurso



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
