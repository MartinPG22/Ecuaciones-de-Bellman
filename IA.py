import random
import csv


def control():
    "Función que se encarga de controlar el termostato, abre el csv de las matrices y llama a ecuaciones bellman para calcular costes"
    temperaturas = (16.0, 16.5, 17.0, 17.5, 18.0, 18.5, 19.0, 19.5, 20.0, 20.5, 21.0, 21.5, 22.0, 22.5, 23.0, 23.5, 24.0, 24.5, 25.0)
    inputs = open_data("inputs.csv")
    tolerancia = float(inputs[2][1])
    tiempo = 0
    horas = 0
    calefaccion_tiempo = 1800
    iteracion = 0
    aux = random.choice(temperaturas)
    # llama a ecuaciones de bellman para calcular los costes y la politica óptima
    diccionario = ecuaciones_bellman()
    temperatura_objetivo = inputs[3][1]

    # un bucle hasta que se llega a la temperatura deseada
    while aux != temperatura_objetivo:

        if aux == 22.0:
            print("Temperatura objetivo: ", aux, " conseguida. Grado de tolerancia:", tolerancia, "Hora:", horas )
            break
        # define la politica optima del estado actual
        if diccionario[str(aux)] == "Apagar":
            calefaccion = False
        if diccionario[str(aux)] == "Encender":
            calefaccion = True

        num = random.random()
        if calefaccion == True:
            if aux == 16:
                if num < 0.3:
                    aux = aux
                elif num < 0.8:
                    aux += 0.5
                else:
                    aux += 1
            elif aux == 24.5:
                if num < 0.1:
                    aux -= 0.5
                elif num < 0.3:
                    aux = aux
                else:
                    aux += 0.5
            elif aux == 25:
                if num < 0.1:
                    aux -= 0.5
                else:
                    aux = aux
            else:
                if num < 0.1:
                    aux -= 0.5
                elif num < 0.3:
                    aux = aux
                elif num < 0.8:
                    aux += 0.5
                else:
                    aux += 1

        if calefaccion == False:
            if aux == 16:
                if num < 0.9:
                    aux = aux
                else:
                    aux += 0.5

            elif aux == 25:
                if num < 0.7:
                    aux -= 0.5
                else:
                    aux = aux
            else:
                if num < 0.7:
                    aux -= 0.5
                elif num < 0.9:
                    aux = aux
                else:
                    aux += 0.5
        iteracion += 1
        tiempo += calefaccion_tiempo
        horas = tiempo/3600


