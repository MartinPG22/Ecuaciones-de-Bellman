import random


def control():
    temperaturas = (16.0, 16.5, 17.0, 17.5, 18.0, 18.5, 19.0, 19.5, 20.0, 20.5, 21.0, 21.5, 22.0, 22.5, 23.0, 23.5, 24.0, 24.5, 25.0)
    calefaccion = False
    tiempo = 0
    calefaccion_tiempo = 1800
    aux = random.choice(temperaturas)
    iteracion = 0
    diccionario = politica_optima()

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

def politica_optima():
    "Se presupone con la iteración 0 ya esta hecha, por tanto los valores de los estados sera el coste más bajo"

    coste_e = 2
    coste_a = 1
    V22 = 0
    if coste_a < coste_e:
        costemin = coste_a
    else:
        costemin = coste_e
    V16 = V165 = V17 = V175 = V18 = V185 = V19 = V195 = V20 = V205 = V21 = V215 = V225 = V23 = V235 = V24 = V245 = V25 = costemin

    # Probabilidades A (t entre 16,5 y 24)

    Pet_A = 0.1
    Petminus5_A = 0.1
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

    Pa16_16 = 0.3
    Pa165_16 = 0.5
    Pa17_16 = 0.2


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

    while V16 - aux > 0.00001 and iteracion < 10000:

        aux = V16
        print("Iteración:", iteracion)
        V16_new = min( coste_e + Pe16_16 * V16 + Pe165_16 * V165 + Pe17_16 * V17,
                       coste_a + Pa16_16 * V16 + Pa17_16 * V17 + Pa165_16 * V165)
        print("V16", V16_new)

        V165_new = min( coste_e + Petminus5_A * V16 + Pet_A * V165 + Petplus5_A * V17 + Petplus1_A * V175,
                        coste_a + Patminus5_A * V16 + Pat_A * V165 + Patplus5_A * V17)
        print("V165", V165_new)

        V17_new = min( coste_e + Petminus5_A * V165 + Pet_A * V17 + Petplus5_A * V175 + Petplus1_A * V18,
                       coste_a + Patminus5_A * V165 + Pat_A * V17 + Patplus5_A * V175)
        print("V17", V17_new)

        V175_new = min( coste_e + Petminus5_A * V17 + Pet_A * V175 + Petplus5_A * V18 + Petplus1_A * V185,
                        coste_a + Patminus5_A * V17 + Pat_A * V175 + Patplus5_A * V18)
        print("V175", V175_new)

        V18_new = min( coste_e + Petminus5_A * V175 + Pet_A * V18 + Petplus5_A * V185 + Petplus1_A * V19,
                       coste_a + Patminus5_A * V175 + Pat_A * V18 + Patplus5_A * V185)
        print("V18", V18_new)

        V185_new = min( coste_e + Petminus5_A * V18 + Pet_A * V185 + Petplus5_A * V19 + Petplus1_A * V195,
                        coste_a + Patminus5_A * V18 + Pat_A * V185 + Patplus5_A * V19)
        print("V185", V185_new)

        V19_new = min( coste_e + Petminus5_A * V185 + Pet_A * V19 + Petplus5_A * V195 + Petplus1_A * V20,
                       coste_a + Patminus5_A * V185 + Pat_A * V19 + Patplus5_A * V195)
        print("V19", V19_new)

        V195_new = min( coste_e + Petminus5_A * V19 + Pet_A * V195 + Petplus5_A * V20 + Petplus1_A * V205,
                        coste_a + Patminus5_A * V19 + Pat_A * V195 + Patplus5_A * V20)
        print("V195", V195_new)

        V20_new = min(coste_e + Petminus5_A * V195 + Pet_A * V20 + Petplus5_A * V205 + Petplus1_A * V21,
                       coste_a + Patminus5_A * V195 + Pat_A * V20 + Patplus5_A * V205)
        print("V20", V20_new)

        V205_new = min( coste_e + Petminus5_A * V20 + Pet_A * V205 + Petplus5_A * V21 + Petplus1_A * V215,
                        coste_a + Patminus5_A * V20 + Pat_A * V205 + Patplus5_A * V21)
        print("V205", V205_new)

        V21_new = min( coste_e + Petminus5_A * V205 + Pet_A * V21 + Petplus5_A * V215 + Petplus1_A * V22,
                       coste_a + Patminus5_A * V205 + Pat_A * V21 + Patplus5_A * V215)
        print("V21", V21_new)

        V215_new = min( coste_e + Petminus5_A * V21 + Pet_A * V215 + Petplus5_A * V22 + Petplus1_A * V225,
                        coste_a + Patminus5_A * V21 + Pat_A * V215 + Patplus5_A * V22)
        print("V215", V215_new)

        V225_new = min( coste_e + Petminus5_A * V22 + Pet_A * V225 + Petplus5_A * V23 + Petplus1_A * V235,
                        coste_a + Patminus5_A * V22 + Pat_A * V225 + Patplus5_A * V23)
        print("V225", V225_new)

        V23_new = min( coste_e + Petminus5_A * V225 + Pet_A * V23 + Petplus5_A * V235 + Petplus1_A * V24,
                       coste_a + Patminus5_A * V225 + Pat_A * V23 + Patplus5_A * V235)
        print("V23", V23_new)

        V235_new = min( coste_e + Petminus5_A * V23 + Pet_A * V235 + Petplus5_A * V24 + Petplus1_A * V245,
                        coste_a + Patminus5_A * V23 + Pat_A * V235 + Patplus5_A * V24)
        print("V235", V235_new)

        V24_new = min( coste_e + Petminus5_A * V235 + Pet_A * V24 + Petplus5_A * V245 + Petplus1_A * V25,
                       coste_a + Patminus5_A * V235 + Pat_A * V24 + Patplus5_A * V245)
        print("V24", V24_new)

        V245_new = min( coste_e + Pe25_245 * V25 + Pe245_245 * V245 + Pe24_245 * V24,
                        coste_a + Pa25_245 * V25 + Pa245_245 * V245 + Pa24_245 * V24)
        print("V245", V245_new)


        V25_new = min( coste_e + Pe25_25 * V25 + Pe245_25 * V245, coste_a + Pa25_25 * V25 + Pa245_25 * V245)
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

    diccionario = {"16.0": None, "16.5" : None, "17.0": None, "17.5" : None, "18.0": None, "18.5": None, "19.0" : None, "19.5": None, "20.0": None,
                   "20.5": None, "21.0": None, "21.5" : None, "22.5": None, "23.0" : None, "23.5": None, "24.0": None, "24.5" : None, "25.0" : None}
    V16e = coste_e + Pe16_16 * V16 + Pe17_16 * V17 + Pe165_16 * V165
    V16a = coste_a + Pa16_16 * V16 + Pa17_16 * V17 + Pa165_16 * V165

    if V16e < V16a:
        diccionario["16.0"] = True
    else:
        diccionario["16.0"] = False

    V165e = coste_e + Petminus5_A * V16 + Pet_A * V165 + Petplus5_A * V17 + Petplus1_A * V175
    V165a = coste_a + Patminus5_A * V16 + Pat_A * V165 + Patplus5_A * V17


    if V165e < V165a:
        diccionario["16.5"] = True
    else:
        diccionario["16.5"] = False

    V17e = coste_e + Petminus5_A * V165 + Pet_A * V17 + Petplus5_A * V175 + Petplus1_A * V18
    V17a = coste_a + Patminus5_A * V165 + Pat_A * V17 + Patplus5_A * V175


    if V17e < V17a:
        diccionario["17.0"] = True
    else:
        diccionario["17.0"] = False

    V175e = coste_e + Petminus5_A * V17 + Pet_A * V175 + Petplus5_A * V18 + Petplus1_A * V185
    V175a = coste_a + Patminus5_A * V17 + Pat_A * V175 + Patplus5_A * V18

    if V175e < V175a:
        diccionario["17.5"] = True
    else:
        diccionario["17.5"] = False

    V18e = coste_e + Petminus5_A * V175 + Pet_A * V18 + Petplus5_A * V185 + Petplus1_A * V19
    V18a = coste_a + Patminus5_A * V175 + Pat_A * V18 + Patplus5_A * V185

    if V18e < V18a:
        diccionario["18.0"] = True
    else:
        diccionario["18.0"] = False

    V185e = coste_e + Petminus5_A * V18 + Pet_A * V185 + Petplus5_A * V19 + Petplus1_A * V195
    V185a = coste_a + Patminus5_A * V18 + Pat_A * V185 + Patplus5_A * V19

    if V185e < V185a:
        diccionario["18.5"] = True
    else:
        diccionario["18.5"] = False

    V19e = coste_e + Petminus5_A * V185 + Pet_A * V19 + Petplus5_A * V195 + Petplus1_A * V20
    V19a = coste_a + Patminus5_A * V185 + Pat_A * V19 + Patplus5_A * V195

    if V19e < V19a:
        diccionario["19.0"] = True
    else:
        diccionario["19.0"] = False

    V195e = coste_e + Petminus5_A * V19 + Pet_A * V195 + Petplus5_A * V20 + Petplus1_A * V205
    V195a = coste_a + Patminus5_A * V19 + Pat_A * V195 + Patplus5_A * V20

    if V195e < V195a:
        diccionario["19.5"] = True
    else:
        diccionario["19.5"] = False

    V20e = coste_e + Petminus5_A * V195 + Pet_A * V20 + Petplus5_A * V205 + Petplus1_A * V21
    V20a = coste_a + Patminus5_A * V195 + Pat_A * V20 + Patplus5_A * V205

    if V20e < V20a:
        diccionario["20.0"] = True
    else:
        diccionario["20.0"] = False

    V205e = coste_e + Petminus5_A * V20 + Pet_A * V205 + Petplus5_A * V21 + Petplus1_A * V215
    V205a = coste_a + Patminus5_A * V20 + Pat_A * V205 + Patplus5_A * V21

    if V205e < V205a:
        diccionario["20.5"] = True
    else:
        diccionario["20.5"] = False

    V21e = coste_e + Petminus5_A * V205 + Pet_A * V21 + Petplus5_A * V215 + Petplus1_A * V22
    V21a = coste_a + Patminus5_A * V205+ Pat_A * V21 + Patplus5_A * V215

    if V21e < V21a:
        diccionario["21.0"] = True
    else:
        diccionario["21.0"] = False

    V215e = coste_e + Petminus5_A * V21 + Pet_A * V215 + Petplus5_A * V22 + Petplus1_A * V225
    V215a = coste_a + Patminus5_A * V21 + Pat_A * V215 + Patplus5_A * V22

    if V215e < V215a:
        diccionario["21.5"] = True
    else:
        diccionario["21.5"] = False

    V225e = coste_e + Petminus5_A * V22 + Pet_A * V225 + Petplus5_A * V23 + Petplus1_A * V235
    V225a = coste_a + Patminus5_A * V22 + Pat_A * V225 + Patplus5_A * V23

    if V225e < V225a:
        diccionario["22.5"] = True
    else:
        diccionario["22.5"] = True

    V23e = coste_e + Petminus5_A * V225 + Pet_A * V23 + Petplus5_A * V235 + Petplus1_A * V24
    V23a = coste_a + Patminus5_A * V225 + Pat_A * V23 + Patplus5_A * V235

    if V23e < V23a:
        diccionario["23.0"] = True
    else:
        diccionario["23.0"] = False

    V235e = coste_e + Petminus5_A * V23 + Pet_A * V235 + Petplus5_A * V24 + Petplus1_A * V245
    V235a = coste_a + Patminus5_A * V23 + Pat_A * V235 + Patplus5_A * V24

    if V235e < V235a:
        diccionario["23.5"] = True
    else:
        diccionario["23.5"] = False

    V24e = coste_e + Petminus5_A * V235 + Pet_A * V24 + Petplus5_A * V245 + Petplus1_A * V25
    V24a = coste_a + Patminus5_A * V235 + Pat_A * V24 + Patplus5_A * V245

    if V24e < V24a:
        diccionario["24.0"] = True
    else:
        diccionario["24.0"] = False

    V245e = coste_e + Pe25_245 * V25 + Pe245_245 * V245 + Pe24_245 * V24
    V245a = coste_a + Pa25_245 * V25 + Pa245_245 * V245 + Pa24_245 * V24

    if V245e < V245a:
        diccionario["24.5"] = True
    else:
        diccionario["24.5"] = False

    V25e = coste_e + Pe25_25 * V25 + Pe245_25 * V245
    V25a = coste_a + Pa25_25 * V25 + Pa245_25 * V245

    if V25e < V25a:
        diccionario["25.0"] = True
    else:
        diccionario["25.0"] = False

    print(diccionario)
    return diccionario


if __name__ == "__main__":
    control()
