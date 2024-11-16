def corr_co_Standing(p,pb):
    co = (10 ** (-6)) * 2.72 * ((pb + 0.004347 * (p - pb) - 79.1) / 0.0007141 * (p - pb) - 12.398)

    return co

def corr_co_Vaszques_Beggs(p,Rs):
    co = (-1433 + 5 * Rs + 17.2 * (250) - 1180 * 0.71 + 12.61 * 26) / ((10 ** 5) * p)

    return co