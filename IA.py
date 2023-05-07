import random

import csv

matriz = []

with open('archivo.csv', newline='') as archivo_csv:
    lector_csv = csv.reader(archivo_csv, delimiter=',')
    for fila in lector_csv:
        matriz.append(fila)


print("matriz",matriz)
print( "fila 0",matriz[1][0])


def control():
    temperaturas = (16.0, 16.5, 17.0, 17.5, 18.0, 18.5, 19.0, 19.5, 20.0, 20.5, 21.0, 21.5, 22.0, 22.5, 23.0, 23.5, 24.0, 24.5, 25.0)
    calefaccion = False
    tiempo = 0
    calefaccion_tiempo = 1800
    aux = random.choice(temperaturas)
    iteracion = 0
    diccionario = ecuaciones_bellman()

    while aux != 22:

        if calefaccion == True:
            if aux == 16:
                if random.random() < 0.3:
                    aux = aux
                elif random.random() < 0.8:
                    aux += 0.5
                else:
                    aux += 1
            elif aux == 24.5:
                if random.random() < 0.1:
                    aux -= 0.5
                elif random.random() < 0.3:
                    aux = aux
                else:
                    aux += 0.5
            elif aux == 25:
                if random.random() < 0.1:
                    aux -= 0.5
                else:
                    aux = aux
            else:
                if random.random() < 0.1:
                    aux -= 0.5
                elif random.random() < 0.3:
                    aux = aux
                elif random.random() < 0.8:
                    aux += 0.5
                else:
                    aux += 1

        if calefaccion == False:
            if aux == 16:
                if random.random() < 0.9:
                    aux = aux
                else:
                    aux += 0.5

            elif aux == 25:
                if random.random() < 0.7:
                    aux -= 0.5
                else:
                    aux = aux
            else:
                if random.random() < 0.7:
                    aux -= 0.5
                elif random.random() < 0.9:
                    aux = aux
                else:
                    aux += 0.5
        iteracion += 1
        tiempo += calefaccion_tiempo
        horas = tiempo/3600

        print("Temperatura:", aux, "Hora:", horas, "Iteración:", iteracion )
        "dependiendo del aux hay que sacar su politica optima"

        if aux == 22.0:
            break

        if diccionario[str(aux)] == False:
            calefaccion = False

        if diccionario[str(aux)] == True:
            calefaccion = True

