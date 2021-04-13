import math
import tkinter as tk
from tkinter import filedialog
from tkinter import *
from tkinter import ttk

from CuadradosMedios import CuadradosMedios 

class Demo1:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)

        
         # Add buttons
        self.button1 = tk.Button(self.frame,text="Metodo de los Cuadrados Medios", command=self.new_windowMedios)
        self.button1.pack(pady = 20)
        self.button1.config(width = 50, height = 5)
        self.button1.config(font=("Courier", 15))
        
        self.button2 = tk.Button( self.frame, text = "Metodo Congruencial Lineal", command=self.loadMetodoCongruencialLineal)
        self.button2.pack(pady = 20)
        self.button2.config(width = 50, height = 5)
        self.button2.config(font=("Courier", 15))
        
        self.button3 = tk.Button( self.frame, text = "Metodo Congruencial Mixto", command=self.loadMetodoCongruencialMixto)
        self.button3.pack(pady = 20)
        self.button3.config(width = 50, height = 5)
        self.button3.config(font=("Courier", 15))

        self.button4 = tk.Button( self.frame, text = "Metodo Congruencial Multiplicativo", command=self.loadMetodoCongruencialMultiplicativo)
        self.button4.pack(pady = 20)
        self.button4.config(width = 50, height = 5)
        self.button4.config(font=("Courier", 15))

        self.button5 = tk.Button( self.frame, text = "Generadores Combinados", command=self.loadMetodoCombinados)
        self.button5.pack(pady = 20)
        self.button5.config(width = 50, height = 5)
        self.button5.config(font=("Courier", 15))
        
        
        #button = Button(window, text="Refresh Screen", command=).place(x=80, y=660, width=300, height=75)

        self.frame.pack()

    def new_windowMedios(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = MediosCuadrados(self.newWindow)
    
    def loadMetodoCongruencialLineal(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = MetodoCongruencialLineal(self.newWindow)
    
    def loadMetodoCongruencialMixto(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = MetodoCongruencialMixto(self.newWindow)

    def loadMetodoCongruencialMultiplicativo(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = CongruencialMultiplicativo(self.newWindow)
    
    def loadMetodoCombinados(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = MetodoCombinado(self.newWindow)

class MediosCuadrados:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)

        self.bg = PhotoImage(file = "fondo.gif")

        self.master.geometry("1100x460")
        # Show image using label


        self.label1 = tk.Label( self.frame, image = self.bg)
        self.label1.place(x = 0, y = 0)
        self.label2 = tk.Label( self.frame, text = "Medios Cuadrados")
        self.label2.pack(pady = 25)
        self.label2.config(width=200)
        self.label2.config(font=("Courier", 44))

        self.labelAyuda = tk.Label( self.frame, text = "Procura que la semilla sea de 4 digitos")
        self.labelAyuda.pack(pady = 10)
        self.labelAyuda.config(width=200)
        self.labelAyuda.config(font=("Courier", 10))
        
        # Add buttons


        self.label3 = tk.Label( self.frame, text = "Semilla")
        self.label3.pack()
        self.label3.config(width=30)
        self.label3.config(font=("Courier", 10))

        self.semilla = ''
        self.semillaEntered = ttk.Entry(self.frame, width = 15, textvariable=self.semilla)
        
        
        self.semillaEntered.pack(pady = 20)
        self.semillaEntered.config(width=30)

        self.label4 = tk.Label( self.frame, text = "Numeros Random")
        self.label4.pack()
        self.label4.config(width=30)
        self.label4.config(font=("Courier", 10))

        self.nRandoms = ''
        self.nRandomsEntered = ttk.Entry(self.frame, width = 15, textvariable=self.nRandoms)
        self.nRandomsEntered.place(x = 400, y = 350)
        
        self.nRandomsEntered.pack(pady = 20)
        self.nRandomsEntered.config(width=30)
        #nameEntered.grid(column = 0, row = 1)



        print(self.semillaEntered.get())

        self.button1 = tk.Button(self.frame,text="Generar", command=self.generar)
        self.button1.pack(pady = 20)
        self.button1.config(width = 25, height = 2)
        self.button1.config(font=("Courier", 10))

        
        self.frame.pack()
    
    def generar(self):

        self.cuadrado = CuadradosMedios()
        semilla = self.semillaEntered.get()
        nRandoms = self.nRandomsEntered.get()

        self.cuadrado.ciclo(int(semilla), int(nRandoms))
        
        print(self.cuadrado.listaRands)

        self.label5 = tk.Label( self.frame, text = self.cuadrado.listaRands)

        
        self.label5.place(x= 300)
        self.label5.pack()

        self.label5.config(width=200)
        
        self.label5.config()
        self.label5.config(font=("Courier", 10))
            



    def close_windows(self):
        self.master.destroy()
    
class MetodoCongruencialLineal:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master, height = 1000)

        self.bg = PhotoImage(file = "fondo.gif")

        self.master.geometry("1100x630")


        ### Titulo

        self.label1 = tk.Label( self.master, image = self.bg)
        self.label1.place(x = 0, y = 0)
        self.label2 = tk.Label( self.master, text = "Medios Congruencial Lineal")
        self.label2.pack(pady = 50)
        self.label2.config(width=200)
        self.label2.config(font=("Courier", 44))

        ### Semilla
        self.labelSmilla = tk.Label( self.master, text = "Semilla")
        self.labelSmilla.place(x = 10 , y = 150)
        self.labelSmilla.config(width=30)
        self.labelSmilla.config(font=("Courier", 10))

        self.semilla = ''
        self.semillaEntered = ttk.Entry(self.master, width = 40, textvariable=self.semilla)
        self.semillaEntered.place(x = 300, y = 150)

       
        
        ### Multiplicador
        self.labelMultiplicador = tk.Label( self.master, text = "Multiplicador")
        self.labelMultiplicador.place(x= 10, y = 200)
        self.labelMultiplicador.config(width=30)
        self.labelMultiplicador.config(font=("Courier", 10))

        self.multiplicativo = ''
        self.multiplicativoEntered = ttk.Entry(self.master, width = 40, textvariable=self.multiplicativo)
        self.multiplicativoEntered.place(x = 300, y = 200)

        

        ### Incremento
        self.labelIncremento = tk.Label( self.master, text = "Incremento")
        self.labelIncremento.place(x= 10, y = 250)
        self.labelIncremento.config(width=30)
        self.labelIncremento.config(font=("Courier", 10))

        self.incremento = ''
        self.incrementoEntered = ttk.Entry(self.master, width = 40, textvariable=self.incremento)
        self.incrementoEntered.place(x = 300, y = 250)

        
        ### Modulo

        self.labelModulo = tk.Label( self.master, text = "Modulo")
        self.labelModulo.place(x= 10, y = 300)
        self.labelModulo.config(width=30)
        self.labelModulo.config(font=("Courier", 10))

        self.modulo = ''
        self.moduloEntered = ttk.Entry(self.master, width = 40, textvariable=self.modulo)
        self.moduloEntered.place(x = 300, y = 300)

        ### Boton de generar

        self.button1 = tk.Button(self.master,text="Generar")
        self.button1.place(x= 170, y = 350)
        self.button1.config(width = 25, height = 2)
        self.button1.config(font=("Courier", 10))

      
        self.frame.pack()

    def close_windows(self):
        self.master.destroy()

class MetodoCongruencialMixto:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master, height = 1000)

        self.bg = PhotoImage(file = "fondo.gif")

        self.master.geometry("1100x630")


        ### Titulo

        self.label1 = tk.Label( self.master, image = self.bg)
        self.label1.place(x = 0, y = 0)
        self.label2 = tk.Label( self.master, text = "Medios Congruencial Mixto")
        self.label2.pack(pady = 50)
        self.label2.config(width=200)
        self.label2.config(font=("Courier", 44))

        ### Semilla
        self.labelSmilla = tk.Label( self.master, text = "Semilla")
        self.labelSmilla.place(x = 10 , y = 150)
        self.labelSmilla.config(width=30)
        self.labelSmilla.config(font=("Courier", 10))

        self.semilla = ''
        self.semillaEntered = ttk.Entry(self.master, width = 40, textvariable=self.semilla)
        self.semillaEntered.place(x = 300, y = 150)

       
        
        ### Multiplicador
        self.labelMultiplicador = tk.Label( self.master, text = "Multiplicador")
        self.labelMultiplicador.place(x= 10, y = 200)
        self.labelMultiplicador.config(width=30)
        self.labelMultiplicador.config(font=("Courier", 10))

        self.multiplicativo = ''
        self.multiplicativoEntered = ttk.Entry(self.master, width = 40, textvariable=self.multiplicativo)
        self.multiplicativoEntered.place(x = 300, y = 200)

        

        ### Incremento
        self.labelIncremento = tk.Label( self.master, text = "Incremento")
        self.labelIncremento.place(x= 10, y = 250)
        self.labelIncremento.config(width=30)
        self.labelIncremento.config(font=("Courier", 10))

        self.incremento = ''
        self.incrementoEntered = ttk.Entry(self.master, width = 40, textvariable=self.incremento)
        self.incrementoEntered.place(x = 300, y = 250)

        
        ### Modulo

        self.labelModulo = tk.Label( self.master, text = "Modulo")
        self.labelModulo.place(x= 10, y = 300)
        self.labelModulo.config(width=30)
        self.labelModulo.config(font=("Courier", 10))

        self.modulo = ''
        self.moduloEntered = ttk.Entry(self.master, width = 40, textvariable=self.modulo)
        self.moduloEntered.place(x = 300, y = 300)


        ### Numero Random

        self.labelnRandom = tk.Label( self.master, text = "Numeros Random")
        self.labelnRandom.place(x = 10, y = 350)
        self.labelnRandom.config(width=30)
        self.labelnRandom.config(font=("Courier", 10))

        self.nRandoms = ''
        self.nRandomsEntered = ttk.Entry(self.master, width = 50, textvariable=self.nRandoms)
        self.nRandomsEntered.place(x = 300, y = 350)
        self.nRandomsEntered.config(width=30)
        
        ### Q

        self.labelQ= tk.Label( self.master, text = "Q")
        self.labelQ.place(x = 10, y = 400)
        self.labelQ.config(width=30)
        self.labelQ.config(font=("Courier", 10))

        self.q = ''
        self.qEntered = ttk.Entry(self.master, width = 50, textvariable=self.q)
        self.qEntered.place(x = 300, y = 400)
        self.qEntered.config(width=30)

        ### Boton de generar

        self.button1 = tk.Button(self.master,text="Generar" , command=self.cicloDeGeneradores)
        self.button1.place(x= 170, y = 450)
        self.button1.config(width = 25, height = 2)
        self.button1.config(font=("Courier", 10))

        self.frame.pack()

    def close_windows(self):
        self.master.destroy()
     
        

    def generador(self, randomNum):
        nextRandom = ((randomNum * int(self.multiplicativoEntered.get())) +
                      int(self.incrementoEntered.get())) % int(self.moduloEntered.get())

        return nextRandom

    def cicloDeGeneradores(self):
        nextRandom = int(self.semillaEntered.get())
        y = 200

        if self.hullDobell(int(self.qEntered.get())):
            for i in range(0, int(self.nRandomsEntered.get())):
                newRandom = self.generador(nextRandom)
                randomNum = float(self.generador(nextRandom))/float(self.moduloEntered.get())
                self.labelHullDobell = tk.Label( self.master, text = randomNum)
                self.labelHullDobell.place(x= 700, y = y)
                self.labelHullDobell.config(width=30)
                self.labelHullDobell.config(font=("Courier", 10))
                nextRandom = newRandom
                y = y + 30

        print(randomNum)

    def checarPrimo(self, num):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    return False
            else:
                return True
        else:
            return False

    def hullDobell(self,q):
        # i) Sea c y m primos relativo (el máximo común divisor entero c y m es 1)
        if math.gcd(int(self.incrementoEntered.get()), int(self.moduloEntered.get())) == 1:
            print("Primer chequeo de Hull-Dobell pasado")

            # ii) Si q es un número primo que divide a m ; entonces, q divide a (a-1) 𝑎≡1𝑚𝑜𝑑𝑞
            if self.checarPrimo(q):
                print((int(self.multiplicativoEntered.get())-1)/q)
                print("Segundo chequeo de Hull-Dobell pasado")

                # iii) Si 4 divide a m ; entonces, 4 divide a (a-1). Es decir, 𝑎≡1𝑚𝑜𝑑4
                if int(self.moduloEntered.get()) % 4 == 0:
                    print((int(self.multiplicativoEntered.get())-1)/4)
                    print("Hull-Dobell pasado!")
                    self.labelHullDobell = tk.Label(self.master, text = "Hull-Dobell pasado!")
                    self.labelHullDobell.place(x= 700, y = 150)
                    self.labelHullDobell.config(width=30)
                    self.labelHullDobell.config(font=("Courier", 10))
                    return True
        else:
            self.labelHullDobell = tk.Label( self.master, text = "No pasa la prueba de Hull-Dobell")
            self.labelHullDobell.place(x= 700, y = 150)
            self.labelHullDobell.config(width=30)
            self.labelHullDobell.config(font=("Courier", 10))
            return False

class CongruencialMultiplicativo:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master, height = 1000)

        self.bg = PhotoImage(file = "fondo.gif")

        self.master.geometry("1100x630")


        ### Titulo

        self.label1 = tk.Label( self.master, image = self.bg)
        self.label1.place(x = 0, y = 0)
        self.label2 = tk.Label( self.master, text = "Medios Congruencial Multiplicativo")
        self.label2.pack(pady = 50)
        self.label2.config(width=200)
        self.label2.config(font=("Courier", 44))

        ### Semilla
        self.labelSmilla = tk.Label( self.master, text = "Semilla")
        self.labelSmilla.place(x = 10 , y = 150)
        self.labelSmilla.config(width=30)
        self.labelSmilla.config(font=("Courier", 10))

        self.semilla = ''
        self.semillaEntered = ttk.Entry(self.master, width = 40, textvariable=self.semilla)
        self.semillaEntered.place(x = 300, y = 150)

       
        
        ### Multiplicador
        self.labelMultiplicador = tk.Label( self.master, text = "Multiplicador")
        self.labelMultiplicador.place(x= 10, y = 200)
        self.labelMultiplicador.config(width=30)
        self.labelMultiplicador.config(font=("Courier", 10))

        self.multiplicativo = ''
        self.multiplicativoEntered = ttk.Entry(self.master, width = 40, textvariable=self.multiplicativo)
        self.multiplicativoEntered.place(x = 300, y = 200)

        ### Modulo

        self.labelModulo = tk.Label( self.master, text = "Modulo")
        self.labelModulo.place(x= 10, y = 250)
        self.labelModulo.config(width=30)
        self.labelModulo.config(font=("Courier", 10))

        self.modulo = ''
        self.moduloEntered = ttk.Entry(self.master, width = 40, textvariable=self.modulo)
        self.moduloEntered.place(x = 300, y = 250)

        ### Boton de generar

        self.button1 = tk.Button(self.master,text="Generar")
        self.button1.place(x= 170, y = 300)
        self.button1.config(width = 25, height = 2)
        self.button1.config(font=("Courier", 10))

    
        self.frame.pack()

    def close_windows(self):
        self.master.destroy()

class MetodoCombinado:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)


        self.bg = PhotoImage(file = "fondo.gif")

        self.master.geometry("1100x630")
        # Show image using label


        self.label1 = tk.Label( self.frame, image = self.bg)
        self.label1.place(x = 0, y = 0)
        self.label2 = tk.Label( self.frame, text = "Metodo Combinado")
        self.label2.pack(pady = 50)
        self.label2.config(width=200)
        self.label2.config(font=("Courier", 44))
        
         # Add buttons
        self.button1 = tk.Button(self.frame,text="Metodo de los Cuadrados Medios")
        self.button1.pack(pady = 20)
        self.button1.config(width = 50, height = 5)
        self.button1.config(font=("Courier", 15))
        
        self.button2 = tk.Button( self.frame, text = "Metodo Congruencial Lineal")
        self.button2.pack(pady = 20)
        self.button2.config(width = 50, height = 5)
        self.button2.config(font=("Courier", 15))
        
        self.button3 = tk.Button( self.frame, text = "Metodo Congruencial ELOTRO CAMBIAME NOMBRE")
        self.button3.pack(pady = 20)
        self.button3.config(width = 50, height = 5)
        self.button3.config(font=("Courier", 15))


        self.frame.pack()

    def close_windows(self):
        self.master.destroy()


def main(): 
    root = tk.Tk()
    root.geometry("1200x850")
    
    root.title("Numeros Random")

    # Add image file
    bg = PhotoImage(file = "fondo.gif")
    
    # Show image using label


    label1 = Label( root, image = bg)
    label1.place(x = 0, y = 0)
    label2 = Label( root, text = "Generacion de Numeros Aleatorios")
    label2.pack(pady = 50)
    label2.config(width=200)
    label2.config(font=("Courier", 44))
    app = Demo1(root)
    root.mainloop()

if __name__ == '__main__':
    main()