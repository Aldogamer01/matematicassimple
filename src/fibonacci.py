def fibonacci(repeticiones: int) -> list:
    """
    Un fibonacci es una secuencia obtenida
    sumando el numero anterior con el actual,
    empezando con 1 y 1.

    Para obtener el fibonacci, 
    use el codigo de ejemplo:


    from matematicassimple import fibonacci

    fibonacci(repeticiones=7) #Obtiene el fibonacci con 7 repeticiones
    """
    if repeticiones <= 0:
        raise ValueError("Ingrese numeros positivos mayor a 0")
    res = 1
    previous = 0
    lista = []
    for i in range(repeticiones):
        lista.append(res)
        res = res + previous
        previous = res-previous
    return lista