def ecuaciones_bellman():
    """
    Se presupone con la iteración 0 ya esta hecha, por tanto los valores de los estados sera el coste de acción más bajo
    Se encarga de buscar los valores de los estados, en funcion del numero máximo de iteraciones y el grado de tolerancia
    """

    matriz = open_data("archivo.csv")
    costes = open_data("costes.csv")
    inputs = open_data("inputs.csv")
    coste_e = int(costes[1][1])
    coste_a = int(costes[2][1])
    tolerancia = float(inputs[2][1])
    iteracion_max = int(inputs[1][1])
    # elige el coste minimo para la primera iteración de los valores
    if coste_a < coste_e:
        costemin = coste_a
    else:
        costemin = coste_e

    V22 = 0
    V16 = V165 = V17 = V175 = V18 = V185 = V19 = V195 = V20 = V205 = V21 = V215 = V225 = V23 = V235 = V24 = V245 = V25 = costemin

    iteracion = 1
    aux = 0
    aux2 = 0

    while (V16 - aux > tolerancia and V25 - aux2 > tolerancia  and iteracion < iteracion_max):

        aux = V16
        aux2 = V25

        V16_new = min( coste_e + float(matriz[1][1]) * V16 + float(matriz[1][2]) * V165 + float(matriz[1][3]) * V17,
                       coste_a + float(matriz[2][1]) * V16 + float(matriz[2][2]) * V165 + float(matriz[2][3]) * V17)

        V165_new = min( coste_e + float(matriz[3][1]) * V16 + float(matriz[3][2]) * V165 + float(matriz[3][3]) * V17 + float(matriz[3][4]) * V175,
                        coste_a + float(matriz[4][1]) * V16 + float(matriz[4][2]) * V165 + float(matriz[4][3]) * V17)

        V17_new = min( coste_e + float(matriz[5][2]) * V165 + float(matriz[5][3]) * V17 + float(matriz[5][4]) * V175 + float(matriz[5][5]) * V18,
                       coste_a + float(matriz[6][2]) * V165 + float(matriz[6][3]) * V17 + float(matriz[6][4]) * V175)

        V175_new = min( coste_e + float(matriz[7][3]) * V17 + float(matriz[7][4]) * V175 + float(matriz[7][5]) * V18 + float(matriz[7][6]) * V185,
                        coste_a + float(matriz[8][3]) * V17 + float(matriz[8][4]) * V175 + float(matriz[8][5]) * V18)

        V18_new = min( coste_e + float(matriz[9][4]) * V175 + float(matriz[9][5]) * V18 + float(matriz[9][6]) * V185 + float(matriz[9][7]) * V19,
                       coste_a + float(matriz[10][4]) * V175 + float(matriz[10][5]) * V18 + float(matriz[10][6]) * V185)

        V185_new = min( coste_e + float(matriz[11][5]) * V18 + float(matriz[11][6])* V185 + float(matriz[11][7]) * V19 + float(matriz[11][8]) * V195,
                        coste_a + float(matriz[12][5]) * V18 + float(matriz[12][6]) * V185 + float(matriz[12][7]) * V19)

        V19_new = min( coste_e + float(matriz[13][6]) * V185 + float(matriz[13][7]) * V19 + float(matriz[13][8]) * V195 + float(matriz[13][9]) * V20,
                       coste_a + float(matriz[14][6]) * V185 + float(matriz[14][7]) * V19 + float(matriz[14][8]) * V195)

        V195_new = min( coste_e + float(matriz[15][7]) * V19 + float(matriz[15][8]) * V195 + float(matriz[15][9]) * V20 + float(matriz[15][10]) * V205,
                        coste_a + float(matriz[16][7]) * V19 + float(matriz[16][8]) * V195 + float(matriz[16][9]) * V20)

        V20_new = min( coste_e + float(matriz[17][8]) * V195 + float(matriz[17][9]) * V20 + float(matriz[17][10]) * V205 + float(matriz[17][11]) * V21,
                       coste_a + float(matriz[18][8]) * V195 + float(matriz[18][9]) * V20 + float(matriz[18][10]) * V205)

        V205_new = min( coste_e + float(matriz[19][9]) * V20 + float(matriz[19][10]) * V205 + float(matriz[19][11]) * V21 + float(matriz[19][12]) * V215,
                        coste_a + float(matriz[20][9]) * V20 + float(matriz[20][10]) * V205 + float(matriz[20][11]) * V21)

        V21_new = min( coste_e + float(matriz[21][10]) * V205 + float(matriz[21][11]) * V21 + float(matriz[21][12]) * V215 + float(matriz[21][13]) * V22,
                       coste_a + float(matriz[22][10]) * V205 + float(matriz[22][11]) * V21 + float(matriz[22][12]) * V215)

        V215_new = min( coste_e + float(matriz[23][11]) * V21 + float(matriz[23][12]) * V215 + float(matriz[23][13]) * V22 + float(matriz[23][14]) * V225,
                        coste_a + float(matriz[24][11]) * V21 + float(matriz[24][12]) * V215 + float(matriz[24][13]) * V22)

        V225_new = min( coste_e + float(matriz[27][13]) * V22 + float(matriz[27][14]) * V225 + float(matriz[27][15]) * V23 + float(matriz[27][16]) * V235,
                        coste_a + float(matriz[28][13]) * V22 + float(matriz[28][14]) * V225 + float(matriz[28][15]) * V23)

        V23_new = min( coste_e + float(matriz[29][14]) * V225 + float(matriz[29][15]) * V23 + float(matriz[29][16]) * V235 + float(matriz[29][17]) * V24,
                       coste_a + float(matriz[30][14]) * V225 + float(matriz[30][15]) * V23 + float(matriz[30][16]) * V235)

        V235_new = min( coste_e + float(matriz[31][15]) * V23 + float(matriz[31][16]) * V235 + float(matriz[31][17]) * V24 + float(matriz[31][18]) * V245,
                        coste_a + float(matriz[32][15]) * V23 + float(matriz[32][16]) * V235 + float(matriz[32][17]) * V24)

        V24_new = min( coste_e + float(matriz[33][16]) * V235 + float(matriz[33][17]) * V24 + float(matriz[33][18]) * V245 + float(matriz[33][19]) * V25,
                       coste_a + float(matriz[34][16]) * V235 + float(matriz[34][17]) * V24 + float(matriz[34][18]) * V245)

        V245_new = min( coste_e + float(matriz[35][19]) * V25 + float(matriz[35][18]) * V245 + float(matriz[35][17]) * V24,
                        coste_a + float(matriz[36][19]) * V25 + float(matriz[36][18]) * V245 + float(matriz[36][17]) * V24)

        V25_new = min( coste_e + float(matriz[37][19]) * V25 + float(matriz[37][18]) * V245,
                       coste_a + float(matriz[38][19]) * V25 + float(matriz[38][18]) * V245)


        V16 = V16_new ; V165 = V165_new ; V17 = V17_new ; V175 = V175_new ; V18 = V18_new ; V185 = V185_new ; V19 = V19_new
        V195 = V195_new ; V20 = V20_new ; V205 = V205_new ; V21 = V21_new ; V215 = V215_new ;  V225 = V225_new ; V23 = V23_new ; V235 =V235_new
        V24 = V24_new ;  V245 = V245_new ; V25 = V25_new

        iteracion += 1

    valores = {"16.0": V16, "16.5" : V165, "17.0": V17, "17.5" : V175, "18.0": V18, "18.5": V185, "19.0" : V19, "19.5": V195, "20.0": V20,
                "20.5": V205, "21.0": V21, "21.5" : V215, "22.0": V22, "22.5": V225, "23.0" : V23, "23.5": V235, "24.0": V24, "24.5" : V245, "25.0" : V25}

    dict_to_csv(valores, "Output/valores.csv")
    print_csv("Output/valores.csv")

    return politica_optima(coste_a, coste_e, valores, matriz)


