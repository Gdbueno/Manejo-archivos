# Archivos [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios con archivos

import csv
from pickle import NONE


def ej3():
    print('Ejercicio de archivos CSV 1º')
    
    
    # Realice un programa que abra el archivo 'stock.csv'
    # en modo lectura y cuente el stock total de tornillos
    # a lo largo de todo el archivo, 
    # sumando el stock en cada fila del archivo

    # Para eso debe leer los datos del archivo
    # con "csv.DictReader", y luego recorrer los datos
    # dentro de un bucle y solo acceder a la columna "tornillos"
    # para cumplir con el enunciado del ejercicio

    # Comenzar aquí, recuerde el identado dentro de esta funcion
    archivo = open('stock.csv')
    detalle_stock = list(csv.DictReader(archivo))
    archivo.close()
    suma = 0
    for i in detalle_stock:
        linea = i
        tornillos = int(linea.get('tornillos'))
        suma += tornillos
    print('cantidad de tornillos:\n', suma)


def ej4():
    print('Ejercicios con archivos CSV 2º')
    

    # Realice un programa que abra el archivo CSV "propiedades.csv"
    # en modo lectura. Recorrar dicho archivo y contar
    # la cantidad de departamentos de 2 ambientes y la cantidad
    # de departamentos de 3 ambientes disponibles.
    # Al finalizar el proceso, imprima en pantalla los resultados.

    # Tener cuidado que hay departamentos que no tienen definidos
    # la cantidad de ambientes, verifique el texto no esté vacio
    # antes de convertirlo a entero con "int( .. )"
    # NOTA: Si desea investigar puede evitar que el programa explote
    # utilizando "try except", tema que se verá la clase que viene.

    # Comenzar aquí, recuerde el identado dentro de esta funcion
    archivo_prop = open('propiedades.csv')
    info_alquiler = list(csv.DictReader(archivo_prop))
    archivo_prop.close()
    ambientes_2 = 0
    ambientes_3 = 0
    for i in info_alquiler:
        try:
            ambientes = int(i.get('ambientes'))
        except:
            print ('Fila sin información de ambientes')
        if ambientes == 2:
            ambientes_2 += 1
        if ambientes == 3:
            ambientes_3 += 1
    print('2 ambientes:\n', ambientes_2)
    print('3 ambientes:\n', ambientes_3)

if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    ej3()
    ej4()
