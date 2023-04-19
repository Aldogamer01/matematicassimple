def primo(numero: int) -> bool:
    """
    Para saber si un numero es primo o no,
    puede usar el siguiente codigo de
    ejemplo:

    
    from matematicassimple import primo

    primo(numero=7)
    """
    if numero <= 1:
        raise ValueError("Ingrese un numero mayor a 1")
    for i in range(numero-1):
        if numero/(i+1) == int(numero/(i+1)) and i != 0:
            return False
    return True