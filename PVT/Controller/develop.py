import xlwings as xw
import numpy as np
from PVT.mode.Rs import corr_Rs_standing,corr_Rs_Marhouns
from PVT.mode.Pb import corr_Pb_standing,corr_Pb_Marhoun
from PVT.mode.Bo import corr_Bo_standing,corr_Bo_Marhouns
from PVT.mode.Po import corr_dens_standing,corr_dens
from PVT.mode.Co import corr_co_Standing,corr_co_Vaszques_Beggs
from PVT.mode.Uo import corr_Uo_Beals

#defino celda
SUMMARY="Summary"
RESULTS="Results"
#llamo nombres de variables
VARIABLES="Variables"
VALUES="Values"
#LLAMO CELDAS

DET_PRESIONES="det_presiones"
DET_RS="det_rs"
DET_VALUES="det_values"
DET_VALUESRS="det_valuesrs"
DET_VALUESBO="det_valuesbo"
DET_VALUESPB="det_valuespb"
DET_VALUESPO="det_valuespo"
DET_VALUESCO="det_valuesco"
DET_VALUESUO="det_valuesuo"
DET_T="det_t"



BO_MARHOUNS="Bo_Marhouns"
BO_STANDING="Bo_Standing"
CO_STANDING="Co_Standing"
CO_VASQUEZ="Co_Vasquez"
PB_STANDING="Pb_Standing"
PB_MARHOUNS="Pb_Marhouns"
PO_CORRLAB="Po_CorrLab"
PO_STANDING="Po_Standing"
RS_MARHOUNS="Rs_Marhouns"
RS_STANDING="Rs_Standing"
UO_BEALS="Uo_Beals"

def main():
    wb = xw.Book.caller()
    sheet = wb.sheets[SUMMARY]

    params = sheet[DET_PRESIONES].options(np.array, transpose=True).value
    parampb= sheet[DET_RS].options(np.array, transpose=True).value
    parambo= sheet[BO_STANDING].options(np.array, transpose=True).value
    parambuo= sheet[DET_T].options(np.array, transpose=True).value

    P= sheet[DET_PRESIONES].options(np.array, transpose=True).value
    PB = sheet[DET_VALUESPB].options(np.array, transpose=True).value



    tot=corr_co_Standing(P,PB)
    totco=corr_co_Vaszques_Beggs(P,parampb)

    resultados = list(map(corr_Rs_standing, params))
    resultados2= list(map(corr_Rs_Marhouns, params))

    pb=list(map(corr_Pb_standing, parampb))
    pb2=list(map(corr_Pb_Marhoun, parampb))

    bo=list(map(corr_Bo_standing, parampb))
    bo2=list(map(corr_Bo_Marhouns, parampb))

    uo=list(map(corr_Uo_Beals, parambuo))

    po=list(map(corr_dens_standing, parampb))
    Po = corr_dens(parampb, parambo)

    # Asigna los resultados a la hoja de cálculo
    sheet[RS_STANDING].options(transpose=True).value = resultados
    sheet[RS_MARHOUNS].options(transpose=True).value = resultados2

    sheet[PB_STANDING].options(transpose=True).value = pb
    sheet[PB_MARHOUNS].options(transpose=True).value = pb2

    sheet[BO_STANDING].options(transpose=True).value = bo
    sheet[BO_MARHOUNS].options(transpose=True).value = bo2

    sheet[UO_BEALS].options(transpose=True).value = uo

    sheet[CO_STANDING].options(transpose=True).value = tot
    sheet[CO_VASQUEZ].options(transpose=True).value = totco

    sheet[PO_STANDING].options(transpose=True).value = po
    sheet[PO_CORRLAB].options(transpose=True).value = Po


if __name__ == "__main__":
    xw.Book("PVT.xlsm").set_mock_caller()
    main()