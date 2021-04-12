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
        
        self.button3 = tk.Button( self.frame, text = "Metodo Congruencial ELOTRO CAMBIAME NOMBRE", command=self.loadMetodoOtro)
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
        self.app = MetodoCongruencial(self.newWindow)
    
    def loadMetodoOtro(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = MetodoOtro(self.newWindow)

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

        self.bg = PhotoImage(file = "fondo.png")

        self.master.geometry("1100x460")
        # Show image using label


        self.label1 = tk.Label( self.frame, image = self.bg)
        self.label1.place(x = 0, y = 0)
        self.label2 = tk.Label( self.frame, text = "Medios Cuadrados")
        self.label2.pack(pady = 50)
        self.label2.config(width=200)
        self.label2.config(font=("Courier", 44))
        
         # Add buttons


        self.label3 = tk.Label( self.frame, text = "Semilla")
        self.label3.pack()
        self.label3.config(width=30)
        self.label3.config(font=("Courier", 10))

        self.semilla = ''
        self.semillaEntered = ttk.Entry(self.frame, width = 15, textvariable=self.semilla)
        self.semillaEntered.place(x = 400, y = 250)
        
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
    
class MetodoCongruencial:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)



        self.bg = PhotoImage(file = "fondo.png")

        self.master.geometry("1100x630")
        # Show image using label


        self.label1 = tk.Label( self.frame, image = self.bg)
        self.label1.place(x = 0, y = 0)
        self.label2 = tk.Label( self.frame, text = "Metodo Congruencial Lineal")
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

class MetodoOtro:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)


        self.bg = PhotoImage(file = "fondo.png")

        self.master.geometry("1100x630")
        # Show image using label


        self.label1 = tk.Label( self.frame, image = self.bg)
        self.label1.place(x = 0, y = 0)
        self.label2 = tk.Label( self.frame, text = "Otro")
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

class CongruencialMultiplicativo:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)


        self.bg = PhotoImage(file = "fondo.png")

        self.master.geometry("1100x630")
        # Show image using label


        self.label1 = tk.Label( self.frame, image = self.bg)
        self.label1.place(x = 0, y = 0)
        self.label2 = tk.Label( self.frame, text = "Congruencial Multiplicativo")
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

class MetodoCombinado:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)


        self.bg = PhotoImage(file = "fondo.png")

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
    bg = PhotoImage(file = "fondo.png")
    
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