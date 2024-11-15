def corr_Bo_standing(T,API,Yg,Rs):
    Yo=141.5/(API+131.5)
    Bo= 0.9759+0.000120*(Rs(Yg/Yo)**0.5+1.25*(T-460))**1.2
    return Bo

def corr_Bo_Marhouns(T,API,Yg,Rs):
        a=0.7422390
        b=0.323294
        c=-1.202040
        Yo = 141.5 / (API + 131.5)
        F=(Rs**a)*(Yg**b)*(Yo**c)
        Bo= 0.497069 + 0.000862963*T + 0.00182594*F + 0.00000318099*(F**2)
        return Bo