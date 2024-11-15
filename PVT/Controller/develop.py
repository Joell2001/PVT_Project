import xlwings as xw
import os
from openpyxl import Workbook

def exportar_a_excel(dataframe, nombre_archivo="data.xlsx", nombre_hoja="Datos"):
    carpeta = os.path.join(os.getcwd(), "Controller")
    ruta_archivo = os.path.join(carpeta, nombre_archivo)

    if not os.path.exists(ruta_archivo):
        libro = Workbook()
        libro.save(ruta_archivo)

    try:
        libro_excel = xw.Book(ruta_archivo)
    except FileNotFoundError:
        raise FileNotFoundError(f"El archivo '{ruta_archivo}' no existe.")

    if nombre_hoja in [hoja.name for hoja in libro_excel.sheets]:
        hoja = libro_excel.sheets[nombre_hoja]
    else:
        hoja = libro_excel.sheets.add(nombre_hoja)

    hoja.range("A1").value = dataframe

    libro_excel.save()
