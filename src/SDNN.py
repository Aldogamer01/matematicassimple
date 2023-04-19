def SDNN(numero : int) -> int:
    """
    La suma de numeros naturales
    es una suma que consiste en
    sumar todos los numeros
    naturales desde el 0
    hasta el numero insertado.

    Para obtener la suma de numeros
    naturales, use el siguiente 
    codigo de ejemplo:


    from matematicassimple import SDNN

    SDNN(numero=5)
    """
    if numero < 0:
        raise ValueError("Ingrese un valor mayor a 0")
    res = 0
    for i in range(numero):
        res = res + (numero-i)
    return res