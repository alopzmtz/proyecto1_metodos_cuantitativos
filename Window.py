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

        container = tk.Frame(master)
        self.canvas = tk.Canvas(container)
        scrollbar = ttk.Scrollbar(
            container, orient="vertical", command=self.canvas.yview
        )
        scrollable_frame = ttk.Frame(self.canvas)
        scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")),
        )
        self.canvas.create_window((0, 0), window=scrollable_frame, anchor="w")
        self.canvas.config(width=605, height=1000)
        self.canvas.configure(yscrollcommand=scrollbar.set)

        # Add buttons
        self.button1 = tk.Button(
            scrollable_frame,
            text="Metodo de los Cuadrados Medios",
            command=self.new_windowMedios,
        )
        self.button1.pack(pady=20)
        self.button1.config(width=50, height=5)
        self.button1.config(font=("Courier", 15))

        self.button2 = tk.Button(
            scrollable_frame,
            text="Metodo Congruencial Lineal",
            command=self.loadMetodoCongruencialLineal,
        )
        self.button2.pack(pady=20)
        self.button2.config(width=50, height=5)
        self.button2.config(font=("Courier", 15))

        self.button3 = tk.Button(
            scrollable_frame,
            text="Metodo Congruencial Mixto",
            command=self.loadMetodoCongruencialMixto,
        )
        self.button3.pack(pady=20)
        self.button3.config(width=50, height=5)
        self.button3.config(font=("Courier", 15))

        self.button4 = tk.Button(
            scrollable_frame,
            text="Metodo Congruencial Multiplicativo",
            command=self.loadMetodoCongruencialMultiplicativo,
        )
        self.button4.pack(pady=20)
        self.button4.config(width=50, height=5)
        self.button4.config(font=("Courier", 15))

        self.button5 = tk.Button(
            scrollable_frame,
            text="Generadores Combinados",
            command=self.loadMetodoCombinados,
        )
        self.button5.pack(pady=20)
        self.button5.config(width=50, height=5)
        self.button5.config(font=("Courier", 15))

        container.pack()
        self.canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        # button = Button(window, text="Refresh Screen", command=).place(x=80, y=660, width=300, height=75)

        # self.frame.pack()

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

        # self.bg = PhotoImage(file="fondo.gif")

        self.master.geometry("1100x460")
        # Show image using label

        ### Titulo

        # self.label1 = tk.Label(self.master, image=self.bg)
        # self.label1.place(x=0, y=0)
        self.label2 = tk.Label(self.master, text="Medios Cuadrados")
        self.label2.pack(pady=25)
        self.label2.config(width=200)
        self.label2.config(font=("Courier", 44))

        self.labelAyuda = tk.Label(
            self.master, text="Procura que la semilla sea de 4 digitos"
        )
        self.labelAyuda.pack(pady=10)
        self.labelAyuda.config(width=200)
        self.labelAyuda.config(font=("Courier", 10))

        # Add buttons
        ### Semilla

        self.labelSmilla = tk.Label(self.master, text="Semilla")
        self.labelSmilla.place(x=10, y=200)
        self.labelSmilla.config(width=30)
        self.labelSmilla.config(font=("Courier", 10))

        self.semilla = ""
        self.semillaEntered = ttk.Entry(
            self.master, width=40, textvariable=self.semilla
        )
        self.semillaEntered.place(x=300, y=200)

        self.labelnRandom = tk.Label(self.master, text="Numeros Random")
        self.labelnRandom.place(x=10, y=250)
        self.labelnRandom.config(width=30)
        self.labelnRandom.config(font=("Courier", 10))

        self.nRandoms = ""
        self.nRandomsEntered = ttk.Entry(
            self.master, width=40, textvariable=self.nRandoms
        )
        self.nRandomsEntered.place(x=300, y=250)

        # nameEntered.grid(column = 0, row = 1)

        print(self.semillaEntered.get())

        self.button1 = tk.Button(self.master, text="Generar", command=self.generar)
        self.button1.place(x=170, y=300)
        self.button1.config(width=25, height=2)
        self.button1.config(font=("Courier", 10))

        ### Scroll Bar

        scrollbar = Scrollbar(self.master)
        scrollbar.pack(side=RIGHT, fill=Y)

        self.mylist = Listbox(self.master, yscrollcommand=scrollbar.set)

        self.mylist.pack(side=RIGHT, fill=BOTH)
        self.mylist.place(x=700, y=200)
        self.mylist.config(width=30, height=20)
        scrollbar.config(command=self.mylist.yview)

        self.frame.pack()

    def generar(self):

        self.mylist.delete(0, END)
        self.cuadrado = CuadradosMedios()
        semilla = self.semillaEntered.get()
        nRandoms = self.nRandomsEntered.get()

        self.cuadrado.ciclo(int(semilla), int(nRandoms))

        print(self.cuadrado.listaRands)

        for i in self.cuadrado.listaRands:
            self.mylist.insert(END, i)

    def close_windows(self):
        self.master.destroy()


