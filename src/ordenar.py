def ordenar(alreves : bool, numeros : list) -> list:
    '''
    Para ordenar los numeros de menor a mayor, puedes usar esta funcion de la siguiente manera:

    
    from matematicassimple import ordenar

    ordenar(alreves=False, numeros=[4,1,0,9,32,51,6,2,8,43])

    
    De lo contrario, si es de mayor a menor, usa lo siguiente:

    
    from matematicassimple import ordenar

    ordenar(alreves=True, numeros=[4,1,0,9,32,51,6,2,8,43])
    '''
    if numeros == []:
        raise ValueError("La lista no puede estar vacia")
    elif len(numeros) == 1:
        return numeros
    elif alreves == False:
        restador = 0
        acum = 0
        while True:
            menor = None
            posmen = 0
            for i in range(len(numeros) - restador - 1):
                if menor != None:
                    if numeros[acum] < numeros[i+acum+1] and numeros[acum] < menor:
                        posmen = acum    
                    elif numeros[acum] > numeros[i+acum+1] and numeros[acum+i+1] < menor:
                        posmen = i+acum+1
                    menor = numeros[posmen]
                else:
                    if numeros[acum] < numeros[i+acum+1]:
                        posmen = acum
                    elif numeros[acum] > numeros[i+acum+1]:
                        posmen = i+acum+1
                    menor = numeros[posmen]
            if posmen != acum:
                numeros[posmen] = numeros[acum]
                numeros[acum] = menor
            acum = acum + 1
            restador = restador + 1
            if restador == len(numeros)-1:
                if numeros[len(numeros)-2] > numeros[len(numeros)-1]:
                    menor = numeros[len(numeros)-1]
                    numeros[len(numeros)-1] = numeros[len(numeros)-2]
                    numeros[len(numeros)-2] = menor
                break
        return numeros   
    else:
        restador = 0
        acum = 0
        while True:
            mayor = None
            posmay = 0
            for i in range(len(numeros) - restador - 1):
                if mayor != None:
                    if numeros[acum] > numeros[i+acum+1] and numeros[acum] > mayor:
                        posmay = acum    
                    elif numeros[acum] < numeros[i+acum+1] and numeros[acum+i+1] > mayor:
                        posmay = i+acum+1
                    mayor = numeros[posmay]
                else:
                    if numeros[acum] > numeros[i+acum+1]:
                        posmay = acum
                    elif numeros[acum] < numeros[i+acum+1]:
                        posmay = i+acum+1
                    mayor = numeros[posmay]
            if posmay != acum:
                numeros[posmay] = numeros[acum]
                numeros[acum] = mayor
            acum = acum + 1
            restador = restador + 1
            if restador == len(numeros)-1:
                if numeros[len(numeros)-2] < numeros[len(numeros)-1]:
                    mayor = numeros[len(numeros)-1]
                    numeros[len(numeros)-1] = numeros[len(numeros)-2]
                    numeros[len(numeros)-2] = mayor
                break
        return numeros 