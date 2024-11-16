def corr_Pb_standing(Rs):
    a=0.00091*(250)-0.0125*(26)
    Pb=18.2*(((Rs/0.71)**0.83)*(10)**a-1.4)

    return Pb

def corr_Pb_Marhoun(Rs):
    A=5.38088*(10**-3)
    B=0.715082
    C=-1.87784
    D=3.1437
    E=1.32657
    Yo= 141.5/(26+131.5)
    Pb=A*(Rs**B)*(0.71**C)*(Yo**D)*((250+460)**E)

    return Pb