class MetodoCongruencialLineal:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master, height=1000)

        # self.bg = PhotoImage(file="fondo.gif")

        self.master.geometry("1100x630")

        ### Titulo

        # self.label1 = tk.Label(self.master, image=self.bg)
        # self.label1.place(x=0, y=0)
        self.label2 = tk.Label(self.master, text="Método Congruencial Lineal")
        self.label2.pack(pady=50)
        self.label2.config(width=200)
        self.label2.config(font=("Courier", 44))

        ### Semilla
        self.labelSmilla = tk.Label(self.master, text="Semilla")
        self.labelSmilla.place(x=10, y=150)
        self.labelSmilla.config(width=30)
        self.labelSmilla.config(font=("Courier", 10))

        self.semilla = ""
        self.semillaEntered = ttk.Entry(
            self.master, width=40, textvariable=self.semilla
        )
        self.semillaEntered.place(x=300, y=150)

        ### Multiplicador
        self.labelMultiplicador = tk.Label(self.master, text="Multiplicador")
        self.labelMultiplicador.place(x=10, y=200)
        self.labelMultiplicador.config(width=30)
        self.labelMultiplicador.config(font=("Courier", 10))

        self.multiplicativo = ""
        self.multiplicativoEntered = ttk.Entry(
            self.master, width=40, textvariable=self.multiplicativo
        )
        self.multiplicativoEntered.place(x=300, y=200)

        ### Incremento
        self.labelIncremento = tk.Label(self.master, text="Incremento")
        self.labelIncremento.place(x=10, y=250)
        self.labelIncremento.config(width=30)
        self.labelIncremento.config(font=("Courier", 10))

        self.incremento = ""
        self.incrementoEntered = ttk.Entry(
            self.master, width=40, textvariable=self.incremento
        )
        self.incrementoEntered.place(x=300, y=250)

        ### Modulo

        self.labelModulo = tk.Label(self.master, text="Modulo")
        self.labelModulo.place(x=10, y=300)
        self.labelModulo.config(width=30)
        self.labelModulo.config(font=("Courier", 10))

        self.modulo = ""
        self.moduloEntered = ttk.Entry(self.master, width=40, textvariable=self.modulo)
        self.moduloEntered.place(x=300, y=300)

        ### Numero Random

        self.labelnRandom = tk.Label(self.master, text="Numeros Random")
        self.labelnRandom.place(x=10, y=350)
        self.labelnRandom.config(width=30)
        self.labelnRandom.config(font=("Courier", 10))

        self.nRandoms = ""
        self.nRandomsEntered = ttk.Entry(
            self.master, width=40, textvariable=self.nRandoms
        )
        self.nRandomsEntered.place(x=300, y=350)

        ### Boton de generar

        self.button1 = tk.Button(
            self.master, text="Generar", command=self.cicloDeGeneradores
        )
        self.button1.place(x=170, y=400)
        self.button1.config(width=25, height=2)
        self.button1.config(font=("Courier", 10))

        ### Scroll Bar

        scrollbar = Scrollbar(self.master)
        scrollbar.pack(side=RIGHT, fill=Y)

        self.mylist = Listbox(self.master, yscrollcommand=scrollbar.set)

        self.mylist.pack(side=RIGHT, fill=BOTH)
        self.mylist.place(x=700, y=200)
        self.mylist.config(width=30, height=20)
        scrollbar.config(command=self.mylist.yview)

        self.frame.pack()

    def generador(self, randomNum):

        nextRandom = (
            (randomNum * int(self.multiplicativoEntered.get()))
            + int(self.incrementoEntered.get())
        ) % int(self.moduloEntered.get())

        return nextRandom

    def cicloDeGeneradores(self):
        nextRandom = int(self.semillaEntered.get())
        self.mylist.delete(0, END)
        for i in range(0, int(self.nRandomsEntered.get())):
            newRandom = self.generador(nextRandom)
            randomNum = float(self.generador(nextRandom)) / float(
                self.moduloEntered.get()
            )
            self.mylist.insert(END, randomNum)
            nextRandom = newRandom

    def close_windows(self):
        self.master.destroy()


