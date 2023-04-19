from typing import overload
@overload
def raiz(raiz : int, numero = float) -> float : ...
def raiz(raiz, numero):
    """
    Para obtener la raiz de x numero, puedes
    usar el siguiente codigo de ejemplo:


    from matematicassimple import raiz

    raiz(raiz=2, numero=8) #Obtiene la raiz cuadrada
    """
    if raiz < 1:
        raise ValueError("Asegurese de que la raiz sea mayor a 1")
    elif raiz == 1:
        return numero
    elif numero == 0:
        return 0
    elif numero < 0:
        raise ValueError("Asegurese de usar numeros positivos")
    res = numero
    for i in range(raiz-1):
        res = res ** 0.5
    return res