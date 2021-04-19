import math


class CongruencialMixto:
    def __init__(self, multiplicativo, incremento, modulo, semilla):
        self.multiplicativo = multiplicativo
        self.incremento = incremento
        self.modulo = modulo
        self.semilla = semilla

    def generador(self, randomNum):
        nextRandom = ((randomNum * self.multiplicativo) + self.incremento) % self.modulo

        return nextRandom

    def cicloDeGeneradores(self, noRandomNum):
        nextRandom = self.semilla
        randomNum = []

        if self.hullDobell():
            for i in range(0, noRandomNum):
                newRandom = self.generador(nextRandom)
                randomNum.append(float(self.generador(nextRandom)) / self.modulo)
                nextRandom = newRandom

        print(randomNum)

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
        if math.gcd(self.incremento, self.modulo) == 1:
            print("Primer chequeo de Hull-Dobell pasado")

            # ii) Si q es un número primo que divide a m ; entonces, q divide a (a-1) 𝑎≡1𝑚𝑜𝑑𝑞
            for q in self.checarPrimo(self.modulo):
                print("Dentro del for")
                if (self.modulo % q == 0) and ((self.multiplicativo - 1) % q == 0):
                    print("Dentro del if")
                    print(q)
                    print("Segundo chequeo de Hull-Dobell pasado")

                    # iii) Si 4 divide a m ; entonces, 4 divide a (a-1). Es decir, 𝑎≡1𝑚𝑜𝑑4
                    if self.modulo % 4 == 0 and ((self.multiplicativo - 1) % 4 == 0):
                        print("Hull-Dobell pasado!")
                        return True
                    else:
                        print("No pasó el 3ro")
                else:
                    print(str(q) + "No cumple con el segundo chequeo")

        print("No pasó Hull-Dobell")
        return False


"""
4,5,7,8
27,8,47,100
cmg = CongruencialMixto(8, 47, 100, 27)
cmg.cicloDeGeneradores(20)
"""
cmg = CongruencialMixto(5, 7, 8, 4)
cmg.cicloDeGeneradores(20)
