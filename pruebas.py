import csv

matriz = []

with open('archivo.csv', newline='') as archivo_csv:
    lector_csv = csv.reader(archivo_csv, delimiter=',')
    for fila in lector_csv:
        matriz.append(fila)


print("matriz",matriz)

print( "fila 0",matriz[1][1])
r = float(matriz[1][1])
print(type(r))