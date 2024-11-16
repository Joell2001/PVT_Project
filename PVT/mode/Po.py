def corr_dens_standing(Rs):
    Yo=141.5/(26+131.5)
    po=(62.4*Yo+0.0136*Rs*0.71)/(0.972+0.000147*(Rs*((0.71/Yo)**0.5)+1.25*(250))**1.175)

    return po

def corr_dens(Rs,bo):
    Yo=141.5/(26+131.5)
    po =(62.4*Yo+0.0136*Rs*0.71)/bo

    return po