def politica_optima(coste_a, coste_e, valores, matriz):
    "Calcula la politica optima para los estados en funcion de los valores obtenidos"

    diccionario = {"16.0": None, "16.5": None, "17.0": None, "17.5": None, "18.0": None, "18.5": None, "19.0": None,
                   "19.5": None, "20.0": None, "20.5": None, "21.0": None, "21.5": None, "22.0": True, "22.5": None, "23.0": None,
                   "23.5": None, "24.0": None, "24.5": None, "25.0": None}

    V16e = coste_e + float(matriz[1][1]) * valores["16.0"] + float(matriz[1][2]) * valores["17.0"] + float(
        matriz[1][3]) * valores["16.5"]
    V16a = coste_a + float(matriz[2][1]) * valores["16.0"] + float(matriz[2][2]) * valores["17.0"] + float(
        matriz[2][3]) * valores["16.5"]
    if V16e < V16a:
        diccionario["16.0"] = "Encender"
    else:
        diccionario["16.0"] = "Apagar"

    V165e = coste_e + float(matriz[3][1]) * valores["16.0"] + float(matriz[3][2]) * valores["16.5"] + float(
        matriz[3][3]) * valores["17.0"] + float(matriz[3][4]) * valores["17.5"]
    V165a = coste_a + float(matriz[4][1]) * valores["16.0"] + float(matriz[4][2]) * valores["16.5"] + float(
        matriz[4][3]) * valores["17.0"]
    if V165e < V165a:
        diccionario["16.5"] = "Encender"
    else:
        diccionario["16.5"] = "Apagar"

    V17e = coste_e + float(matriz[5][2]) * valores["16.5"] + float(matriz[5][3]) * valores["17.0"] + float(
        matriz[5][4]) * valores["17.5"] + float(matriz[5][5]) * valores["18.0"]
    V17a = coste_a + float(matriz[6][2]) * valores["16.5"] + float(matriz[6][3]) * valores["17.0"] + float(
        matriz[6][3]) * valores["17.5"]
    if V17e < V17a:
        diccionario["17.0"] = "Encender"
    else:
        diccionario["17.0"] = "Apagar"

    V175e = coste_e + float(matriz[7][3]) * valores["17.0"] + float(matriz[7][4]) * valores["17.5"] + float(
        matriz[7][5]) * valores["18.0"] + float(matriz[7][6]) * valores["18.5"]
    V175a = coste_a + float(matriz[8][3]) * valores["17.0"] + float(matriz[8][4]) * valores["17.5"] + float(
        matriz[8][5]) * valores["18.0"]
    if V175e < V175a:
        diccionario["17.5"] = "Encender"
    else:
        diccionario["17.5"] = "Apagar"

    V18e = coste_e + float(matriz[9][4]) * valores["17.5"] + float(matriz[9][5]) * valores["18.0"] + float(
        matriz[9][6]) * valores["18.5"] + float(matriz[9][7]) * valores["19.0"]
    V18a = coste_a + float(matriz[10][4]) * valores["17.5"] + float(matriz[10][5]) * valores["18.0"] + float(
        matriz[10][6]) * valores["18.5"]
    if V18e < V18a:
        diccionario["18.0"] = "Encender"
    else:
        diccionario["18.0"] = "Apagar"

    V185e = coste_e + float(matriz[11][5]) * valores["18.0"] + float(matriz[11][6]) * valores["18.5"] + float(
        matriz[11][7]) * valores["19.0"] + float(matriz[11][8]) * valores["19.5"]
    V185a = coste_a + float(matriz[12][5]) * valores["18.0"] + float(matriz[12][6]) * valores["18.5"] + float(
        matriz[12][7]) * valores["19.0"]
    if V185e < V185a:
        diccionario["18.5"] = "Encender"
    else:
        diccionario["18.5"] = "Apagar"

    V19e = coste_e + float(matriz[13][6]) * valores["18.5"] + float(matriz[13][7]) * valores["19.0"] + float(
        matriz[13][8]) * valores["19.5"] + float(matriz[13][9]) * valores["20.0"]
    V19a = coste_a + float(matriz[14][6]) * valores["18.5"] + float(matriz[14][7]) * valores["19.0"] + float(
        matriz[14][8]) * valores["19.5"]
    if V19e < V19a:
        diccionario["19.0"] = "Encender"
    else:
        diccionario["19.0"] = "Apagar"

    V195e = coste_e + float(matriz[15][7]) * valores["19.0"] + float(matriz[15][8]) * valores["19.5"] + float(
        matriz[15][9]) * valores["20.0"] + float(matriz[15][10]) * valores["20.5"]
    V195a = coste_a + float(matriz[16][7]) * valores["19.0"] + float(matriz[16][8]) * valores["19.5"] + float(
        matriz[16][9]) * valores["20.0"]
    if V195e < V195a:
        diccionario["19.5"] = "Encender"
    else:
        diccionario["19.5"] = "Apagar"

    V20e = coste_e + float(matriz[17][8]) * valores["19.5"] + float(matriz[17][9]) * valores["20.0"] + float(
        matriz[17][10]) * valores["20.5"] + float(matriz[17][11]) * valores["21.0"]
    V20a = coste_a + float(matriz[18][8]) * valores["19.5"] + float(matriz[18][9]) * valores["20.0"] + float(
        matriz[18][10]) * valores["20.5"]
    if V20e < V20a:
        diccionario["20.0"] = "Encender"
    else:
        diccionario["20.0"] = "Apagar"

    V205e = coste_e + float(matriz[19][9]) * valores["20.0"] + float(matriz[19][10]) * valores["20.5"] +\
            float(matriz[19][11]) * valores["21.0"] + float(matriz[19][12]) * valores["21.5"]
    V205a = coste_a + float(matriz[20][9]) * valores["20.0"] + float(matriz[20][10]) * valores["20.5"] + float(matriz[20][11]) * valores["21.0"]
    if V205e < V205a:
        diccionario["20.5"] = "Encender"
    else:
        diccionario["20.5"] = "Apagar"

    V21e = coste_e + float(matriz[21][10]) * valores["20.5"] + float(matriz[21][11]) * valores["21.0"] +\
           float(matriz[21][12]) * valores["21.5"] + float(matriz[21][13]) * valores["22.0"]
    V21a = coste_a + float(matriz[22][10]) * valores["20.5"] + float(matriz[22][11])* valores["21.0"] + float(matriz[22][12]) * valores["21.5"]
    if V21e < V21a:
        diccionario["21.0"] = "Encender"
    else:
        diccionario["21.0"] = "Apagar"

    V215e = coste_e + float(matriz[23][11]) * valores["21.0"] + float(matriz[23][12]) * valores["21.5"] +\
            float(matriz[23][13]) * valores["22.0"] + float(matriz[23][14]) * valores["22.5"]
    V215a = coste_a + float(matriz[24][11]) * valores["21.0"] + float(matriz[24][12]) * valores["21.5"] + float(matriz[24][13]) * valores["22.0"]
    if V215e < V215a:
        diccionario["21.5"] = "Encender"
    else:
        diccionario["21.5"] = "Apagar"

    V225e = coste_e + float(matriz[27][13]) * valores["22.0"] + float(matriz[27][14]) * valores["22.5"] +\
            float(matriz[27][15]) * valores["23.0"] + float(matriz[27][16]) * valores["23.5"]
    V225a = coste_a + float(matriz[28][13]) * valores["22.0"] + float(matriz[28][14]) * valores["22.5"] + float(matriz[28][15]) * valores["23.0"]
    if V225e < V225a:
        diccionario["22.5"] = "Encender"
    else:
        diccionario["22.5"] = "Apagar"

    V23e = coste_e + float(matriz[29][14]) * valores["22.5"] + float(matriz[29][15]) * valores["23.0"] +\
           float(matriz[29][16]) * valores["23.5"] + float(matriz[29][17]) * valores["24.0"]
    V23a = coste_a + float(matriz[30][14]) * valores["22.5"] + float(matriz[30][15]) * valores["23.0"] + float(matriz[30][16]) * valores["23.5"]
    if V23e < V23a:
        diccionario["23.0"] = "Encender"
    else:
        diccionario["23.0"] = "Apagar"

    V235e = coste_e + float(matriz[31][15]) * valores["23.0"] + float(matriz[31][16]) * valores["23.5"]\
            + float(matriz[31][17]) * valores["24.0"] + float(matriz[31][18]) * valores["24.5"]
    V235a = coste_a + float(matriz[32][15]) * valores["23.0"] + float(matriz[32][16]) * valores["23.5"] + float(matriz[32][17]) * valores["24.0"]
    if V235e < V235a:
        diccionario["23.5"] = "Encender"
    else:
        diccionario["23.5"] = "Apagar"

    V24e = coste_e + float(matriz[33][16]) * valores["23.5"] + float(matriz[33][17]) * valores["24.0"]\
           + float(matriz[33][18]) * valores["24.5"] + float(matriz[33][19]) * valores["25.0"]
    V24a = coste_a + float(matriz[34][16]) * valores["23.5"] + float(matriz[34][17]) * valores["24.0"] + float(matriz[34][18]) * valores["24.5"]
    if V24e < V24a:
        diccionario["24.0"] = "Encender"
    else:
        diccionario["24.0"] = "Apagar"

    V245e = coste_e + float(matriz[35][19]) * valores["25.0"] + float(matriz[35][18]) * valores["24.5"] + float(matriz[35][17]) * valores["24.0"]
    V245a = coste_a + float(matriz[36][19]) * valores["25.0"] + float(matriz[36][18]) * valores["24.5"] + float(matriz[36][17]) * valores["24.0"]
    if V245e < V245a:
        diccionario["24.5"] = "Encender"
    else:
        diccionario["24.5"] = "Apagar"

    V25e = coste_e + float(matriz[37][19]) * valores["25.0"] + float(matriz[37][18]) * valores["24.5"]
    V25a = coste_a + float(matriz[38][19]) * valores["25.0"] + float(matriz[38][18]) * valores["24.5"]

    if V25e < V25a:
        diccionario["25.0"] = "Encender"
    else:
        diccionario["25.0"] = "Apagar"

    dict_to_csv(diccionario, "Output/politica_optima.csv")
    print_csv("Output/politica_optima.csv")
    return diccionario

def open_data(inputfile):
    "Función que abre un archivo csv"
    matriz = []
    with open(inputfile, newline='') as archivo_csv:
        lector_csv = csv.reader(archivo_csv, delimiter=',')
        for fila in lector_csv:
            matriz.append(fila)
    return matriz

def dict_to_csv(dictionary, filename):
    "Función que transforma un diccionario en csv"
    keys = dictionary.keys()
    values = dictionary.values()

    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(keys)
        writer.writerow(values)

    return filename

def print_csv(filename):
    "Función que imprime un csv"
    with open(filename, 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            print(', '.join(row))

if __name__ == "__main__":
    control()