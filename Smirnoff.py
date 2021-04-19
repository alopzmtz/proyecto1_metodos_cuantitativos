import math
import scipy.stats as ss
import scipy.integrate as integrate


def smirnoff(data, alpha):
    N = len(data)
    D_plus = []
    D_minus = []
    _random = sorted(data)

    # Calculate max(i/N-Ri)
    for i in range(1, N + 1):
        x = i / N - _random[i - 1]
        D_plus.append(x)

    # Calculate max(Ri-((i-1)/N))
    for i in range(1, N + 1):
        y = (i - 1) / N
        y = _random[i - 1] - y
        D_minus.append(y)
    # Calculate max(D+, D-)

    D = max(max(D_plus), max(D_minus))
    ks_critical_value = ss.ksone.ppf(1 - alpha/2, N)
    if(D > ks_critical_value):
        return "La hipotesis es rechazada - Kolmogorov"
    elif(D < ks_critical_value):
        return "La hipotesis es acepatada - Kolmogorov"


def chi_square(data, alpha):
    print(data)
    data_sorted = sorted(data)
    rango = data[-1] - data[0]
    k = math.floor(1 + (3.322 * math.log10(len(data))))
    eX = 1/(sum(data)/len(data))
    clase = rango/k
    sub_n = []
    e_n = []
    clase_start = 0
    clase_end = clase

    def sub_nCreation(clase_start, clase_end, data):
        counter = 0
        for i in data:
            if(i >= clase_start and i <= clase_end):
                counter += 1
            elif (i >= clase_end):
                return counter

    def integral(x):
        return eX * math.exp(-eX*x)

    for x in range(k):
        integlarRes = integrate.quad(integral, clase_start, clase_end)
        ans = sub_nCreation(clase_start, clase_end, data_sorted)
        sub_n.append(ans)
        e_n.append(integlarRes[0] * 50)
        clase_start += clase
        clase_end += clase

    x02 = 0
    for x in range(k):
        x02 += (sub_n[x] - e_n[x])**2/e_n[x]

    grado_libertad = ((k-1) - 1)
    crit = ss.chi2.ppf(alpha, grado_libertad)

    if(x02 > crit):
        return "La hipotesis es rechazada - chi square"
    elif(x02 < crit):
        return "La hipotesis es acepatada - chi square"
