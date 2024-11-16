def corr_Rs_standing(p):

    x=0.0125*26-0.00091*(250)
    Rs= 0.71*((p/18.2)+1.4)*(10**x)**1.2048
    return Rs

def corr_Rs_Marhouns(p):
    Yo=141.5/(26+131.5)
    a=185.843208
    b=1.877840
    c=3.1437
    d=1.32657
    e=1.39844
    Rs=(a*(0.71**b)*(Yo**c)*((250+460)**d)*p)**e
    return Rs