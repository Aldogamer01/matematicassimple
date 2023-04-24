def elevado(al: int, numero: float) -> float:
    """
    Para elevar un numero al cuadrado, cubico o algun
    otro numero, puede hacerlo de la siguiente manera:


    from matematicassimple import elevado

    elevado(al=2, numero=46)
    """
    res = numero
    if al < 1:
        raise ValueError("Asegurese de elevarlo a un numero mayor a 1")
    for i in range(al-1):
        res = numero*res
    return res
