#valores
Rs=float(input("ingrese valores de solubilidad: "))
Yg=float(input("Ingrese la gravedad del gas: "))
API=float(input("ingrese la gravedad del crudo: "))
T=float(input("Ingrese temperatura en (°R) : "))

#Correlaciones
def corr_Pb():
#standing
    a=0.00091*(T-460)-0.0125*(API)
    Pb=18.2*(((Rs/Yg)**0.83)*(10)**a-1.4)

    #Marhoun's
    A=5.38088*(10**-3)
    B=0.715082
    C=-1.87784
    D=3.1437
    E=1.32657
    Yo= 141.5/(API+131.5)

    pb=A*(Rs**B)*(Yg**C)*(Yo**D)*(T**E)

#Solubilidad del gas Rs
def corr_Rs(T,API,Yo,p,opcion):
    if opcion == 1:
        #Standing
        p=float(input("Ingrese el valor de Presion: "))
        x=0.0125*API-0.00091*(T-460)
        Rs= Yg*((p/18.2)+1.4)*(10**x)**1.2048

    else:
        #Marhouns
        a=185.843208
        b=1.877840
        c=3.1437
        d=1.32657
        e=1.39844
        Rs=(a*(Yg**b)*(Yo**c)*(T**d)*p)**e

# Bo correlaciones
def corr_Bo(T,Yo,Yg,opcion):
#Standing
    if opcion == 1:
        Bo= 0.9759+0.000120*(Rs(Yg/Yo)**0.5+1.25*(T-460))**1.2
#Marhouns
    else:
        a=0.7422390
        b=0.323294
        c=-1.202040
        F=(Rs**a)*(Yg**b)*(Yo**c)
        Bo= 0.497069 + 0.000862963*T + 0.00182594*F + 0.00000318099*(F**2)

def corr_dens(T,Yo,Yg,opcion):
    if opcion == 1:
        po=(62.4*Yo+0.0136*Rs*Yg)/(0.972+0.000147*(Rs*(Yg/Yo)**0.5+1.25(T-460))**1.175)
    else:

