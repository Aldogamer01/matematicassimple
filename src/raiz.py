from decimal import Decimal
def raiz(raiz : int, numero : float) -> float :
    """
    Para obtener la raiz de x numero, puedes
    usar el siguiente codigo de ejemplo:


    from matematicassimple import raiz

    raiz(raiz=2, numero=8) #Obtiene la raiz cuadrada de 8
    """
    if raiz < 1:
        raise ValueError("Asegurese de que la raiz sea mayor a 0")
    elif numero <= 0:
        raise ValueError("Asegurese de que el numero sea mayor a 0")
    return float("{:.2f}".format(Decimal(numero)**Decimal(1/raiz)))