class MetodoCongruencialMixto:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master, height=1000)

        # self.bg = PhotoImage(file="fondo.gif")

        self.master.geometry("1100x630")

        ### Titulo

        # self.label1 = tk.Label(self.master, image=self.bg)
        # self.label1.place(x=0, y=0)
        self.label2 = tk.Label(self.master, text="Método Congruencial Mixto")
        self.label2.pack(pady=50)
        self.label2.config(width=200)
        self.label2.config(font=("Courier", 44))

        ### Semilla
        self.labelSmilla = tk.Label(self.master, text="Semilla")
        self.labelSmilla.place(x=10, y=150)
        self.labelSmilla.config(width=30)
        self.labelSmilla.config(font=("Courier", 10))

        self.semilla = ""
        self.semillaEntered = ttk.Entry(
            self.master, width=40, textvariable=self.semilla
        )
        self.semillaEntered.place(x=300, y=150)

        ### Multiplicador
        self.labelMultiplicador = tk.Label(self.master, text="Multiplicador")
        self.labelMultiplicador.place(x=10, y=200)
        self.labelMultiplicador.config(width=30)
        self.labelMultiplicador.config(font=("Courier", 10))

        self.multiplicativo = ""
        self.multiplicativoEntered = ttk.Entry(
            self.master, width=40, textvariable=self.multiplicativo
        )
        self.multiplicativoEntered.place(x=300, y=200)

        ### Incremento
        self.labelIncremento = tk.Label(self.master, text="Incremento")
        self.labelIncremento.place(x=10, y=250)
        self.labelIncremento.config(width=30)
        self.labelIncremento.config(font=("Courier", 10))

        self.incremento = ""
        self.incrementoEntered = ttk.Entry(
            self.master, width=40, textvariable=self.incremento
        )
        self.incrementoEntered.place(x=300, y=250)

        ### Modulo

        self.labelModulo = tk.Label(self.master, text="Modulo")
        self.labelModulo.place(x=10, y=300)
        self.labelModulo.config(width=30)
        self.labelModulo.config(font=("Courier", 10))

        self.modulo = ""
        self.moduloEntered = ttk.Entry(self.master, width=40, textvariable=self.modulo)
        self.moduloEntered.place(x=300, y=300)

        ### Numero Random

        self.labelnRandom = tk.Label(self.master, text="Numeros Random")
        self.labelnRandom.place(x=10, y=350)
        self.labelnRandom.config(width=30)
        self.labelnRandom.config(font=("Courier", 10))

        self.nRandoms = ""
        self.nRandomsEntered = ttk.Entry(
            self.master, width=50, textvariable=self.nRandoms
        )
        self.nRandomsEntered.place(x=300, y=350)
        self.nRandomsEntered.config(width=30)

        ### Boton de generar

        self.button1 = tk.Button(
            self.master, text="Generar", command=self.cicloDeGeneradores
        )
        self.button1.place(x=170, y=450)
        self.button1.config(width=25, height=2)
        self.button1.config(font=("Courier", 10))

        ### Scroll Bar

        scrollbar = Scrollbar(self.master)
        scrollbar.pack(side=RIGHT, fill=Y)

        self.mylist = Listbox(self.master, yscrollcommand=scrollbar.set)

        self.mylist.pack(side=RIGHT, fill=BOTH)
        self.mylist.place(x=700, y=200)
        self.mylist.config(width=30, height=20)
        scrollbar.config(command=self.mylist.yview)

        self.frame.pack()

    def close_windows(self):
        self.master.destroy()

    def generador(self, randomNum):
        nextRandom = (
            (randomNum * int(self.multiplicativoEntered.get()))
            + int(self.incrementoEntered.get())
        ) % int(self.moduloEntered.get())

        return nextRandom

    def cicloDeGeneradores(self):
        nextRandom = int(self.semillaEntered.get())
        self.mylist.delete(0, END)
        if self.hullDobell():
            for i in range(0, int(self.nRandomsEntered.get())):
                newRandom = self.generador(nextRandom)
                randomNum = float(self.generador(nextRandom)) / float(
                    self.moduloEntered.get()
                )
                self.mylist.insert(END, randomNum)
                nextRandom = newRandom

    def checarPrimo(self, num):
        primos = []
        while num % 2 == 0:
            primos.append(2)
            num /= 2

        for i in range(3, int(math.sqrt(num)) + 1, 2):
            while num % i == 0:
                primos.append(i)
                num /= i

        if num > 2:
            primos.append(num)

        return primos

    def hullDobell(self):
        # i) Sea c y m primos relativo (el máximo común divisor entero c y m es 1)
        if (
            math.gcd(int(self.incrementoEntered.get()), int(self.moduloEntered.get()))
            == 1
        ):
            print("Primer chequeo de Hull-Dobell pasado")
            # ii) Si q es un número primo que divide a m ; entonces, q divide a (a-1) 𝑎≡1𝑚𝑜𝑑𝑞
            for q in self.checarPrimo(int(self.moduloEntered.get())):
                print("Dentro del for")
                if (int(self.moduloEntered.get()) % q == 0) and (
                    (int(self.multiplicativoEntered.get()) - 1) % q == 0
                ):
                    print(q)
                    print("Segundo chequeo de Hull-Dobell pasado")
                    # iii) Si 4 divide a m ; entonces, 4 divide a (a-1). Es decir, 𝑎≡1𝑚𝑜𝑑4
                    if int(self.moduloEntered.get()) % 4 == 0 and (
                        (int(self.multiplicativoEntered.get()) - 1) % 4 == 0
                    ):
                        print("Hull-Dobell pasado!")
                        self.labelHullDobell = tk.Label(
                            self.master, text="Hull-Dobell pasado!"
                        )
                        self.labelHullDobell.place(x=700, y=150)
                        self.labelHullDobell.config(width=30)
                        self.labelHullDobell.config(font=("Courier", 10))
                        return True
                else:
                    print("No pasó el segundo")

        self.labelHullDobell = tk.Label(
            self.master, text="No pasa la prueba de Hull-Dobell"
        )

        self.labelHullDobell.place(x=700, y=150)
        self.labelHullDobell.config(width=30)
        self.labelHullDobell.config(font=("Courier", 10))
        return False


