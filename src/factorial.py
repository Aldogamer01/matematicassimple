def factorial(numero: int) -> int:
    """
    Para obtener la factorial
    de un numero, es tan facil
    como insertal el siguiente,

    Ejemplo:


    from matematicassimple import factorial

    factorial(numero=7)
    """
    res = 1
    if numero == 1:
        return res
    elif numero == 0:
        return 0
    elif numero > 0:
        for i in range(numero):
            res = res * (numero-i)
        return res
    else:
        numero = -numero
        for i in range(numero):
            res = res * (numero-i)
        return -res