def ecuaciones_bellman():
    "Se presupone con la iteración 0 ya esta hecha, por tanto los valores de los estados sera el coste más bajo"

    coste_e = 2
    coste_a = 1

    if coste_a < coste_e:
        costemin = coste_a
    else:
        costemin = coste_e
    V22 = 0
    V16 = V165 = V17 = V175 = V18 = V185 = V19 = V195 = V20 = V205 = V21 = V215 = V225 = V23 = V235 = V24 = V245 = V25 = costemin

    # Probabilidades A (t entre 16,5 y 24)

    Pet_A = 0.1
    Petminus5_A = 0.2
    Petplus5_A = 0.5
    Petplus1_A = 0.2

    Pat_A = 0.2
    Patminus5_A = 0.7
    Patplus5_A = 0.1
    Patplus1_A = 0

    #Probabilidades B(t=16)

    Pe16_16 = 0.3
    Pe165_16 = 0.5
    Pe17_16 = 0.2

    Pa16_16 = 0.9
    Pa165_16 = 0.1
    Pa17_16 = 0


    # Probabilidades C(t=24.5)

    Pe24_245 = 0.1
    Pe245_245 = 0.2
    Pe25_245 = 0.7

    Pa24_245 = Patminus5_A
    Pa245_245 = Pat_A
    Pa25_245 = Patplus5_A

    # Probabilidades D(t=25)

    Pe245_25 = 0.1
    Pe25_25 = 0.9

    Pa245_25 = 0.7
    Pa25_25 = 0.3


    iteracion = 1
    aux = 0


    while (V16 - aux > 0.00001 and iteracion < 10000):

        aux = V16
        print("Iteración:", iteracion)
        V16_new = min( coste_e + float(matriz[1][1]) * V16 + float(matriz[1][2]) * V165 + float(matriz[1][3]) * V17,
                       coste_a + float(matriz[2][1]) * V16 + float(matriz[2][2]) * V165 + float(matriz[2][3]) * V17)
        print("V16", V16_new)

        V165_new = min( coste_e + float(matriz[3][1]) * V16 + float(matriz[3][2]) * V165 + float(matriz[3][3]) * V17 + float(matriz[3][4]) * V175,
                        coste_a + float(matriz[4][1]) * V16 + float(matriz[4][2]) * V165 + float(matriz[4][3]) * V17)
        print("V165", V165_new)

        V17_new = min( coste_e + float(matriz[5][2]) * V165 + float(matriz[5][3]) * V17 + float(matriz[5][4]) * V175 + float(matriz[5][5]) * V18,
                       coste_a + float(matriz[6][2]) * V165 + float(matriz[6][3]) * V17 + float(matriz[6][4]) * V175)
        print("V17", V17_new)

        V175_new = min( coste_e + float(matriz[7][3]) * V17 + float(matriz[7][4]) * V175 + float(matriz[7][5]) * V18 + float(matriz[7][6]) * V185,
                        coste_a + float(matriz[8][3]) * V17 + float(matriz[8][4]) * V175 + float(matriz[8][5]) * V18)
        print("V175", V175_new)

        V18_new = min( coste_e + float(matriz[9][4]) * V175 + float(matriz[9][5]) * V18 + float(matriz[9][6]) * V185 + float(matriz[9][7]) * V19,
                       coste_a + float(matriz[10][4]) * V175 + float(matriz[10][5]) * V18 + float(matriz[10][6]) * V185)
        print("V18", V18_new)

        V185_new = min( coste_e + float(matriz[11][5]) * V18 + float(matriz[11][6])* V185 + float(matriz[11][7]) * V19 + float(matriz[11][8]) * V195,
                        coste_a + float(matriz[12][5]) * V18 + float(matriz[12][6]) * V185 + float(matriz[12][7]) * V19)
        print("V185", V185_new)

        V19_new = min( coste_e + float(matriz[13][6]) * V185 + float(matriz[13][7]) * V19 + float(matriz[13][8]) * V195 + float(matriz[13][9]) * V20,
                       coste_a + float(matriz[14][6]) * V185 + float(matriz[14][7]) * V19 + float(matriz[14][8]) * V195)
        print("V19", V19_new)

        V195_new = min( coste_e + float(matriz[15][8]) * V19 + float(matriz[15][9]) * V195 + float(matriz[15][10]) * V20 + float(matriz[15][11]) * V205,
                        coste_a + float(matriz[16][8]) * V19 + float(matriz[16][9]) * V195 + float(matriz[16][10]) * V20)
        print("V195", V195_new)

        V20_new = min( coste_e + float(matriz[17][9]) * V195 + float(matriz[17][10]) * V20 + float(matriz[17][10]) * V205 + float(matriz[17][11]) * V21,
                       coste_a + float(matriz[18][9]) * V195 + float(matriz[18][10]) * V20 + float(matriz[18][10]) * V205)
        print("V20", V20_new)

        V205_new = min( coste_e + float(matriz[19][9]) * V20 + float(matriz[19][10]) * V205 + float(matriz[19][11]) * V21 + float(matriz[19][12]) * V215,
                        coste_a + float(matriz[20][9]) * V20 + float(matriz[20][10]) * V205 + float(matriz[20][11]) * V21)
        print("V205", V205_new)

        V21_new = min( coste_e + float(matriz[21][10]) * V205 + float(matriz[21][11]) * V21 + float(matriz[21][12]) * V215 + float(matriz[21][13]) * V22,
                       coste_a + float(matriz[22][10]) * V205 + float(matriz[22][11]) * V21 + float(matriz[22][12]) * V215)
        print("V21", V21_new)

        V215_new = min( coste_e + float(matriz[23][11]) * V21 + float(matriz[23][12]) * V215 + float(matriz[23][13]) * V22 + float(matriz[23][14]) * V225,
                        coste_a + float(matriz[24][11]) * V21 + float(matriz[24][12]) * V215 + float(matriz[24][13]) * V22)
        print("V215", V215_new)

        V225_new = min(
            coste_e + float(matriz[27][13]) * V22 + float(matriz[27][14]) * V225 + float(matriz[27][15]) * V23 + float(matriz[27][16]) * V235,
            coste_a + float(matriz[28][13]) * V22 + float(matriz[28][14]) * V225 + float(matriz[28][15]) * V23)
        print("V225", V225_new)

        V23_new = min(
            coste_e + float(matriz[29][14]) * V225 + float(matriz[29][15]) * V23 + float(matriz[29][16]) * V235 + float(
                matriz[29][17]) * V24,
            coste_a + float(matriz[30][14]) * V225 + float(matriz[30][15]) * V23 + float(matriz[30][16]) * V235)
        print("V23", V23_new)

        V235_new = min(
            coste_e + float(matriz[31][15]) * V23 + float(matriz[31][16]) * V235 + float(matriz[31][17]) * V24 + float(
                matriz[31][18]) * V245,
            coste_a + float(matriz[32][15]) * V23 + float(matriz[32][16]) * V235 + float(matriz[32][17]) * V24)
        print("V235", V235_new)

        V24_new = min(
            coste_e + float(matriz[33][16]) * V235 + float(matriz[33][17]) * V24 + float(matriz[33][18]) * V245 + float(
                matriz[33][19]) * V25,
            coste_a + float(matriz[34][16]) * V235 + float(matriz[34][17]) * V24 + float(matriz[34][18]) * V245)
        print("V24", V24_new)

        V245_new = min(
            coste_e + float(matriz[35][19]) * V25 + float(matriz[35][18]) * V245 + float(matriz[35][17]) * V24,
            coste_a + float(matriz[36][19]) * V25 + float(matriz[36][18]) * V245 + float(matriz[36][17]) * V24)
        print("V245", V245_new)

        V25_new = min(coste_e + float(matriz[37][19]) * V25 + float(matriz[37][18]) * V245,
                      coste_a + float(matriz[38][19]) * V25 + float(matriz[38][18]) * V245)
        print("V25", V25_new)


        V16 = V16_new
        V165 = V165_new
        V17 = V17_new
        V175 = V17_new
        V18 = V18_new
        V185 = V185_new
        V19 = V19_new
        V195 = V195_new
        V205 = V205_new
        V21 = V215_new
        V215 = V215_new
        V225 = V225_new
        V23 = V23_new
        V235 =V235_new
        V24 = V24_new
        V245 = V245_new
        V25 = V25_new

        iteracion += 1
        print("iteracion valores",iteracion)
    valores = {"16.0": V16, "16.5" : V165, "17.0": V17, "17.5" : V175, "18.0": V18, "18.5": V185, "19.0" : V19, "19.5": V195, "20.0": V20,
                "20.5": V205, "21.0": V21, "21.5" : V215, "22.0": 0, "22.5": V225, "23.0" : V23, "23.5": V235, "24.0": V24, "24.5" : V245, "25.0" : V25}

    return politica_optima(Pa165_16, Pa16_16, Pa17_16, Pa245_245, Pa245_25, Pa24_245, Pa25_245, Pa25_25, Pat_A, Patminus5_A,
                       Patplus5_A, Pe165_16, Pe16_16, Pe17_16, Pe245_245, Pe245_25, Pe24_245, Pe25_245, Pe25_25, Pet_A,
                       Petminus5_A, Petplus1_A, Petplus5_A, coste_a, coste_e, valores)



