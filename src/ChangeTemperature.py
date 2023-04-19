def temperatura(conversion: int, grados: float) -> float:
    '''
    Para convertir Celcius a Fahrenheit, puede hacerlo de la siguiente manera:

    
    from matematicassimple import temperatura

    grados = 36.5

    temperatura(conversion=1, grados=grados)  


    Para convertir Fahrenheit a Celcius, puede hacerlo de la siguiente manera:


    from matematicassimple import temperatura

    grados = 75.9

    temperatura(conversion=2, grados=grados)
    '''
    if conversion == 1:
        return grados*1.8+32
    elif conversion == 2:
        return (grados-32)/1.8
    else:
        raise ValueError("Inserte una conversion valida.")