import scipy.stats as ss


def test_chicuadrado(data, N):
    n = data.count()
    freqs, edges, _ = ss.binned_statistic(data, data, statistic="count")

    def ei(i):
        return n*(N.cdf(edges[i]) - N.cdf(edges[i-1]))
    expected = [ei(i) for i in range(1, len(edges))]
    return ss.chisquare(freqs, expected)


def test_kolmogorov(data):
    media, desviacion = ss.norm.fit(data)
    d, pvalor = ss.ktest(data, "norm", args=(media, desviacion))
    return pvalor