class CongruencialMultiplicativo:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master, height=1000)

        # self.bg = PhotoImage(file="fondo.gif")

        self.master.geometry("1100x630")

        ### Titulo

        # self.label1 = tk.Label(self.master, image=self.bg)
        # self.label1.place(x=0, y=0)
        self.label2 = tk.Label(self.master, text="Método Congruencial Multiplicativo")
        self.label2.pack(pady=50)
        self.label2.config(width=200)
        self.label2.config(font=("Courier", 44))

        ### Semilla
        self.labelSmilla = tk.Label(self.master, text="Semilla")
        self.labelSmilla.place(x=10, y=150)
        self.labelSmilla.config(width=30)
        self.labelSmilla.config(font=("Courier", 10))

        self.semilla = ""
        self.semillaEntered = ttk.Entry(
            self.master, width=40, textvariable=self.semilla
        )
        self.semillaEntered.place(x=300, y=150)

        ### Multiplicador
        self.labelMultiplicador = tk.Label(self.master, text="Multiplicador")
        self.labelMultiplicador.place(x=10, y=200)
        self.labelMultiplicador.config(width=30)
        self.labelMultiplicador.config(font=("Courier", 10))

        self.multiplicativo = ""
        self.multiplicativoEntered = ttk.Entry(
            self.master, width=40, textvariable=self.multiplicativo
        )
        self.multiplicativoEntered.place(x=300, y=200)

        ### Modulo

        self.labelModulo = tk.Label(self.master, text="Modulo")
        self.labelModulo.place(x=10, y=250)
        self.labelModulo.config(width=30)
        self.labelModulo.config(font=("Courier", 10))

        self.modulo = ""
        self.moduloEntered = ttk.Entry(self.master, width=40, textvariable=self.modulo)
        self.moduloEntered.place(x=300, y=250)

        ### Numero Random

        self.labelnRandom = tk.Label(self.master, text="Numeros Random")
        self.labelnRandom.place(x=10, y=300)
        self.labelnRandom.config(width=30)
        self.labelnRandom.config(font=("Courier", 10))

        self.nRandoms = ""
        self.nRandomsEntered = ttk.Entry(
            self.master, width=50, textvariable=self.nRandoms
        )
        self.nRandomsEntered.place(x=300, y=300)
        self.nRandomsEntered.config(width=30)

        ### Boton de generar

        self.button1 = tk.Button(
            self.master, text="Generar", command=self.cicloDeGeneradores
        )
        self.button1.place(x=170, y=350)
        self.button1.config(width=25, height=2)
        self.button1.config(font=("Courier", 10))

        ### Scroll Bar

        scrollbar = Scrollbar(self.master)
        scrollbar.pack(side=RIGHT, fill=Y)

        self.mylist = Listbox(self.master, yscrollcommand=scrollbar.set)

        self.mylist.pack(side=RIGHT, fill=BOTH)
        self.mylist.place(x=700, y=200)
        self.mylist.config(width=30, height=20)
        scrollbar.config(command=self.mylist.yview)

        self.frame.pack()

    def generador(self, randomNum):
        nextRandom = (randomNum * int(self.multiplicativoEntered.get())) % int(
            self.moduloEntered.get()
        )

        return nextRandom

    def cicloDeGeneradores(self):
        nextRandom = int(self.semillaEntered.get())
        self.mylist.delete(0, END)
        if self.validar():
            for i in range(0, int(self.nRandomsEntered.get())):
                newRandom = self.generador(nextRandom)
                randomNum = float(self.generador(nextRandom)) / float(
                    self.moduloEntered.get()
                )
                self.mylist.insert(END, randomNum)
                nextRandom = newRandom

    def validar(self):
        if (
            int(self.semillaEntered.get()) >= 0
            and int(self.moduloEntered.get()) >= 0
            and int(self.multiplicativoEntered.get()) >= 0
            and int(self.moduloEntered.get()) > int(self.semillaEntered.get())
            and int(self.moduloEntered.get()) > int(self.multiplicativoEntered.get())
        ):
            return True
        else:
            self.labelValidar = tk.Label(
                self.master, text="No pasa la prueba de validacion"
            )
            self.labelValidar.place(x=700, y=150)
            self.labelValidar.config(width=30)
            self.labelValidar.config(font=("Courier", 10))
            return False

    def close_windows(self):
        self.master.destroy()


