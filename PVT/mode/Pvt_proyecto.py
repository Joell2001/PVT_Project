#valores
Rs=float(input("ingrese valores de solubilidad: "))
Yg=float(input("Ingrese la gravedad del gas: "))
API=float(input("ingrese la gravedad del crudo: "))
T=float(input("Ingrese temperatura en (°R) : "))

#Correlaciones

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

#Standing
p=float(input("Ingrese el valor de Presion: "))
x=0.0125*API-0.00091*(T-460)
Rs= Yg*((p/18.2)+1.4)*(10**x)**1.2048

#Marhouns
a=185.843208
b=1.877840
c=3.1437
d=1.32657
e=1.39844

Rs=(a*(Yg**b)*(Yo**c)*(T**d)*p)**e