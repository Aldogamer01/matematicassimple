def ordenar(alreves : bool, numeros : list) -> list:
    '''
    Para ordenar los numeros de menor a mayor, puedes usar esta funcion de la siguiente manera:

    
    from matematicassimple import ordenar

    ordenar(alreves=False, numeros=[4,1,0,9,32,51,6,2,8,43])

    
    De lo contrario, si es de mayor a menor, usa lo siguiente:


    from matematicassimple import ordenar

    ordenar(alreves=True, numeros=[4,1,0,9,32,51,6,2,8,43])
    '''
    def merge_sort(numeros):
        if len(numeros) <= 1:
            return numeros
        mitad = len(numeros) // 2
        izquierda = numeros[:mitad]
        derecha = numeros[mitad:]
        izquierda = merge_sort(izquierda)
        derecha = merge_sort(derecha)
        return merge(izquierda, derecha)
    n = len(numeros)
    if numeros == []:
        raise ValueError("La numeros no puede estar vacia")
    elif n == 1:
        return numeros
    elif alreves == False:
        def merge(izquierda, derecha):
            resultado = []
            i = 0
            j = 0
            while i < len(izquierda) and j < len(derecha):
                if izquierda[i] < derecha[j]:
                    resultado.append(izquierda[i])
                    i += 1
                else:
                    resultado.append(derecha[j])
                    j += 1
            resultado += izquierda[i:]
            resultado += derecha[j:]
            return resultado
    else:
        def merge(izquierda, derecha):
            resultado = []
            i = 0
            j = 0
            while i < len(izquierda) and j < len(derecha):
                if izquierda[i] < derecha[j]:
                    resultado.append(derecha[j])
                    j += 1
                else:
                    resultado.append(izquierda[i])
                    i += 1
            resultado += izquierda[i:]
            resultado += derecha[j:]
            return resultado
    return merge_sort(numeros)