class MetodoCombinado:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)

        # self.bg = PhotoImage(file="fondo.gif")

        self.master.geometry("1100x630")
        # Show image using label

        # self.label1 = tk.Label(self.master, image=self.bg)
        # self.label1.place(x=0, y=0)
        self.label2 = tk.Label(self.master, text="Metodo Combinado")
        self.label2.pack(pady=50)
        self.label2.config(width=200)
        self.label2.config(font=("Courier", 44))

        ### Semilla 1
        self.labelSmilla1 = tk.Label(self.master, text="Semilla 1")
        self.labelSmilla1.place(x=10, y=150)
        self.labelSmilla1.config(width=30)
        self.labelSmilla1.config(font=("Courier", 10))

        self.semilla1 = ""
        self.semillaEntered1 = ttk.Entry(
            self.master, width=40, textvariable=self.semilla1
        )
        self.semillaEntered1.place(x=300, y=150)

        ### Multiplicador 1
        self.labelMultiplicador1 = tk.Label(self.master, text="Multiplicador 1")
        self.labelMultiplicador1.place(x=10, y=200)
        self.labelMultiplicador1.config(width=30)
        self.labelMultiplicador1.config(font=("Courier", 10))

        self.multiplicativo1 = ""
        self.multiplicativoEntered1 = ttk.Entry(
            self.master, width=40, textvariable=self.multiplicativo1
        )
        self.multiplicativoEntered1.place(x=300, y=200)

        ### Modulo 1

        self.labelModulo1 = tk.Label(self.master, text="Modulo 1")
        self.labelModulo1.place(x=10, y=250)
        self.labelModulo1.config(width=30)
        self.labelModulo1.config(font=("Courier", 10))

        self.modulo1 = ""
        self.moduloEntered1 = ttk.Entry(
            self.master, width=40, textvariable=self.modulo1
        )
        self.moduloEntered1.place(x=300, y=250)

        ### Semilla 2
        self.labelSmilla2 = tk.Label(self.master, text="Semilla 2")
        self.labelSmilla2.place(x=10, y=300)
        self.labelSmilla2.config(width=30)
        self.labelSmilla2.config(font=("Courier", 10))

        self.semilla2 = ""
        self.semillaEntered2 = ttk.Entry(
            self.master, width=40, textvariable=self.semilla2
        )
        self.semillaEntered2.place(x=300, y=300)

        ### Multiplicador 2
        self.labelMultiplicador2 = tk.Label(self.master, text="Multiplicador 2")
        self.labelMultiplicador2.place(x=10, y=350)
        self.labelMultiplicador2.config(width=30)
        self.labelMultiplicador2.config(font=("Courier", 10))

        self.multiplicativo2 = ""
        self.multiplicativoEntered2 = ttk.Entry(
            self.master, width=40, textvariable=self.multiplicativo2
        )
        self.multiplicativoEntered2.place(x=300, y=350)

        ### Modulo 2

        self.labelModulo2 = tk.Label(self.master, text="Modulo 2")
        self.labelModulo2.place(x=10, y=400)
        self.labelModulo2.config(width=30)
        self.labelModulo2.config(font=("Courier", 10))

        self.modulo2 = ""
        self.moduloEntered2 = ttk.Entry(
            self.master, width=40, textvariable=self.modulo2
        )
        self.moduloEntered2.place(x=300, y=400)

        ### Numero Random

        self.labelnRandom = tk.Label(self.master, text="Numeros Random")
        self.labelnRandom.place(x=10, y=450)
        self.labelnRandom.config(width=30)
        self.labelnRandom.config(font=("Courier", 10))

        self.nRandoms = ""
        self.nRandomsEntered = ttk.Entry(
            self.master, width=50, textvariable=self.nRandoms
        )
        self.nRandomsEntered.place(x=300, y=450)
        self.nRandomsEntered.config(width=30)

        ### Boton de generar

        self.button1 = tk.Button(
            self.master, text="Generar", command=self.cicloDeGeneradores
        )
        self.button1.place(x=170, y=500)
        self.button1.config(width=25, height=2)
        self.button1.config(font=("Courier", 10))

        ### Scroll Bar

        scrollbar = Scrollbar(self.master)
        scrollbar.pack(side=RIGHT, fill=Y)

        self.mylist = Listbox(self.master, yscrollcommand=scrollbar.set)

        self.mylist.pack(side=RIGHT, fill=BOTH)
        self.mylist.place(x=700, y=200)
        self.mylist.config(width=30, height=20)
        scrollbar.config(command=self.mylist.yview)

        self.frame.pack()

    def generador_1(self, randomNum):
        nextRandom = (randomNum * int(self.multiplicativoEntered1.get())) % int(
            self.moduloEntered1.get()
        )
        return nextRandom

    def generador_2(self, randomNum):
        nextRandom = (randomNum * int(self.multiplicativoEntered2.get())) % int(
            self.moduloEntered2.get()
        )
        return nextRandom

    def cicloDeGeneradores(self):
        self.mylist.delete(0, END)
        nextRandom_1 = int(self.semillaEntered1.get())
        nextRandom_2 = int(self.semillaEntered2.get())
        modulo = 1
        if int(self.moduloEntered1.get()) > int(self.moduloEntered2.get()):
            modulo = int(self.moduloEntered1.get())
        else:
            modulo = int(self.moduloEntered2.get())

        for i in range(0, int(self.nRandomsEntered.get())):
            newRandom_1 = self.generador_1(nextRandom_1)
            newRandom_2 = self.generador_2(nextRandom_2)
            nextRandom = (newRandom_1 - newRandom_2) % (modulo)
            randomNum = float(nextRandom) / (modulo)
            self.mylist.insert(END, randomNum)
            nextRandom_1 = newRandom_1
            nextRandom_2 = newRandom_2

        print(randomNum)

    def close_windows(self):
        self.master.destroy()


def main():
    root = tk.Tk()
    root.geometry("1200x850")

    root.title("Numeros Random")

    # Add image file
    # bg = PhotoImage(file="fondo.gif")

    # Show image using label

    label2 = Label(root, text="Generacion de Numeros Aleatorios")
    label2.pack(pady=50)
    label2.config(width=200)
    label2.config(font=("Courier", 44))
    app = Demo1(root)
    root.mainloop()


if __name__ == "__main__":
    main()