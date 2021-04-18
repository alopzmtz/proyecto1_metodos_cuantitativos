'''
Este programa crea numeros aleatorios utilizando el metodo de los cuadrados medios.
Para un numero entero de 4 digitos (el primero por la izquierda puede ser 0)
'''


class CuadradosMedios:

    
    def _init_(self):
        self.rand = 0
        self.semilla = 0
        self.nRandoms = 0
        self.listaRands = []
        

    def generarRi(self, rando):
        random = rando/10000.0
        print("Random generado " + str(random))
        self.listaRands.append(random)
        self.rand = random
        self.semilla = rando

    def numAleatorio(self,x_cuadrada):
        x_cuadrada_string = list(str(x_cuadrada))
        new_num = ""
        if len(x_cuadrada_string) == 5:
            x_cuadrada_string.insert(0, 0)
        if len(x_cuadrada_string) == 6:
            x_cuadrada_string.insert(0, 0)
        if len(x_cuadrada_string) == 7:
            x_cuadrada_string.insert(0, 0)
        for x in range(2, len(x_cuadrada_string)-2):
            new_num += str(x_cuadrada_string[x])
        print(new_num, x_cuadrada_string)
        self.generarRi(int(new_num))
    

    def generador(self,raiz):
        x_cuadrada = raiz * raiz
        self.numAleatorio(int(x_cuadrada))
    
    def ciclo(self, semilla, nRandoms):
        self.semilla = semilla
        self.nRandoms = nRandoms
        self.listaRands = []
        for i in range(self.nRandoms):
            self.generador(self.semilla)

    