def politica_optima(Pa165_16, Pa16_16, Pa17_16, Pa245_245, Pa245_25, Pa24_245, Pa25_245, Pa25_25, Pat_A, Patminus5_A,
                Patplus5_A, Pe165_16, Pe16_16, Pe17_16, Pe245_245, Pe245_25, Pe24_245, Pe25_245, Pe25_25, Pet_A,
                Petminus5_A, Petplus1_A, Petplus5_A, coste_a, coste_e, valores):

    diccionario = {"16.0": None, "16.5": None, "17.0": None, "17.5": None, "18.0": None, "18.5": None, "19.0": None,
                   "19.5": None, "20.0": None,
                   "20.5": None, "21.0": None, "21.5": None, "22.5": None, "23.0": None, "23.5": None, "24.0": None,
                   "24.5": None, "25.0": None}

    V16e = coste_e + Pe16_16 * valores["16.0"] + Pe17_16 * valores["17.0"] + Pe165_16 * valores["16.5"]
    V16a = coste_a + Pa16_16 * valores["16.0"] + Pa17_16 * valores["17.0"] + Pa165_16 * valores["16.5"]
    if V16e < V16a:
        diccionario["16.0"] = True
    else:
        diccionario["16.0"] = False

    V165e = coste_e + Petminus5_A * valores["16.0"] + Pet_A * valores["16.5"] + Petplus5_A * valores["17.0"] + Petplus1_A * valores["17.5"]
    V165a = coste_a + Patminus5_A * valores["16.0"] + Pat_A * valores["16.5"] + Patplus5_A * valores["17.0"]
    if V165e < V165a:
        diccionario["16.5"] = True
    else:
        diccionario["16.5"] = False

    V17e = coste_e + Petminus5_A * valores["16.5"] + Pet_A * valores["17.0"] + Petplus5_A * valores["17.5"] + Petplus1_A * valores["18.0"]
    V17a = coste_a + Patminus5_A * valores["16.5"] + Pat_A * valores["17.0"] + Patplus5_A * valores["17.5"]
    if V17e < V17a:
        diccionario["17.0"] = True
    else:
        diccionario["17.0"] = False

    V175e = coste_e + Petminus5_A * valores["17.0"] + Pet_A * valores["17.5"] + Petplus5_A * valores["18.0"] + Petplus1_A * valores["18.5"]
    V175a = coste_a + Patminus5_A * valores["17.0"] + Pat_A * valores["17.5"] + Patplus5_A * valores["18.0"]
    if V175e < V175a:
        diccionario["17.5"] = True
    else:
        diccionario["17.5"] = False

    V18e = coste_e + Petminus5_A * valores["17.5"] + Pet_A * valores["18.0"] + Petplus5_A * valores["18.5"] + Petplus1_A * valores["19.0"]
    V18a = coste_a + Patminus5_A * valores["17.5"] + Pat_A * valores["18.0"] + Patplus5_A * valores["18.5"]
    if V18e < V18a:
        diccionario["18.0"] = True
    else:
        diccionario["18.0"] = False

    V185e = coste_e + Petminus5_A * valores["18.0"] + Pet_A * valores["18.5"] + Petplus5_A * valores["19.0"] + Petplus1_A * valores["19.5"]
    V185a = coste_a + Patminus5_A * valores["18.0"] + Pat_A * valores["18.5"] + Patplus5_A * valores["19.0"]
    if V185e < V185a:
        diccionario["18.5"] = True
    else:
        diccionario["18.5"] = False

    V19e = coste_e + Petminus5_A * valores["18.5"] + Pet_A * valores["19.0"] + Petplus5_A * valores["19.5"] + Petplus1_A * valores["20.0"]
    V19a = coste_a + Patminus5_A * valores["18.5"] + Pat_A * valores["19.0"] + Patplus5_A * valores["19.5"]
    if V19e < V19a:
        diccionario["19.0"] = True
    else:
        diccionario["19.0"] = False

    V195e = coste_e + Petminus5_A * valores["19.0"] + Pet_A * valores["19.5"] + Petplus5_A * valores["20.0"] + Petplus1_A * valores["20.5"]
    V195a = coste_a + Patminus5_A * valores["19.0"] + Pat_A * valores["19.5"] + Patplus5_A * valores["20.0"]
    if V195e < V195a:
        diccionario["19.5"] = True
    else:
        diccionario["19.5"] = False

    V20e = coste_e + Petminus5_A * valores["19.5"] + Pet_A * valores["20.0"] + Petplus5_A * valores["20.5"] + Petplus1_A * valores["21.0"]
    V20a = coste_a + Patminus5_A * valores["19.5"] + Pat_A * valores["20.0"] + Patplus5_A * valores["20.5"]
    if V20e < V20a:
        diccionario["20.0"] = True
    else:
        diccionario["20.0"] = False

    V205e = coste_e + Petminus5_A * valores["20.0"] + Pet_A * valores["20.5"] + Petplus5_A * valores["21.0"] + Petplus1_A * valores["21.5"]
    V205a = coste_a + Patminus5_A * valores["20.0"] + Pat_A * valores["20.5"] + Patplus5_A * valores["21.0"]
    if V205e < V205a:
        diccionario["20.5"] = True
    else:
        diccionario["20.5"] = False

    V21e = coste_e + Petminus5_A * valores["20.5"] + Pet_A * valores["21.0"] + Petplus5_A * valores["21.5"] + Petplus1_A * valores["22.0"]
    V21a = coste_a + Patminus5_A * valores["20.5"] + Pat_A * valores["21.0"] + Patplus5_A * valores["21.5"]
    if V21e < V21a:
        diccionario["21.0"] = True
    else:
        diccionario["21.0"] = False

    V215e = coste_e + Petminus5_A * valores["21.0"] + Pet_A * valores["21.5"] + Petplus5_A * valores["22.0"] + Petplus1_A * valores["22.5"]
    V215a = coste_a + Patminus5_A * valores["21.0"] + Pat_A * valores["21.5"] + Patplus5_A * valores["22.0"]
    if V215e < V215a:
        diccionario["21.5"] = True
    else:
        diccionario["21.5"] = False

    V225e = coste_e + Petminus5_A * valores["22.0"] + Pet_A * valores["22.5"] + Petplus5_A * valores["23.0"] + Petplus1_A * valores["23.5"]
    V225a = coste_a + Patminus5_A * valores["22.0"] + Pat_A * valores["22.5"] + Patplus5_A * valores["23.0"]
    if V225e < V225a:
        diccionario["22.5"] = True
    else:
        diccionario["22.5"] = True

    V23e = coste_e + Petminus5_A * valores["22.5"] + Pet_A * valores["23.0"] + Petplus5_A * valores["23.5"] + Petplus1_A * valores["24.0"]
    V23a = coste_a + Patminus5_A * valores["22.5"] + Pat_A * valores["23.0"] + Patplus5_A * valores["23.5"]
    if V23e < V23a:
        diccionario["23.0"] = True
    else:
        diccionario["23.0"] = False

    V235e = coste_e + Petminus5_A * valores["23.0"] + Pet_A * valores["23.5"] + Petplus5_A * valores["24.0"] + Petplus1_A * valores["24.5"]
    V235a = coste_a + Patminus5_A * valores["23.0"] + Pat_A * valores["23.5"] + Patplus5_A * valores["24.0"]
    if V235e < V235a:
        diccionario["23.5"] = True
    else:
        diccionario["23.5"] = False

    V24e = coste_e + Petminus5_A * valores["23.5"] + Pet_A * valores["24.0"] + Petplus5_A * valores["24.5"] + Petplus1_A * valores["25.0"]
    V24a = coste_a + Patminus5_A * valores["23.5"] + Pat_A * valores["24.0"] + Patplus5_A * valores["24.5"]
    if V24e < V24a:
        diccionario["24.0"] = True
    else:
        diccionario["24.0"] = False

    V245e = coste_e + Pe25_245 * valores["25.0"] + Pe245_245 * valores["24.5"] + Pe24_245 * valores["24.0"]
    V245a = coste_a + Pa25_245 * valores["25.0"] + Pa245_245 * valores["24.5"] + Pa24_245 * valores["24.0"]
    if V245e < V245a:
        diccionario["24.5"] = True
    else:
        diccionario["24.5"] = False

    V25e = coste_e + Pe25_25 * valores["25.0"] + Pe245_25 * valores["24.5"]
    V25a = coste_a + Pa25_25 * valores["25.0"] + Pa245_25 * valores["24.5"]
    if V25e < V25a:
        diccionario["25.0"] = True
    else:
        diccionario["25.0"] = False
    print(diccionario)
    return diccionario


if __name__ == "__main__":
    control()
