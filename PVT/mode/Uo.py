def corr_Uo_Beals(T):
    a = (10) ** (0.42 + (8.33 / 26))
    uod = 0.32 + ((18 * (10 ** 7)) / 26 ** 4.53) * (360 / ((T+460) - 260)) ** a
    return uod