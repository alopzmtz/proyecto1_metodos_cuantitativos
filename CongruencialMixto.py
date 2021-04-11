import math


class CongruencialMixto:
    def __init__(self, multiplicativo, incremento, modulo, semilla):
        self.multiplicativo = multiplicativo
        self.incremento = incremento
        self.modulo = modulo
        self.semilla = semilla

    def generador(self, randomNum):
        nextRandom = ((randomNum * self.multiplicativo) +
                      self.incremento) % self.modulo

        return nextRandom

    def cicloDeGeneradores(self, noRandomNum, q):
        nextRandom = self.semilla
        randomNum = []

        if self.hullDobell(q):
            for i in range(0, noRandomNum):
                newRandom = self.generador(nextRandom)
                randomNum.append(float(self.generador(nextRandom))/self.modulo)
                nextRandom = newRandom

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

    def hullDobell(self, q):
        # i) Sea c y m primos relativo (el máximo común divisor entero c y m es 1)
        if math.gcd(self.incremento, self.modulo) == 1:
            print("Primer chequeo de Hull-Dobell pasado")

            # ii) Si q es un número primo que divide a m ; entonces, q divide a (a-1) 𝑎≡1𝑚𝑜𝑑𝑞
            if self.checarPrimo(q):
                print((self.multiplicativo-1)/q)
                print("Segundo chequeo de Hull-Dobell pasado")

                # iii) Si 4 divide a m ; entonces, 4 divide a (a-1). Es decir, 𝑎≡1𝑚𝑜𝑑4
                if self.modulo % 4 == 0:
                    print((self.multiplicativo-1)/4)
                    print("Hull-Dobell pasado!")
                    return True
        else:
            print("No paso el chequeo Hull-Dobell")
            return False


'''
cmg = CongruencialMixto(5, 7, 8, 4)
cmg.cicloDeGeneradores(20, 2)
'''
